# Bit Mobile Store API

Welcome to **Bit Mobile Store**, a robust and modern RESTful API built with **Django Rest Framework (DRF)** for managing a mobile phone store. This project provides a scalable backend for handling products, categories, user authentication, and advanced filtering.

## 🚀 Features

- **CRUD Operations**: Create, read, update, and delete products and categories.
- **User Authentication**: Secure JWT-based authentication with login, logout, and registration endpoints.
- **Permission Control**: Role-based access (e.g., only admins can delete categories, users who created products can edit them).
- **Data Validation**: Robust input validation for data integrity (e.g., positive prices, non-negative stock).
- **Advanced Filtering**: Search, sort, and filter products by category, price, stock, and more.
- **Browsable API**: Interactive API interface for easy testing and exploration.
- **Custom Permissions**: Tailored rules, like allowing only users with created products to edit them.

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- Virtualenv (recommended for isolating dependencies)
- PostgreSQL or SQLite (default database)

## 🛠️ Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/erfunzi/bit-mobile-store.git
    cd bit-mobile-store
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**:
    - Configure your database in `bit_store/settings.py` (default is SQLite).
    - Run migrations to create the database schema:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000`.

## 📡 API Endpoints

The API provides the following endpoints (all prefixed with `/api/`):

| Endpoint            | Method | Description                          | Authentication    |
|---------------------|--------|--------------------------------------|-------------------|
| `register/`         | POST   | Register a new user                  | None              |
| `login/`            | POST   | Log in and obtain JWT tokens         | None              |
| `logout/`           | POST   | Log out (blacklist refresh token)    | JWT Token         |
| `categories/`       | GET    | List all categories                  | JWT Token         |
| `categories/`       | POST   | Create a new category                | JWT Token         |
| `categories/<id>/`  | GET    | Retrieve a category                  | JWT Token         |
| `categories/<id>/`  | PUT    | Update a category                    | Admin Only        |
| `categories/<id>/`  | DELETE | Delete a category                    | Admin Only        |
| `products/`         | GET    | List all products with filters       | JWT Token         |
| `products/`         | POST   | Create a new product                 | JWT Token         |
| `products/<id>/`    | GET    | Retrieve a product                   | JWT Token         |
| `products/<id>/`    | PUT    | Update a product                     | Admin or Creator  |
| `products/<id>/`    | DELETE | Delete a product                     | Admin or Creator  |

### Example Requests

#### Register a User
```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{"username": "newuser", "email": "newuser@example.com", "password": "newpass123", "password2": "newpass123"}'
```

#### Login
```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
-H "Content-Type: application/json" \
-d '{"username": "newuser", "password": "newpass123"}'
```

#### List Products with Filter
```bash
curl -X GET "http://127.0.0.1:8000/api/products/?search=galaxy&min_price=500&ordering=price" \
-H "Authorization: Bearer <your_access_token>"
```

## 🔍 Filtering and Searching

- **Search**: Use `?search=<query>` to search products or categories by name or description.
    - Example: `/api/products/?search=galaxy`
- **Ordering**: Use `?ordering=<field>` to sort results (prefix with `-` for descending).
    - Example: `/api/products/?ordering=-price`
- **Filtering**: Filter products by category, price, stock, or custom ranges.
    - Example: `/api/products/?category=1&min_price=500&max_price=2000`

## 🔐 Authentication

The API uses **JWT (JSON Web Tokens)** for authentication:
- Obtain tokens via `/api/login/` or `/api/register/`.
- Include the Access Token in the `Authorization` header: `Bearer <access_token>`.
- Use `/api/token/refresh/` to refresh an expired Access Token with a Refresh Token.

## 🛡️ Permissions

- **Public Access**: `/api/register/` and `/api/login/` are accessible to everyone.
- **Authenticated Users**: Can list and create products/categories.
- **Admins**: Can update/delete categories and any product.
- **Product Creators**: Can update/delete their own products.

## 📚 Project Structure

```
bit-mobile-store/
├── bit_store/         # Project settings and main configuration
├── store/             # Main app for models, views, and serializers
│   ├── migrations/    # Database migrations
│   ├── models.py      # Product and Category models
│   ├── serializers.py # API serializers
│   ├── views.py       # API views
│   ├── urls.py        # App-specific URLs
│   ├── filters.py     # Custom filter sets
│   └── permissions.py # Custom permissions
├── requirements.txt   # Project dependencies
├── manage.py          # Django management script
└── README.md          # This file
```

## 🧪 Testing

You can test the API using:
- **Browsable API**: Access endpoints like `http://127.0.0.1:8000/api/products/` in a browser.
- **Postman**: Import the API endpoints and test with JWT tokens.
- **cURL**: Use command-line requests as shown in examples.

To create test data:
1. Log in to the Django Admin (`/admin/`) with a superuser account.
2. Add categories (e.g., "Samsung", "Apple") and products (e.g., "Galaxy S23").

## 🚧 Future Improvements

- Add support for product images (file uploads).
- Implement a shopping cart and order management system.
- Add pagination to API responses.
- Integrate email verification for user registration.
- Write unit tests for models, serializers, and views.

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a Pull Request.

## 📧 Contact

For questions or suggestions, reach out to:
- **Email**: [erfzia83@gmail.com](mailto:erfzia83@gmail.com)
- **Telegram**: [@erfun_zi](https://t.me/erfun_zi)

## 📜 License

This project is licensed under the MIT License by **Erfan**. See the [LICENSE](LICENSE) file for details.

---

Happy coding! 🎉
