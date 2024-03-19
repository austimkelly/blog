An example of a malicious phishing attack header.

* "From" and "Return-Path" fields should match
* See if SPF is enabled. SPF stands for Sender Policy Framework and detects forged sender addresses. Not all email services use SPF, but most major ones like Gmail and Outlook do. If SPF says "Fail" or "SoftFail," it's likely spoofed.
* Check the IP address. The IP address indicates the network location of the email sender. Do a quick search to see if the IP address matches the sender's email service. If not, it's probably spoofed.
* Header fields like "Received" show the path the email took to get to you. The email should pass through servers that match the sender's email service. If there are unknown servers, especially at the beginning or end of the path, it may indicate spoofing.

Use https://mxtoolbox.com/ to check the SPF record and IP address.

```
Delivered-To: recipient@example.com
Received: from attacker-server.com (attacker-server.com [218.56.58.196])
        by mx.example.com (Postfix) with ESMTP id 1234567890
        for <recipient@example.com>; Tue, 01 Mar 2022 10:00:00 -0500 (EST)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=attacker-server.com;
        s=dkim; t=1646146800;
        bh=XnXH5ADatc2T4yFjQ4jvqSoLBUNnvHkMf9qUkT4QLLY=;
        h=From:To:Subject:Date:Message-ID:Content-Type;
        b=Wo4d2ldN35XpXgWUw5bX6neJ+VtJ6gyUVmFr1V6q3F5bR7XcQxxeMStK7oLx1dCv+
         F5OB2kROchLrB9cGaZsXyUqz6bncTT2qg9QFte9Kb9vgekzFiWmPjOTmVhMFQ0w8L+
         1mC2Jk+fQoUHcEVsYDdDDFj1cslpUjRmRLbVHnj1o=
Received-SPF: pass (attacker-server.com: domain of noreply@your-bank-phishing.com designates 203.0.113.1 as permitted sender)
Return-Path: <bounce-back@attacker-server.com>
From: "Your Bank" <noreply@your-bank-phishing.com>
To: recipient@example.com
Subject: Urgent: Security Alert - Please Verify Your Account
Date: Tue, 01 Mar 2022 10:00:00 -0500 (EST)
Message-ID: <1234567890@attacker-server.com>
Content-Type: text/plain; charset="utf-8"

Dear Customer,

We have detected unusual activity on your account. Please click the link below to verify your account information.

https://www.your-bank-phishing.com/verify-account

Thank you for your cooperation.

Sincerely,
Your Bank

```