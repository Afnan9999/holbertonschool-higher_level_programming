# Web Communication Basics and API Consumption Using curl

## Overview
This repository contains two tasks:
1. Understanding the basics of HTTP and HTTPS
2. Consuming data from an API using the command-line tool curl

---

# Task 1: Basics of HTTP and HTTPS

## Objective
To understand the difference between HTTP and HTTPS, learn the structure of HTTP requests and responses, and identify common HTTP methods and status codes.

---

## 1. Difference Between HTTP and HTTPS

HTTP (Hypertext Transfer Protocol) is used for communication between a client and a server. It does not provide security, meaning data is sent in plain text.

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to protect data from interception and tampering.

### Key Differences
- HTTP does not encrypt data.
- HTTPS encrypts data using SSL/TLS.
- HTTP URLs start with `http://`.
- HTTPS URLs start with `https://`.
- HTTPS ensures confidentiality, integrity, and authentication.

**Conclusion:**  
HTTPS is recommended for all modern websites, especially those handling sensitive information.

---

## 2. Structure of an HTTP Request and Response

### HTTP Request Structure
An HTTP request consists of:
- Request line (method, path, HTTP version)
- Headers (additional request information)
- Optional body (data sent to the server)

Example:

---

### HTTP Response Structure
An HTTP response consists of:
- Status line (HTTP version, status code, status message)
- Headers (response information)
- Body (requested content)

Example:

---

## 3. Common HTTP Methods

| Method | Description | Use Case |
|------|------------|---------|
| GET | Retrieves data | Loading a webpage |
| POST | Sends data | Submitting a form |
| PUT | Updates data | Updating user information |
| DELETE | Removes data | Deleting a resource |

---

## 4. Common HTTP Status Codes

| Status Code | Description | Scenario |
|-----------|------------|----------|
| 200 | OK | Page loads successfully |
| 301 | Moved Permanently | Redirecting HTTP to HTTPS |
| 400 | Bad Request | Invalid request |
| 404 | Not Found | Page does not exist |
| 500 | Internal Server Error | Server failure |

---

# Task 2: Consuming Data from an API Using curl

## Objective
To install and use curl from the command line to fetch data from a webpage and interact with a RESTful API.

---

## 1. Verifying curl Installation

```bash
curl --version
