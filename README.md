# Web Application

A modern full-stack e-commerce application built with React and Django. This project provides a complete online shopping experience with user authentication, product management, shopping cart functionality, and order processing.

##  Features

- ### User Authentication & Authorization
  - User registration and login
  - JWT-based authentication
  - Secure password validation
<img width="663" height="351" alt="Picture1" src="https://github.com/user-attachments/assets/b0d740f5-43ce-4461-829c-f8b1c2bee086" />


- ### Product Management ###
  - Browse products with pagination
  - Detailed product views with images
  - Product search and filtering
<img width="663" height="351" alt="landing" src="https://github.com/user-attachments/assets/fdb13b21-0759-4d23-a3b1-6d1b7f3ea480" />

- ### Shopping Cart ###
  - Add/remove items from cart
  - Persistent cart across sessions
  - Real-time cart updates
<img width="663" height="351" alt="cart" src="https://github.com/user-attachments/assets/4baf066b-a947-41bd-ae64-0b2d358369ad" />


- ### Order Management ###
  - Create orders from cart items
  - Order history tracking
  - Order status updates (Ordered, In delivery, Delivered)
<img width="663" height="351" alt="comenzi" src="https://github.com/user-attachments/assets/b28a56ea-891f-408b-975d-cd6c2677ed49" />

- ### User Profile ###
  - User account management
  - Order history viewing
  - Profile customization
  <img width="663" height="351" alt="profile" src="https://github.com/user-attachments/assets/c3c7510a-1aa6-48b2-930f-99a9c921d40a" />


## Architecture

This project follows a modern full-stack architecture:

### Frontend (`/online_store/`)
- **Framework**: React with Vite
- **UI Library**: Chakra UI for modern components
- **State Management**: React Query for server state management
- **Routing**: React Router v6 for client-side routing
- **HTTP Client**: Axios for API communication
- **Authentication**: JWT token-based authentication

### Backend (`/djangoProject/`)
- **Framework**: Django 4.2 with Django REST Framework
- **Database**: MySQL
- **Authentication**: JWT tokens 
- **API**: RESTful API design with ViewSets
- **File Storage**: Local media file handling
- **CORS**: Configured for cross-origin requests

##  Quick Start

### Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.10)
- **MySQL** database
- **pipenv** for Python dependency management

### Backend Setup

1. **Navigate to the Django project**:
   ```bash
   cd djangoProject
   ```

2. **Install Python dependencies**:
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Configure environment variables**:
   Create a `.env` file in the `djangoProject` directory:
   ```env
   DATABASE_NAME=online_store
   DATABASE_USER=root
   DATABASE_PASSWORD=your_password
   DATABASE_HOST=localhost
   DATABASE_PORT=3306
   ```

4. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

The backend API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. **Navigate to the React project**:
   ```bash
   cd online_store
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```

The frontend application will be available at `http://localhost:5173`

## 📁 Project Structure

```
licenta/
├── online_store/                 # React Frontend
│   ├── src/
│   │   ├── api/                 # API configuration
│   │   ├── pages/               # Page components
│   │   │   ├── Landing/         # Home page with product list
│   │   │   ├── Login/           # User login
│   │   │   ├── Register/        # User registration
│   │   │   ├── ItemDetails/     # Product details
│   │   │   ├── Cart/            # Shopping cart
│   │   │   ├── Order/           # Order processing
│   │   │   └── Profile/         # User profile
│   │   └── providers/           # React context providers
│   ├── package.json
│   └── vite.config.js
├── djangoProject/               # Django Backend
│   ├── djangoProject/           # Django project settings
│   │   ├── settings.py          # Main configuration
│   │   └── urls.py              # URL routing
│   ├── online_store/            # Django app
│   │   ├── models.py            # Database models
│   │   ├── views.py             # API views
│   │   ├── serializers.py       # Data serialization
│   │   └── urls.py              # API endpoints
│   ├── manage.py
│   └── Pipfile
└── README.md
```

##  API Endpoints

### Authentication
- `POST /api/authorization/register/` - User registration
- `POST /api/authorization/login/` - User login
- `POST /api/authorization/logout/` - User logout

### Products
- `GET /api/items/` - List all products (paginated)
- `GET /api/items/{id}/` - Get product details

### Shopping Cart
- `GET /api/cart/get_cart/` - Get user's cart
- `POST /api/cart/add_item/` - Add item to cart
- `POST /api/cart/remove_item/` - Remove item from cart

### Orders
- `GET /api/orders/user_orders/` - Get user's orders
- `POST /api/orders/create_order/` - Create new order

##  Database Models

### User
- Extended Django's built-in User model
- Email-based authentication

### Item
- Product information (name, description, image, price)
- Image upload support

### Cart
- User-specific shopping cart
- Many-to-many relationship with items

### Order
- Order tracking with status management
- Delivery information (name, address, city, country)
- Date tracking and user association

### Database Diagram
<img width="1543" height="1036" alt="db" src="https://github.com/user-attachments/assets/9bc2177a-a0eb-4da1-b8bb-93b436758891" />



    
