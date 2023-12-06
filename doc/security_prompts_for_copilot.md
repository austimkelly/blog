
**Contents**

* [Audience](#audience)
    * [Security Basic Pre-requisites](#security-basic-pre-requisites)
* [Limitations](#limitations)
* [TL;DR](#tldr)
* [File Scope Prompts w/ Example Output](#prompts-with-example-output-scope--file)
* [Code Fragment Prompts](#prompts-for-code-fragments)
* [Typical LLM Disclaimers](#typical-llm-disclaimers)

# Security Prompts for [Github Copilot](https://github.com/features/copilot). 

If you are using Github Copilot in your IDE (e.g. Visual Studio Code), this document provides Application Security prompts that can assist any software developer to write more secure code. It's like having an Application Security Engineer in your back-pocket! When complimented with a code scanning tool, Copilot + Security prompts will be a massive time saver for software engineers to understand the nature, impact, and remediation of security vulnerabilities.

No code scanning tool is perfect and there will invariably many false negatives (vulnerabilities missed) and false positives (vulnerability flagged where there is none) alerts in any code.  These prompts can not only help you to discover vulnerabilities that code scanner may have missed, but also provide a way to better gauge the actual risk and remediation of any particular code vulnerability.

# Audience

Software developers who have a ~~requirement~~ desire to write and review code to ensure safety and security of user data and systems. 

## Security Basic Pre-requisites

The prompts also assume the intended audience has a basic understand of the following security principles. All software engineers writing security code should have awareness of these areas:

* Static code analysis and alerts
* What threat modeling is. If you don't, see [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling) summary
* What a Common Web Exploit is. If not, please see [What is CWE](https://cwe.mitre.org/about/index.html).

# Limitations

* Prompts for Copilot will only work on individual files or highlighted code snippets. It is not yet possible to evaluate security posture over multiple source files or an [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree).
* At the time of this writing, it does not appear that any LLM such as Copilot is integrated into Github Advanced Security. However, Github has announced [AI Powered AppSec](https://github.com/features/preview/security) that will likely make a lot of these workflows native to the developer experience.

# TL;DR

Here's the bulleted list of prompts you can feed to Copilot:

* `Do a security code review on this file. Separate out the results with a summary of the problems, potential exploits, the type of security vulnerability, and recommended code changes.`
* `Provide a threat analysis in the STRIDE format`
* `Provide a threat analysis in the PASTA format`
* `Provide links to any CWE related to security vulnerabilities found.`
* `Please provide an example or examples of how to exploit found vulnerabilities in this code.`
* `Fix this security vulnerability`
* `Please fix code alert for {code alert summary}`
*  A multi-step prompt for full report:

   ```
   Analyze this code and provide results for each vulnerability found. For each vulnerability include the following sections:
    1. Summary of the Vulnerably, including lines of offending code
    2. Recommendation for fixing. Please include a code example for what fix should be.
    3. A generic vulnerable code example, in the same language as the found vulnerability. This should demonstrate a snippet of the vulnerability.
    4. An example of how an attacker might exploit this vulnerability
    5. A References Section with OWASP articles on the found vulnerability and a list of related CWEs, all with hyperlinks.```


# Prompts with Example Output: Scope = File

Here are prompts that I've found useful when asking general questions about a file:

## Prompt: Basic open ended security analysis

```
Do a security code review on this file. Separate out the results with a summary of the problems, potential exploits, the type of security vulnerability, and recommended code changes.
```

### Example Copilot Result

**Source for prompt**: [sqli.py](https://github.com/austimkelly/swiss-cheese/blob/main/sqli/sqli.py)

<details>
<summary>Generic Security Summary on SQL Injection</summary>
### Summary of the Problems

1. The provided code is relatively secure. It uses parameterized queries to interact with the SQLite database, which helps prevent SQL Injection attacks. However, there are a few potential improvements that could be made.

2. Lack of User Input Validation: The vulnerable_query function does not perform any validation on the username parameter before using it in a SQL query. While the use of parameterized queries mitigates the risk of SQL injection, it's still a good practice to validate user input.

### Potential Exploits

Given the use of parameterized queries, there are no clear exploits in this code. However, if user input validation is not performed elsewhere in the application, it could potentially lead to other types of attacks, such as business logic errors.

### Type of Security Vulnerability

The potential vulnerabilities in this code are related to Input Validation and Error Handling (CWE-20) and Insufficiently Protected Credentials (CWE-522).

### Recommended Code Changes

1. User Input Validation: Add validation checks for the username parameter in the vulnerable_query function. For example, you could check if the username is a non-empty string and does not contain any special characters.

```python
def vulnerable_query(username):
    # Validate username
    if not isinstance(username, str) or not username.isalnum():
        raise ValueError("Invalid username")

    # Rest of the code...
```

2. Database Connection Handling: Consider using a context manager to handle the database connection. This will ensure that the connection is properly closed even if an error occurs.

```python
def vulnerable_query(username):
    # Validate username
    if not isinstance(username, str) or not username.isalnum():
        raise ValueError("Invalid username")

    # Use a context manager to handle the database connection
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, (username,))
        results = cursor.fetchall()

    return results
```

### References
OWASP: [Injection Prevention Cheat Sheet](https://owasp.org/www-community/attacks/SQL_Injection in Python
CWE-20: [Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)
CWE-522: [Insufficiently Protected Credentials](https://cwe.mitre.org/data/definitions/522.html)

</details>

## Prompt: Analyis using STRIDE (Threat Analysis)

See [OWASP STRIDE](https://owasp.org/www-community/Threat_Modeling_Process#stride) for a summary of what STRIDE is an how it cna help you understand attacker goals. 

```
Provide a threat analysis in the STRIDE format
```

### Example Copilot Result

**Source for prompt**: [ssrf.py](https://github.com/austimkelly/swiss-cheese/blob/main/ssrf/ssrf.py)

<details>
<summary>Threat Analysis using STRIDE</summary>

STRIDE is a model for identifying security threats. It stands for Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege. Here's a threat analysis of the provided code snippet using the STRIDE format:

Spoofing: Not applicable. The code does not involve any authentication mechanism where identity spoofing could be a concern.

Tampering: The code is vulnerable to Server-Side Request Forgery (SSRF). An attacker could tamper with the url parameter in the /follow route to make the server send a request to an arbitrary URL.

Repudiation: Not applicable. The code does not involve any actions where tracking or logging would be necessary to provide evidence of activities.

Information Disclosure: The SSRF vulnerability could lead to information disclosure. An attacker could exploit this vulnerability to access sensitive information from internal resources that the server can access.

Denial of Service: The SSRF vulnerability could potentially be used to perform a Denial of Service (DoS) attack. An attacker could make the server send numerous requests to a specific URL, potentially overloading the server or the target URL.
</details>

## Prompt: Analysis using PASTA (Threat Analysis)

PASTA is nother popular threat modeling technique that may provide another perspective. See [OWASP Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) for more details on PASTA threat modeling. 

```
Provide a threat analysis in the PASTA format
```

### Example Copilot Result

**Source for prompt**: [idor.py](https://github.com/austimkelly/swiss-cheese/blob/main/idor/idor.py)

<details>
<summary>Threat Analysis using PASTA</summary>
PASTA (Process for Attack Simulation and Threat Analysis) is a risk-centric threat modeling framework designed to identify and evaluate risk at the application level. Here's a threat analysis of the provided code snippet using the PASTA format:

Definition of Technical Scope: The code is a Flask application with two routes: one for getting user details by ID (/api/users/<int:user_id>) and one for updating user details by ID (/api/users/<int:user_id>). The data is stored in a dummy list of users.

Identification and Evaluation of Threats: The main threat is Insecure Direct Object References (IDOR). An attacker could potentially manipulate the user_id parameter in the update route to modify the details of any user.

Application Vulnerability Analysis: The application is vulnerable to IDOR because it does not perform any authentication or authorization checks before updating user details. This means that any user can update the details of any other user.

Attack Modeling: An attacker could exploit this vulnerability by sending a PUT request to the update route with the user_id of another user. This could allow the attacker to change the details of that user.

Risk Analysis: The risk associated with this vulnerability is high. If an attacker can change the details of other users, they could potentially gain access to sensitive information or perform actions on behalf of those users.

Residual Risk Analysis: The residual risk after the vulnerability is fixed would be low. Once proper authentication and authorization checks are implemented, an attacker would no longer be able to update the details of other users.

To mitigate this threat, you should implement proper authentication and authorization checks in the update_user function. Only authenticated users should be able to update user details, and they should only be able to update their own details or those of users they have permission to modify.
</details>

## Prompt: CWE References

[Common Weakness Enumeration](https://cwe.mitre.org/) (CWE) provides a common language for describing and categorizing software weaknesses in a standardized way, making it easier to identify, understand, and address security issues.

 ```
 Provide links to any CWE related to security vulnerabilities found.
 ```

**Source for prompt**: [broken-auth.py](https://github.com/austimkelly/swiss-cheese/blob/main/broken-auth/broken-auth.py)

### Example Copilot Result

<details>
<summary>CWE References</summary>
The provided code snippet has a couple of potential security vulnerabilities:

Hardcoded Secret: The application's secret key is hardcoded as b'secret_key'. This is a bad practice as it exposes the secret key in the source code, which could lead to various security issues if the code is ever exposed. This vulnerability is related to the CWE-798: Use of Hard-coded Credentials. You can read more about it here.

Insecure Storage of Sensitive Information: The passwords for the users are stored in plaintext in the users dictionary. This is a serious security issue as anyone with access to the code or the runtime environment could easily read these passwords. This vulnerability is related to the CWE-256: Unprotected Storage of Credentials. You can read more about it here.

Please note that CWE (Common Weakness Enumeration) is a community-developed list of software and hardware weakness types. It serves as a common language for describing vulnerabilities and a standard measuring stick for software and hardware tools targeting these weaknesses. CVE (Common Vulnerabilities and Exposures), on the other hand, is a list of publicly disclosed cybersecurity vulnerabilities and exposures. The provided code snippet does not have any specific CVEs associated with it.
</details>

## Prompt: Providing exploit examples

One of the most important aspects of vulnerability management is reachability and reproducibility: can this reported vulnerability be reachable and can you provide a reproducible case. 

```
Please provide an example or examples of how to exploit found vulnerabities in this code.
```

**Source for prompt**: [xss.py](https://github.com/austimkelly/swiss-cheese/blob/main/xss/xss.py)

### Example Copilot Result

<details>
<summary>XSS Exploit Response</summary>
The code you've provided is vulnerable to Cross-Site Scripting (XSS) attacks. This is because it takes user input from a form and directly displays it on the webpage without any sanitization.

Here's an example of how an attacker could exploit this vulnerability:

1. The attacker submits the form with the following input: When the form is submitted, the server will render the index.html template with the user_input variable set to the attacker's input.

`<script>alert('XSS Attack!')</script>`

2. The malicious script is then executed in the browser of anyone who views the page. In this case, it would display a popup with the message "XSS Attack!", but it could also be used to steal sensitive information or perform actions on behalf of the user.

3. To prevent this type of attack, you should always sanitize user input before displaying it on a webpage. This can be done by escaping special characters, using safe functions to display user input, or using a library or framework that automatically sanitizes user input.

</details>


# Prompts for Code Fragments

Here are prompts I've found useful when working with a line or block of code. These are very straight foward so did no include any sample output.

## Prompt: Fix a vulnerability

```
Fix this security vulnerability
```

## Prompt: Fix a vulnerability from a specific code alert

```
Please fix code alert for {code alert summary}
```

For example,  `Please fix code alert for "Full server-side request forgery"`


#  Putting it all together: Generating Full Analysis Report

This one would will work on the file level best. I built a prompt to try to recreate the format of a CodeQL alert. For my tests, it does a pretty good job at identifying problems, fixes and CWE references.  It may provide broken links in the references depending on the age of the training data set.

## Prompt: Full analysis report

```
Analyze this code and provide results for each vulnerability found. For each vulnerability include the following sections:

1. Summary of the Vulnerability, including lines of offending code
2. Recommendation for fixing. Please include a code example for what fix should be.
3. A generic vulnerable code example, in the same language as the found vulnerability. This should demonstrate a snippet of the vulnerability.
4. An example of how an attacker might exploit this vulnerability
5. A References Section with OWASP articles on the found vulnerability and a list of related CWEs, all with hyperlinks.
```

## Example result for full analysis report

Source for prompt: [broken-auth.py](https://github.com/austimkelly/swiss-cheese/blob/main/broken-auth/broken-auth.py)

Note that Github Advanced Security + CodeQL did not alert on any of these vulnerability.

<details>
<summary>Security Vulnerabilities Analysis - Full Report</summary>

## Vulnerability 1: Hardcoded Secret Key

### Summary of the Vulnerability
The application's secret key is hardcoded as `b'secret_key'` on line 5. This is a bad practice as it exposes the secret key in the source code, which could lead to various security issues if the code is ever exposed.

### Recommendation for Fixing
The secret key should be stored in an environment variable or a secure configuration that is not included in the source code.

```python
import os
app.secret_key = os.environ.get('SECRET_KEY')
```

### Generic Code Example
```python
app = Flask(__name__)
app.secret_key = 'hardcoded_secret_key'
```

### Example of How an Attacker Might Exploit This Vulnerability

If an attacker gains access to the source code, they could use the secret key to forge session cookies or perform other attacks that require knowledge of the secret key.

### References

* [OWASP: Using Hard-coded Cryptographic Key](https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_password)
* [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)

## Vulnerability 2: Insecure Storage of Sensitive Information

### Summary of the Vulnerability

The passwords for the users are stored in plaintext in the users dictionary on lines 8-10. This is a serious security issue as anyone with access to the code or the runtime environment could easily read these passwords. 

### Recommendation for Fixing

Passwords should be hashed using a secure hashing algorithm before they are stored. When a user logs in, the entered password should be hashed and compared to the stored hash.

```python
from werkzeug.security import generate_password_hash, check_password_hash

users = {
    'user1': {'password': generate_password_hash('password1')},
    'user2': {'password': generate_password_hash('password2')},
}

# In the login route
if username in users and check_password_hash(users[username]['password'], password):
    # ...
```

### Generic Vulnerable Code Example

```python
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'},
}
```

### Example of How an Attacker Might Exploit This Vulnerability

If an attacker gains access to the user data, they could read the plaintext passwords and use them to log in as any user.

### References

* [OWASP: Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
* [CWE-256: Unprotected Storage of Credentials](https://cwe.mitre.org/data/definitions/256.html)
* [CWE-319: Cleartext Transmission of Sensitive Information](https://cwe.mitre.org/data/definitions/319.html)

## Vulnerability 3: Inappropriate Session Timeout

### Summary of the Vulnerability

The code checks if the time difference between the current time and last_active_time is greater than 5000 days, and if so, it deletes the 'username' from the session (lines 2-4). This is an extremely long time for a session to be active, which could potentially allow an attacker to use an old session.

### Recommendation for Fixing

The session timeout should be much shorter for security reasons. Here's how you can set the session timeout to 30 minutes in Flask:

```python
from datetime import timedelta
from flask import Flask, session

app = Flask(__name__)
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
```

### Generic Vulnerable Code Example

```python
import datetime
last_active_time = datetime.datetime.now()
current_time = datetime.datetime.now()

if (current_time - last_active_time).days > 5000:
    del session['username']
```

### Example of How an Attacker Might Exploit This Vulnerability

If an attacker manages to obtain a valid session (for example, via session hi-jacking or session fixation), they could potentially use this session to impersonate the user for up to 5000 days, as the session is not invalidated for this period.

### References
[OWASP: Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
[CWE-613: Insufficient Session Expiration](https://cwe.mitre.org/data/definitions/613.html)

</details>

## Getting Copilot to format markdown

While generated results in the Copilot side-bar look great, it does not do so great at generating full markdown. It tends to break formatting after code snippets. Hence, in order to show the examples here I had to do a bit of hand-formatting.

## Typical LLM disclaimers

* Results should be taken as suggestions and may be misleading or incorrect. LLMs work by pattern matching and suggesting the most likely response to your query. Human brain is still required.
* The Copilot LLM is based on Github source code for training data. See [Inside Github: Working with the LLMs behind Github Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-Copilot/).
* Be sure to read [Copilot Exclusins](https://docs.github.com/en/Copilot/managing-Copilot-business/configuring-content-exclusions-for-github-Copilot) and [Training Data](https://docs.github.com/en/Copilot/overview-of-github-Copilot/about-github-Copilot-individual#about-github-Copilot) for how to exclude content from suggestions and what data Github uses to train models.
* Prompts aren't replacements for Application Security Experts, code scanners, pen testing, or bug bounty programs. 
