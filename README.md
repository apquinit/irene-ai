# Irene

Irene is an intelligent AI assistant designed to enhance your daily life. Whether you're managing your smart home, organizing your schedule, or simply looking for a more intuitive way to interact with technology, Irene is here to help.

## Prerequisites

- Python 3.7+
- Docker

## Setup and Installation

To get started with the project, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/apquinit/irene-ai.git
cd irene-ai
```

### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

After activating the virtual environment, install the required packages:

```bash
pip install -r requirements.txt
```

### Building and Running the Containers

To build and run the Docker containers, follow these steps:

1. **Build the Docker Images**

   Navigate to the directory containing your `docker-compose.yml` file and run:

   ```bash
   docker-compose build
   ```

2. **Start the Containers**

   After building, you can start all the containers using:

   ```bash
   docker-compose up
   ```

3. **Stopping the Containers**

   To stop and remove all the running containers, use:

   ```bash
   docker-compose down
   ```

## Environment Variables

The application can use environment variables for configuration. Copy the `.env.example` file to `.env` and update the values as needed.

```bash
cp .env.example .env
```

## Accessing the Services

The services can be accessed using the following URLs:

- **Irene Server`**: 
  - URL: `http://localhost:8000`
  - Description: This is the main API endpoint for the Irene server.

- **Swagger**:
  - URL: `http://localhost:8000/docs`
  - Description: Swagger provides a web-based interface to interact with the Irene API.

- **Redoc**:
  - URL: `http://localhost:8000/redoc`
  - Description: Redoc provides a web-based interface to view the Irene API documentation.

- **Redis Commander**: 
  - URL: `http://localhost:8082`
  - Description: Redis Commander provides a web-based interface to manage and interact with your Redis instance.

- **Mongo Express**: 
  - URL: `http://localhost:8081`
  - Description: Mongo Express offers a web-based interface to view and manage your MongoDB collections and documents.
  - Username: `admin`
  - Password: `admin`

- **Prometheus**: 
  - URL: `http://localhost:9090`
  - Description: Prometheus is used for monitoring and alerting. This URL provides access to the Prometheus web UI for querying metrics and setting up alerts.

- **Grafana**: 
  - URL: `http://localhost:3000`
  - Description: Grafana is a powerful visualization tool. Use this URL to access the Grafana web UI, where you can create dashboards and visualize data collected by Prometheus.
  - Username: `admin`
  - Password: `admin`

## Testing

To run the tests, use the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
