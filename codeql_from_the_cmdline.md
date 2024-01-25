I thought doing off-line, local checkout analysis of a source code repository [using CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/about-the-codeql-cli) would be pretty straightforward and fast. It wasn’t. Here’s what I learned. If are writing custom queries or are using a self-hosted solution this makes sense, but for a quick scan of a repo, it’s not worth the effort.

# Basic steps.

The installation, configuration, and execution docs are pretty lengthy to digest so here are some key points:

* You need to create one CodeQL DB per language, per repo first before scanning.
* You need to scan one language at a time. Scans of even small repositories can take 10s of minutes.
* Results can be in CSV or SARIF format. CVS format lacked severity and just called everything “error”
* Compiled languages require extra configuration to define build steps.

# Example Execution

Here’s an example run on a repository checked out on a local machine called [swiss-cheese](https://github.com/austimkelly/swiss-cheese). This repo has known python vulnerabilities (for demonstration only):

1. Create the DBs (make codeql-dbs directory first):

```bash
codeql database create ./codeql-dbs/example-repo-multi \
	 --db-cluster --language python,javascript \
	--source-root ./swiss-cheese --overwrite
```

2. Run the javascript scan:

```bash
codeql database analyze ./codeql-dbs/example-repo-multi/javascript --format=CSV \
--output=./results_javascript.csv
```

3. Run the python scan:

```bash
codeql database analyze ./codeql-dbs/example-repo-multi/python --format=CSV \
--output=./results_python.csv
```

## Results

Here's the CSV results. I didn't see any way to get the actual severity, making it hard to prioritize. 

```csv
"Full server-side request forgery","Making a network request to a URL that is fully user-controlled allows for request forgery attacks.","error","The full URL of this request depends on a [[""user-provided value""|""relative:///ssrf/ssrf.py:1:26:1:32""]].","/ssrf/ssrf.py","10","16","10","32"
"Flask app is run in debug mode","Running a Flask app in debug mode may allow an attacker to run arbitrary code through the Werkzeug debugger.","error","A Flask app appears to be run in debug mode. This may allow an attacker to run arbitrary code through the debugger.","/xss/xss.py","18","5","18","34"
"Reflected server-side cross-site scripting","Writing user input directly to a web page allows for a cross-site scripting vulnerability.","error","Cross-site scripting vulnerability due to a [[""user-provided value""|""relative:///ssrf/ssrf.py:1:26:1:32""]].","/ssrf/ssrf.py","10","16","10","37"
```

## What I didn't try

* Compiled languages (Java, C++, C#) require extra configuration to define build steps.
* SARIF - I didn't bother trying the SARIF format out.
* Tweaking query packs, like adding the extension packs.