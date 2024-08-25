# Irene

Irene is an intelligent AI assistant designed to enhance your daily life. Whether you're managing your smart home, organizing your schedule, or simply looking for a more intuitive way to interact with technology, Irene is here to help.

## Prerequisites

- Python 3.7+
- `virtualenv` (optional but recommended)

## Setup and Installation

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

### 4. Run the Application

You can start the FastAPI server by running the following command:

```bash
uvicorn app.main:app --reload
```

This will start the server on `http://127.0.0.1:8000`. The `--reload` flag is useful during development as it automatically reloads the server when code changes are detected.

### 5. Access the API Documentation

The API documentation that can be accessed in your browser:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **Redoc**: `http://127.0.0.1:8000/redoc`

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
