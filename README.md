# Employee Management System

A simple web application built with Django for managing employee data (CRUD operations).

## Features

-   Add new employees
-   View a list of existing employees
-   Edit employee details
-   Delete employees

## Prerequisites

Before you begin, ensure you have met the following requirements:

*   Python 3.6+ installed
*   Git installed

## Setup and Installation

Follow these steps to get the project running on your local machine:

1.  **Clone the repository:**

    ```bash
    git clone <URL_REPO_GITHUB_ANDA>
    cd python-project # Sesuaikan dengan nama folder project Anda jika berbeda
    ```
    Replace `<URL_REPO_GITHUB_ANDA>` with the actual URL of your GitHub repository.

2.  **Create and activate a virtual environment:**

    It's highly recommended to use a virtual environment to manage project dependencies.

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install dependencies:**

    Install the required Python packages using pip and the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**

    Set up the database schema by running the migrations.

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional but recommended for accessing Django Admin):**

    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin user.

## Running the Application

1.  **Start the Django development server:**

    Make sure your virtual environment is activated.

    ```bash
    python manage.py runserver
    ```

2.  **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

    You can access the Django Admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials you created.
