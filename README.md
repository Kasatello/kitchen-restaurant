# Restaurant Website

This is a web application for managing a restaurant, including creating and updating dishes, managing cooks, and more.

## Check it out

[Restaurant project deployed to Render](https://restaurant-mate-zb80.onrender.com/)

U can use this login credentials:
```shell
admin: kasatello
password: admin12341
```

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Restaurant Website is a Django-based web application that allows restaurant owners and staff to manage their menu, cooks, and dish types. It provides a user-friendly interface for creating, updating, and deleting dishes, as well as managing cook details.

## Features

- User authentication and authorization: Different user roles have different access levels for various functionalities.
- Create, update, and delete dishes: Authorized users can manage the restaurant's menu by adding new dishes or updating existing ones.
- Manage cooks: Users can add and edit cook details, including their names and specialties.
- Dish types: Users can create different types of dishes to categorize the menu items.

## Technologies Used

- Python
- Django
- Django Bootstrap5
- HTML
- CSS
- JavaScript
- SQLite (or other database of your choice)

## Setup

1. Install Python on your system.
2. Clone this repository to your local machine.
3. Create a virtual environment and activate it.
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Apply migrations to create the database tables: `python manage.py migrate`.
6. Create a superuser account: `python manage.py createsuperuser`.
7. Run the development server: `python manage.py runserver`.

## Usage

1. Access the web application by navigating to `http://localhost:8000` in your web browser.
2. Login using the superuser credentials you created during setup.
3. Use the sidebar navigation to access different functionalities, such as creating new dishes or managing cooks.
4. Logout when you are done using the web application.

## Contributing

Contributions are welcome! If you find any bugs or want to suggest enhancements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as per the terms of the license.
