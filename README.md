# Irene

Irene is an intelligent AI assistant designed to enhance your daily life. Whether you're managing your smart home, organizing your schedule, or simply looking for a more intuitive way to interact with technology, Irene is here to help.

## Prerequisites

- Python 3.7+
- `virtualenv` (optional but recommended)

## Setup and Installation

This project can be easily set up using Docker. Below are the instructions to build and run the server and other associated services using Docker and Docker Compose.

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

## Testing

To run the tests, use the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
