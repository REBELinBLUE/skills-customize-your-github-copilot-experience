# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and build modern REST APIs using the FastAPI framework. You'll create endpoints for a simple application, handle HTTP methods, work with request/response models, and understand REST principles.

## 📝 Tasks

### 🛠️ Create a Todo API

#### Description

Build a REST API for managing a simple todo list application. The API should support creating, reading, updating, and deleting todo items. Use FastAPI to define routes, Pydantic models for data validation, and implement proper HTTP status codes.

#### Requirements

Completed program should:

- Create a FastAPI application with endpoints for GET, POST, PUT, and DELETE operations
- Define a Pydantic model for todo items (with fields like id, title, description, completed)
- Implement in-memory storage for todo items
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Include query parameters to filter todos by completion status


### 🛠️ Add Data Validation and Error Handling

#### Description

Extend your todo API with robust data validation and comprehensive error handling. Implement request validation using Pydantic, handle edge cases, and return meaningful error messages to API clients.

#### Requirements

Completed program should:

- Validate incoming request data using Pydantic models
- Return proper error responses with descriptive messages
- Handle cases like missing todo items, invalid input, and duplicate operations
- Include request validation for required and optional fields
- Demonstrate consistent error response format across all endpoints
