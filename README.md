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

3.  **Install Django:**

    Install the Django framework.

    ```bash
    pip install django
    ```

4.  **Install other dependencies:**

    Install the remaining required Python packages using pip and the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

5.  **Apply database migrations:**

    Set up the database schema by running the migrations.

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (optional but recommended for accessing Django Admin):**

    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin user.
