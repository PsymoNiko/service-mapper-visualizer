# Service Mapper Visualizer

A dynamic web application for visualizing server infrastructure, service stacks, and container deployments. Built with Django REST Framework backend and vanilla JavaScript frontend.

## Features

### Hierarchical Infrastructure Visualization

- 🖥️ **Server Mapping (Level 0)**: Visualize servers with IP addresses and directional connectivity
- 📦 **Service Stacks (Level 1)**: View docker-compose based application stacks on each server
- 🐳 **Container Services (Level 2)**: Explore individual containers organized by Docker networks
- 🔗 **Connection Health**: Color-coded arrows (green for healthy, red for unhealthy connections)
- 🎯 **Interactive Navigation**: Click-based drill-down through infrastructure levels
- 🧭 **Breadcrumb Navigation**: Easy navigation between levels (Servers > server-01 > Chat Application)

### Docker Compose Integration

- 📄 **YAML Parsing**: Upload and parse docker-compose.yml files
- 🔍 **Service Extraction**: Automatically extract services, ports, networks, volumes, and dependencies
- 🏗️ **Stack Management**: Organize services as logical application stacks
- 📊 **Network Visualization**: Group and display services by their Docker networks

### Legacy Features

- 🎨 **Visual Service Mapping**: Display services as interactive nodes on a canvas
- 🔗 **Connection Visualization**: Show connections between services with green colored lines
- 🖱️ **Interactive Nodes**: Click on any service to open its URL in a new tab
- 🎯 **Drag & Drop**: Reposition servers by dragging them around the canvas
- 🔄 **Dynamic Updates**: Add servers, stacks, and connections in real-time via REST API
- 📡 **REST API**: Full CRUD operations for all resources

## Screenshots

