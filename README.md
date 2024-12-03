# Newspaper Agency Project

This project is a web application for managing a newspaper agency. It allows users to create, update, and delete newspapers, topics, and redactors. The application is built using Django and includes features such as search functionality, user authentication, and form handling with crispy forms.

## Project Structure
![Structure](Structure.webp)

## Installation

Python must be already installed

```shell
git clone https://github.com/dxrrkwm/newspaper-agency.git
cd newspaper-agency
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Features

* Newspaper Management: Create, update, delete, and view newspapers.
* Topic Management: Create, update, delete, and view topics.
* Redactor Management: Create, update, delete, and view redactors.
* Search Functionality: Search for newspapers, topics, and redactors.
* User Authentication: Register, login, and logout functionality.
* Form Handling: Use of crispy forms for better form rendering.