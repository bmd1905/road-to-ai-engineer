# FastAPI Auth Example

Welcome to the **FastAPI Auth Example**, a simple but robust authentication system built with FastAPI. This project demonstrates how to implement user authentication using OAuth2 with JSON Web Tokens (JWT), providing secure access to protected routes within your application.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [User Routes](#user-routes)
- [Authentication Flow](#authentication-flow)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication**: Secure user login with OAuth2 and JWT.
- **Protected Routes**: Access user-specific data through authenticated endpoints.
- **Password Handling**: Passwords are hashed using bcrypt for secure storage.
- **Configurable Settings**: Easily manage application settings via environment variables.
- **Modular Design**: Organized codebase with clear separation of concerns.

## Project Structure

```text
.
├── auth
│ ├── init.py
│ ├── config.py
│ ├── dependencies.py
│ ├── exceptions.py
│ ├── router.py
│ ├── schemas.py
│ ├── service.py
│ └── utils.py
├── users
│ ├── init.py
│ └── routes.py
├── main.py
└── requirements.txt
```

- **auth/**: Contains all authentication-related modules, including configuration, dependencies, schemas, services, and utilities.
- **users/**: Handles user-related routes and functionalities.
- **main.py**: The entry point of the application where the FastAPI app is initialized and routers are included.
- **requirements.txt**: Lists all the Python dependencies required for the project.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- **Python 3.8+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python package installer. It typically comes with Python.

### Installation

1. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - **Windows**

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or MacOS**

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

The application uses environment variables for configuration. You can set them directly in your environment or create a `.env` file in the project root.

#### Environment Variables

- `SECRET_KEY`: Secret key for JWT encoding. **Default**: `secret-key`
- `ALGORITHM`: Algorithm used for JWT. **Default**: `HS256`
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes. **Default**: `30`

#### Example `.env` File

Create a `.env` file in the project root and add the following:

```bash
SECRET_KEY=your-secret-key
```

The `SECRET_KEY` is crucial for the security of your JWT. It should be a long, random string. In production, consider using a more secure method to manage secrets. 

To generate a random secret key, you can use the following command:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

- **Parameters**:
  - `main:app`: Refers to the `app` instance in `main.py`.
  - `--reload`: Enables auto-reloading on code changes (useful during development).

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Authentication

#### **POST** `/auth/token`

**Description**: Authenticate a user and issue a JWT access token.

**Request Parameters**:

- `username` (form data): The user's username.
- `password` (form data): The user's password.

**Response**:

- `access_token`: The generated JWT token.
- `token_type`: The type of token (`bearer`).

**Example Request**:

```bash
curl -X POST "http://127.0.0.1:8000/auth/token" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=bmd&password=secret"
```

**Example Response**:

```json
{
  "access_token": "your-jwt-token",
  "token_type": "bearer"
}
```

### User Routes

#### **GET** `/users/me`

**Description**: Retrieve information about the currently authenticated user.

**Headers**:

- `Authorization`: `Bearer <access_token>`

**Response**:

- `username`: The user's username.
- `email`: The user's email.
- `full_name`: The user's full name.
- `disabled`: Whether the user is disabled.

**Example Request**:

```bash
curl -X GET "http://127.0.0.1:8000/users/me" \
-H "Authorization: Bearer your-jwt-token"
```

**Example Response**:

```json
{
  "username": "bmd",
  "email": "bmd@example.com",
  "full_name": "BMD",
  "disabled": false
}
```

## Authentication Flow

1. **User Login**:
   - The user sends a POST request to `/auth/token` with their `username` and `password`.
   - The server authenticates the credentials using the `authenticate_user` function in `auth/service.py`.
   - If authentication is successful, a JWT access token is created using `create_access_token` from `auth/utils.py`.
   - The token is returned to the user.

2. **Accessing Protected Routes**:
   - The user includes the JWT token in the `Authorization` header of their requests (e.g., `Authorization: Bearer <token>`).
   - For protected routes like `/users/me`, the `get_current_user` dependency in `auth/dependencies.py` is invoked.
   - The token is decoded to extract the username, and the corresponding user is retrieved from the database.
   - If the token is valid and the user exists, the request proceeds; otherwise, a 401 Unauthorized error is returned.

3. **Password Handling**:
   - Passwords are securely hashed using bcrypt via the `passlib` library.
   - During login, the provided plaintext password is verified against the hashed password stored in the database.

## Security Considerations

- **Secret Key Management**: Ensure that the `SECRET_KEY` is kept confidential and not exposed in version control systems.
- **Database Integration**: The current implementation uses an in-memory "fake" database (`fake_users_db`) for demonstration purposes. Replace this with a persistent database (e.g., PostgreSQL, MongoDB) for production use.
- **HTTPS**: Always deploy the application over HTTPS to secure data in transit.
- **Token Expiration**: Adjust the `ACCESS_TOKEN_EXPIRE_MINUTES` based on your security requirements.
- **Error Handling**: Customize error messages to avoid exposing sensitive information.

---

*Happy Coding! 🚀*