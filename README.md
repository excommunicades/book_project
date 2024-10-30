# REST API Book Project ✅
![Blog Image](https://raw.githubusercontent.com/excommunicades/book_project/main/blog.jpg)

## DESCRIPTION: 

This project provides a RESTful API for managing a collection of books. It is built using Django and Django REST Framework, allowing for easy integration with web and mobile applications.

## This project is an example how to create a custom REST API using Django and Django REST Framework. The code serves as a practical guide to the following concepts:

* **Creating a Custom Web Server: Set up a web server using Django to handle HTTP requests.**
* **Building a Simple REST API: Implement a RESTful API for managing book data, including operations for creating, reading, updating, and deleting book entries.**
* **Data Serialization: Utilize serializers to format data for API responses and handle input validation.**
* **Error Handling: Implement robust error handling with appropriate HTTP status codes and messages.**
* **Clean URL Routing: Use Django's built-in routing features for intuitive endpoint management.**

## Key Features 💡

- **User Registration and Authentication:** Utilizes Django's robust user management framework, enhanced with JWT for secure token handling and authentication.
  secure token handling.
- **Book Management:** Enables users to create, read, update, and delete book entries through a simple RESTful API.
- **Data Serialization:** Uses Django REST Framework serializers to ensure proper formatting and validation of data for API interactions.
- **Database Integration:** Connects seamlessly to a PostgreSQL database, ensuring reliable data storage and retrieval.
  notifications or processing data asynchronously.

# Installation Guide 📕:

### Prerequisites 💻

Ensure you have Docker and Docker Compose installed on your machine. You can download them from:

- Docker: [Get Docker](https://docs.docker.com/get-docker/) 🐳
- Docker Compose: [Docker Compose](https://docs.docker.com/compose/install/) 🐳

### Environment Variables
Create a `.env` file in the root of your project directory with the following content:
```
    POSTGRES_DB=Books
    POSTGRES_USER=postgres 
    POSTGRES_PASSWORD=12345
```


1. **Clone the repository:** ```git clone https://github.com/excommunicades/book_project.git``` -> ```cd books-api```
2. **Build and run the application with Docker Compose:** ```docker-compose up --build```

# Stopping the Services 🚪


To run the test suite using pytest, you can use the test service defined in the docker-compose.yml file. This service will build the image and execute the tests in an isolated environment.

**To stop all running services, you can use:** ```docker-compose down```

### API Endpoints

- **POST** /api/books/: Create a new book entry. 🟡
- **GET** /api/books/: Retrieve all book entries. 🟢
- **GET** /api/books/{pk}/: Retrieve a specific book by its primary key. 🟢
- **PUT** /api/books/{pk}/: Update an existing book entry. 🟡
- **DELETE** /api/books/{pk}/: Delete a specific book entry. 🔴

# Running Tests ♻️

To run the test suite using pytest, you can use the test service defined in the docker-compose.yml file. This service will build the image and execute the tests in an isolated environment.

1. **Make sure your services are up and running:** ```docker-compose up -d```
2. **Execute the tests:** ```docker-compose run test```


# Conclusion

This setup provides a complete environment for developing and testing the Books API. Using Docker simplifies the process of managing dependencies and running tests, making it easier to ensure your application behaves as expected before deployment.

## Authors 😎

- **Stepanenko Daniil** - "Book project"