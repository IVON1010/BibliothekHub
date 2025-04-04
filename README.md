# BibliothekHub
Welcome to BibliothekHub, a modern, user-friendly online library system built with Django. BibliothekHub allows users to easily manage their book borrowing activities, track borrowed books, and view borrowing histories. With a clean and intuitive interface, it simplifies the process of browsing and borrowing books, making it ideal for libraries of all sizes.

## Features
- **User Authentication**: Sign up, log in, and log out with secure user authentication.

- **Book Borrowing**: Users can browse and borrow books from the library.

- **Borrow Tracking**: Track borrowed books and their due dates.

- **Book Return**: Return borrowed books and manage return dates.

- **Email Notifications**: Receive email notifications whenever you borrow or return a book, keeping you informed about your library activities.

- **User Profiles**: Manage personal details and borrowing history.

- **Admin Dashboard**: Library admins can manage books, users, and borrowings with ease.

## Technologies Used
- **Django**: A powerful Python web framework for building scalable web applications.

- **HTML/CSS**: For styling and layout of the user interface.

- **Bootstrap**: For responsive design to ensure the site is mobile-friendly.

- **SQLite**: A lightweight database used for storing data related to books, users, and borrowings.

- **Django Admin**: For easy management of the system’s content, such as books and user data.

- **Email Services**: Configured to send email notifications when a book is borrowed or returned.

## Installation
### Prerequisites
Before you begin, ensure that you have the following installed on your machine:

- Python 3.8+

- pip (Python package manager)

- Django 3.2+

- SQLite (default)

- A working email service (e.g., Gmail) for sending email notifications.

## Steps to Run the Project Locally
Clone the Repository

```bash
git clone https://github.com/IVON1010/BibliothekHub.git
cd BibliothekHub
```
## Create a Virtual Environment

```bash
python -m venv venv
```
## Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```
On macOS/Linux:

```bash
source venv/bin/activate
```
## Install Dependencies

```bash
pip install -r requirements.txt
```
## Apply Migrations

```bash
python manage.py migrate
```
## Set Up Email Backend

### For email notifications to work, you'll need to configure your email settings in the settings.py file. Example (for Gmail):

- python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
Note: Replace the EMAIL_HOST_USER and EMAIL_HOST_PASSWORD with your actual email credentials. If you're using Gmail, consider creating an App Password for added security.

## Run the Development Server

```bash
python manage.py runserver
```
## Visit the Application

Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

Usage
-**Sign Up / Log In**: To start using BibliothekHub, sign up for an account or log in if you already have one.

- **Browse Books**: Explore the collection of books available in the library.

- **Borrow Books**: Select a book to borrow and follow the borrowing process. You will receive an email confirmation after borrowing.

- **Track Borrowed Books**: Keep track of your borrowed books and their due dates.

- **Return Books**: Return books by their due date and update your records. An email will notify you when you successfully return a book.

## Admin Access
Admins can manage the library by logging into the Django admin dashboard at http://127.0.0.1:8000/admin/ using the superuser credentials.

## Contributing
We welcome contributions to BibliothekHub! To contribute:

- Fork the repository.

- Create a new branch (git checkout -b feature-xyz).

- Make your changes.

- Commit your changes (git commit -am 'Add new feature').

- Push to the branch (git push origin feature-xyz).

- Open a pull request.

## License
This project is licensed under the MIT License.

