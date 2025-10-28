# React & Django Full Stack CRUD Application

This repository hosts a project demonstrating the creation of a **full stack CRUD (Create, Read, Update, Delete) application**.

## 📖 Project Overview

The core purpose of this application is to build a website where users can **manipulate data related to books**. This manipulation covers the four foundational functions of a REST API:
*   **Create:** Adding new data to a database.
*   **Read:** Displaying data from a database on the website.
*   **Update:** Altering existing data.
*   **Delete:** Removing data.

The application focuses on handling simple book data: the **book title** and the **release year**.

## 🛠️ Tech Stack

This project integrates two primary frameworks and libraries:

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend** | **Django** (Python) | Backend framework for handling the API logic and database interactions. |
| **API Framework** | **Django Rest Framework** | Used to easily create the REST API endpoints. |
| **Frontend** | **React** (JavaScript) | Frontend Library for the user interface. |
| **App Generation** | **Vite** | Used as the recommended tool to generate the React application. |

## 📁 Project Structure

The project is deliberately separated into two main folders to facilitate clear structure and potentially separate deployment:

1.  `client`: Contains the **React/JavaScript** frontend code.
2.  `server`: Contains the **Django/Python** backend code.

## 🚀 Getting Started

### Prerequisites

While no prior knowledge of Django or React is required, users should have some understanding of **JavaScript and Python**. You must have **Python** and **pip** (the Python package manager) installed.

### Backend Setup (`server` folder)

1.  **Install Dependencies:** Install Django and the necessary API and CORS handling packages using `pip`.
    ```bash
    pip install django djangorestframework django-cors-headers
    ```
2.  **Configure Settings:** Ensure that `API`, `rest_framework`, and `corsheaders` are added to `INSTALLED_APPS` in `settings.py`. The `corsheaders.middleware.CorsMiddleware` must also be added to the `MIDDLEWARE` array.
3.  **Database Migration:** After defining the `Book` model (which uses `Charfield` for title and `IntegerField` for release year), run migrations:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
4.  **Run Server:** Start the Django development server.
    ```bash
    python3 manage.py runserver
    ```

### Frontend Setup (`client` folder)

1.  **Generate App:** Use Yarn and Vite to generate the React application, selecting **React** and **JavaScript**.
    ```bash
    yarn create vite app
    ```
2.  **Install Packages:** Navigate into the new application directory and install dependencies.
    ```bash
    yarn
    ```
3.  **Run Frontend:** Start the React development server.
    ```bash
    yarn dev
    ```

## ⚙️ API Endpoints

The API is built using Django views and serializers (to convert between Python models and JSON data). Endpoints are defined using URL paths that map to specific functions.

| Method | Route Pattern | Functionality | Key Requirements |
| :--- | :--- | :--- | :--- |
| **GET** | `/API/books/` | **Read:** Retrieves and returns all book entries from the database. | None. |
| **POST** | `/API/books/create` | **Create:** Accepts data (title, release year) in the request body (JSON) and saves a new entry. | Request Body (JSON data). |
| **PUT** | `/API/books/<int:pk>` | **Update:** Alters an existing book entry identified by its primary key (`PK`). | Primary Key (`PK`) in URL path and Request Body (new data). |
| **DELETE** | `/API/books/<int:pk>` | **Delete:** Removes an existing book entry identified by its primary key (`PK`). | Primary Key (`PK`) in URL path. |

***