### Level 0 - Server Infrastructure View
![Server Infrastructure](https://github.com/user-attachments/assets/ab0693b7-4e0e-4972-a6ed-ba1d0f619c53)

Shows servers with directional connectivity. Green arrows indicate healthy connections. Click on a server to drill down to its service stacks.

### Level 1 - Service Stacks View
![Service Stacks](https://github.com/user-attachments/assets/edde025b-2e04-46a4-b45c-30246d39b806)

Displays docker-compose based application stacks running on a server. Upload docker-compose.yml files to populate services. Click on a stack to view its containers.

### Level 2 - Container Services View
![Container Services](https://github.com/user-attachments/assets/8ad2a03a-944e-4932-bdd6-903a78ab292e)

Shows individual container services organized by Docker network, with detailed information including images, ports, and dependencies.

### Legacy Interface
![Initial Page](https://github.com/user-attachments/assets/13b31139-937d-44f9-9c75-02fcbb08f120)

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
http://localhost:8000/        # Legacy service visualization
http://localhost:8000/servers/ # New hierarchical server infrastructure view
```

## Usage

### Hierarchical Server Infrastructure View

Access the new hierarchical visualization at `http://localhost:8000/servers/`

#### Level 0 - Managing Servers

**Adding Servers:**
1. Enter server name (e.g., "prod-server-01")
2. Enter IP address (e.g., "192.168.1.10")
3. Enter description (e.g., "Production web server")
4. Click "Add Server"

**Adding Server Connections:**
1. Select source server from dropdown
2. Select target server from dropdown
3. Check "Healthy (Green)" for reachable connections (uncheck for unhealthy/red)
4. Click "Add Connection"

**Navigation:**
- Click on a server to view its service stacks (Level 1)
- Drag servers to reposition them on the canvas

#### Level 1 - Managing Service Stacks

**Adding Service Stacks:**
1. Click on a server to navigate to Level 1
2. Enter stack name (e.g., "Chat Application")
3. Enter URL (e.g., "https://chat.example.com")
4. Click "Add Stack"

**Uploading Docker Compose:**
1. Select a stack from the dropdown
2. Paste your docker-compose.yml content in the textarea
3. Click "Parse & Load Services"

The system will automatically extract and create container services from the docker-compose file.

**Navigation:**
- Click on a stack to view its container services (Level 2)
- Use breadcrumb to navigate back to servers

#### Level 2 - Viewing Container Services

Container services are automatically organized by their Docker networks. You can view:
- Service name and image
- Exposed ports
- Network membership
- Dependencies

Use breadcrumb navigation to return to previous levels.

### Legacy Web Interface

Access the original service visualization at `http://localhost:8000/`

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
- **Click** on a service node to highlight it and recursively show connected services (use controls to pick direction/depth); **double-click** to open its URL in a new tab
- **Drag** a service node to reposition it on the canvas
- Service positions are automatically saved

### REST API

The application provides a comprehensive RESTful API for programmatic access:

#### Servers API

**List all servers:**
```bash
GET /api/servers/
```

**Create a server:**
```bash
POST /api/servers/
Content-Type: application/json

{
    "name": "prod-server-01",
    "ip_address": "192.168.1.10",
    "description": "Production web server",
    "x_position": 200,
    "y_position": 200
}
```

**Get a specific server:**
```bash
GET /api/servers/{id}/
```

**Update a server:**
```bash
PATCH /api/servers/{id}/
Content-Type: application/json

{
    "description": "Updated description"
}
```

**Get stacks for a server:**
```bash
GET /api/servers/{id}/stacks/
```

**Delete a server:**
```bash
DELETE /api/servers/{id}/
```

#### Server Connections API

**List all server connections:**
```bash
GET /api/server-connections/
```

**Create a connection:**
```bash
POST /api/server-connections/
Content-Type: application/json

{
    "source": 1,
    "target": 2,
    "is_healthy": true
}
```

**Delete a connection:**
```bash
DELETE /api/server-connections/{id}/
```

#### Service Stacks API

**List all stacks:**
```bash
GET /api/stacks/
```

**Filter stacks by server:**
```bash
GET /api/stacks/?server=1
```

**Create a stack:**
```bash
POST /api/stacks/
Content-Type: application/json

{
    "server": 1,
    "name": "Chat Application",
    "url": "https://chat.example.com",
    "description": "Django chat application"
}
```

**Parse docker-compose.yml:**
```bash
POST /api/stacks/{id}/parse_compose/
Content-Type: application/json

{
    "docker_compose_content": "services:\n  nginx:\n    image: nginx:latest\n..."
}
```

**Get stack details (includes container services):**
```bash
GET /api/stacks/{id}/
```

**Delete a stack:**
```bash
DELETE /api/stacks/{id}/
```

#### Container Services API

**List all container services:**
```bash
GET /api/container-services/
```

**Get a specific container service:**
```bash
GET /api/container-services/{id}/
```

#### Legacy Services API

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

#### Legacy Connections API

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

#### Server Infrastructure Examples

```bash
# Create a server
curl -X POST http://localhost:8000/api/servers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "prod-server-01", "ip_address": "192.168.1.10", "description": "Production web server", "x_position": 200, "y_position": 200}'

# List all servers
curl http://localhost:8000/api/servers/

# Create a server connection (healthy)
curl -X POST http://localhost:8000/api/server-connections/ \
  -H "Content-Type: application/json" \
  -d '{"source": 1, "target": 2, "is_healthy": true}'

# Create a service stack
curl -X POST http://localhost:8000/api/stacks/ \
  -H "Content-Type: application/json" \
  -d '{"server": 1, "name": "Chat Application", "url": "https://chat.example.com"}'

# Parse docker-compose file
curl -X POST http://localhost:8000/api/stacks/1/parse_compose/ \
  -H "Content-Type: application/json" \
  -d '{"docker_compose_content": "services:\n  nginx:\n    image: nginx:latest\n    ports:\n      - \"80:80\"\n    networks:\n      - web\nnetworks:\n  web:"}'

# Get stack with container services
curl http://localhost:8000/api/stacks/1/
```

#### Legacy Service Examples

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
│   ├── models.py            # Data models (Server, ServerConnection, ServiceStack, ContainerService, Service, Connection)
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API views
│   ├── admin.py             # Django admin configuration
│   └── ...
└── templates/               # HTML templates
    ├── index.html           # Legacy service visualization
    └── server_map.html      # Hierarchical server infrastructure visualization
```

## Technology Stack

- **Backend**: Django 4.2.x, Django REST Framework 3.14+
- **Frontend**: HTML5 Canvas, Vanilla JavaScript, CSS3
- **Database**: SQLite (default, can be changed to PostgreSQL, MySQL, etc.)
- **API**: RESTful API with Django REST Framework
- **YAML Parser**: PyYAML for docker-compose parsing

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