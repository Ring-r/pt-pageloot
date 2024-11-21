# Practical Task from Pageloot

This project is an **Expense Management API** built with **Django** and **Django REST Framework (DRF)**. The project allows users to manage their expenses with features like CRUD operations, date-range filtering, and category summaries.

---

## Prerequisites

To run this project, you will need the following tools installed:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)

---

## Setup Instructions

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/Ring-r/pt-pageloot.git
cd pt-pageloot
```

### 2. Build the Docker Image

To build the Docker image, run:

```bash
docker-compose build
```

### 3. Run the Containers

Start the application with:

```bash
docker-compose up -d
```

### 4. Run Database Migrations

To apply the database migrations (e.g., creating tables), run:

```bash
docker-compose exec app python manage.py migrate
```

### 5. Create a Superuser (Optional)

To access Django’s admin panel, create a superuser:

```bash
docker-compose exec app python manage.py createsuperuser
```

### 6. Access the Application

Once the containers are running, you can access the API at:

```
http://127.0.0.1:8000/
```

---

### 7. Stop the Containers

Stop the application with:

```bash
docker-compose down
```

## Available API Endpoints

Once the containers are running, you can access available API endpoints at:

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

### Expense Endpoints

#### 1. Create an Expense
- **Endpoint**: `/api/expenses/`
- **Method**: `POST`
- **Request body**:
  ```json
  {
    "title": "Lunch",
    "amount": 20.0,
    "date": "2024-11-21",
    "category": "Food",
    "user": 1
  }
  ```
- **Response**: `201 Created` with the expense data.

#### 2. List Expenses
- **Endpoint**: `/api/expenses/`
- **Method**: `GET`
- **Response**: A list of expenses.

#### 3. Get Expense by ID
- **Endpoint**: `/api/expenses/{id}/`
- **Method**: `GET`
- **Response**: Details of the expense with the given ID.

#### 4. Update an Expense
- **Endpoint**: `/api/expenses/{id}/`
- **Method**: `PUT`
- **Request body**:
  ```json
  {
    "title": "Updated Lunch",
    "amount": 25.0,
    "date": "2024-11-21",
    "category": "Food",
    "user": 1
  }
  ```
- **Response**: `200 OK` with the updated expense data.

#### 5. Delete an Expense
- **Endpoint**: `/api/expenses/{id}/`
- **Method**: `DELETE`
- **Response**: `204 No Content`

#### 6. List by Date Range
- **Endpoint**: `/api/expenses/by-date-range`
- **Method**: `GET`
- **Query Parameters**:
  - `start_date`: Start date for filtering (e.g., `2024-11-01`).
  - `end_date`: End date for filtering (e.g., `2024-11-30`).
  - `user`: User ID to filter expenses by.
- **Response**: A list of expenses in the given date range.

#### 7. Category Summary (Total Expenses by Category for a Month)
- **Endpoint**: `/api/expenses/category-summary/`
- **Method**: `GET`
- **Query Parameters**:
  - `month`: The month for which to get the category summary (e.g., `11`).
  - `year`: The yesr for which to get the category summary (e.g., `2024`).
  - `user`: User ID to filter expenses by.
- **Response**:
  ```json
  {
    "Food": 50.0,
    "Travel": 30.0,
    "Utilities": 100.0
  }
  ```
