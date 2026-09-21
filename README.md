# Secure API Request

A Python project demonstrating secure API authentication using environment variables and Bearer Token authorization. This project follows industry-standard security practices by storing sensitive credentials in a `.env` file instead of hardcoding them into the source code.

---

## Features

- Secure API Key management using `.env`
- Load environment variables with `python-dotenv`
- Bearer Token authentication
- Custom HTTP headers
- GET request using the Requests library
- HTTP status code validation
- Exception handling with `try-except`
- Authentication error handling (401 Unauthorized)
- Clean command-line output

---

## Technologies Used

- Python 3
- Requests
- python-dotenv
- GitHub REST API

---

## Concepts Covered

- Environment Variables
- API Authentication
- Bearer Token
- Authorization Header
- HTTP Headers
- REST APIs
- HTTP Status Codes
- Error Handling
- Secure Coding Practices

---

## Project Structure

```
secure-api-request/
│
├── main.py
├── .env (Not uploaded to GitHub)
├── .gitignore
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/secure-api-request.git
```

Move into the project folder:

```bash
cd secure-api-request
```

Install dependencies:

```bash
pip install requests
pip install python-dotenv
```

---

## Create a .env File

Create a file named `.env` in the project directory.

Example:

```
API_KEY=your_api_key_here
```

---

## Run the Project

```bash
python main.py
```

---

## Example Output

### Valid API Key

```
==================================================
SECURE API REQUEST
==================================================

Status Code : 200

Login : octocat
Name : The Octocat
Followers : 5000
Public Repositories : 12

==================================================
THANK YOU
==================================================
```

---

### Invalid API Key

```
==================================================
SECURE API REQUEST
==================================================

Status Code : 401

Invalid API Key

==================================================
THANK YOU
==================================================
```

---

## Security

This project follows secure coding practices:

- API Keys are stored inside a `.env` file.
- `.env` is ignored using `.gitignore`.
- Sensitive credentials are never hardcoded into the source code.
- Authentication is handled using the Authorization header.

---

## Learning Outcomes

By building this project, I learned:

- Secure API authentication
- Environment Variables
- Using `python-dotenv`
- Loading secrets with `os.getenv()`
- Bearer Token authentication
- HTTP Headers
- Error handling
- Professional project structure
- Secure coding practices

---

## Future Improvements

- Interactive CLI menu
- Support for multiple APIs
- Retry mechanism
- Timeout handling
- Logging
- Unit testing
- Configuration management

---

## Author

Created as part of my AI Automation learning journey using Python, REST APIs, secure authentication, and professional software development practices.
