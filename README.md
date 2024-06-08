# Bookstore Website

This is a fully functional bookstore website built using Django. Users can browse and buy books of their choice using the PayPal payment gateway integrated for transactions. The website is deployed on PythonAnywhere.com and uses a MySQL database to store transaction details, user information, and book data.

## Tech Stack

- **Django**: Python-based web framework for building web applications.
- **MySQL**: Relational database management system used for data storage.
- **PayPal API**: API integration for handling payments securely.
- **HTML, CSS**: Front-end components for user interaction and styling.

## Features

- **User Authentication**: Allows users to log in and register.
- **Book Listing**: Displays a list of available books for purchase.
- **Payment Gateway Integration**: Integrates PayPal for seamless payment processing.
- **Database**: Stores book, user and transaction details in MySQL for record-keeping.
- **Django ORM**: Utilizes Django's ORM to interact with the MySQL database.
- **Secure Payments**: Implements secure payment handling using PayPal's APIs.
- **User-Friendly Interface**: Provides a simple interface for users to initiate and complete payments.

## Usage

1. Login to the site or Sign up if you are a new user.
2. Choose the book of your choice from the book listing page.
3. Click on the "Buy Now" button next to the desired book.
4. Follow the PayPal payment flow to complete the transaction (Please use a Sandbox account because this website is for demonstration only).
5. A confirmation message will be shown upon successful payment.

## Screenshots

Home Page :

![App Screenshot](https://i.ibb.co/NZ5TDwK/home.png)

Book description :

![App Screenshot](https://i.ibb.co/zZxbz52/desc.png)

Payment option :

![App Screenshot](https://i.ibb.co/Y0Gw3YX/payp.png)

Paypal payment initiation and completion :

![App Screenshot](https://i.ibb.co/yXs11kr/tsn.png)

![App Screenshot](https://i.ibb.co/Np9FRBJ/completed.png)

All details are stored in the MySQL database :

![App Screenshot](https://i.ibb.co/FnTvJTV/sql.png)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- MySQL
- PayPal Sandbox Account
