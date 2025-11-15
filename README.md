# Service Mapper Visualizer

A dynamic web application for visualizing services and their connections. Built with Django REST Framework backend and vanilla JavaScript frontend.

## Features

- 🎨 **Visual Service Mapping**: Display services as interactive nodes on a canvas
- 🔗 **Connection Visualization**: Show connections between services with green colored lines
- 🖱️ **Interactive Nodes**: Click on any service to open its URL in a new tab
- 🎯 **Drag & Drop**: Reposition services by dragging them around the canvas
- 🔄 **Dynamic Updates**: Add services and connections in real-time via REST API
- 📡 **REST API**: Full CRUD operations for services and connections

## Screenshots

### Initial Interface
![Initial Page](https://github.com/user-attachments/assets/13b31139-937d-44f9-9c75-02fcbb08f120)

### With Services and Connections
![Services with Connections](https://github.com/user-attachments/assets/7cb59fe2-1516-4288-88b9-eb3341af2840)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/PsymoNiko/service-mapper-visualizer.git
cd service-mapper-visualizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run database migrations:
```bash
python manage.py migrate
```

4. (Optional) Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to:
```
http://localhost:8000/
```

## Usage

### Web Interface

#### Adding Services
1. Enter the service name (e.g., "jira", "gitlab", "website")
2. Enter the service URL (e.g., "https://jira.com")
3. Click "Add Service"
4. The service will appear as a node on the canvas

#### Adding Connections
1. Select a source service from the dropdown
2. Select a target service from the dropdown
3. Click "Add Connection"
4. A green line with an arrow will appear showing the connection

#### Interacting with Services
- **Click** on a service node to open its URL in a new tab
- **Drag** a service node to reposition it on the canvas
- Service positions are automatically saved

### REST API

The application provides a RESTful API for programmatic access:

#### Services API

**List all services:**
```bash
GET /api/services/
```

**Create a service:**
```bash
POST /api/services/
Content-Type: application/json

{
    "name": "jira",
    "url": "https://jira.com",
    "x_position": 100,
    "y_position": 100
}
```

**Get a specific service:**
```bash
GET /api/services/{id}/
```

**Update a service:**
```bash
PATCH /api/services/{id}/
Content-Type: application/json

{
    "url": "https://new-jira-url.com"
}
```

**Delete a service:**
```bash
DELETE /api/services/{id}/
```

#### Connections API

**List all connections:**
```bash
GET /api/connections/
```

**Create a connection:**
```bash
POST /api/connections/
Content-Type: application/json

{
    "source": 1,
    "target": 2
}
```

**Get a specific connection:**
```bash
GET /api/connections/{id}/
```

**Delete a connection:**
```bash
DELETE /api/connections/{id}/
```

### API Examples with curl

```bash
# Add a new service
curl -X POST http://localhost:8000/api/services/ \
  -H "Content-Type: application/json" \
  -d '{"name": "jenkins", "url": "https://jenkins.io", "x_position": 200, "y_position": 300}'

# List all services
curl http://localhost:8000/api/services/

# Create a connection
curl -X POST http://localhost:8000/api/connections/ \
  -H "Content-Type: application/json" \
  -d '{"source": 1, "target": 2}'

# List all connections
curl http://localhost:8000/api/connections/
```

## Project Structure

```
service-mapper-visualizer/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── service_mapper/          # Django project settings
│   ├── settings.py          # Main settings
│   ├── urls.py              # URL routing
│   └── ...
├── services/                # Django app for services
│   ├── models.py            # Data models (Service, Connection)
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API views
│   ├── admin.py             # Django admin configuration
│   └── ...
└── templates/               # HTML templates
    └── index.html           # Main visualization page
```

## Technology Stack

- **Backend**: Django 5.x, Django REST Framework
- **Frontend**: HTML5 Canvas, Vanilla JavaScript, CSS3
- **Database**: SQLite (default, can be changed to PostgreSQL, MySQL, etc.)
- **API**: RESTful API with Django REST Framework

## Development

### Running Tests
```bash
python manage.py test
```

### Accessing Admin Panel
1. Create a superuser (if not already done):
```bash
python manage.py createsuperuser
```

2. Navigate to:
```
http://localhost:8000/admin/
```

## Configuration

### Changing Database
Edit `service_mapper/settings.py` and update the `DATABASES` configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Production Deployment
For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use a production-grade database
4. Set up a proper web server (nginx + gunicorn/uwsgi)
5. Configure static files serving
6. Set a secure `SECRET_KEY`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.