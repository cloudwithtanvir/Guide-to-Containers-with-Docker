# Node.js Application with Docker

This is a simple Node.js application that demonstrates Dockerization. It includes basic functions to add and multiply numbers, and uses Express.js to create a simple HTTP server.

## Prerequisites

Before running the application, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (v14 or higher)
- [Docker](https://www.docker.com/)

## Getting Started

Follow these steps to get the application running:

Fork the repository by clicking on the "Fork" button at the top-right corner of this page. This creates a copy of the repository in your GitHub account.

  ```bash
    git clone https://github.com/cloudwithtanvir/Guide-to-Containers-with-Docker.git
    cd Guide to Containers with Docker\04 Docker Registry

   ```

1. Install dependencies:
   ```bash
   npm install
   ```

2. Build the Docker image:
   ```bash
   docker build -t node-docker-app .
   ```

3. Run the Docker container:
   ```bash
   docker run -p 3000:3000 node-docker-app
   ```

4. Access the application in your browser:
   ```
   http://localhost:3000
   ```

## Usage

### Endpoints

- **GET /add/:num1/:num2**
  - Adds two numbers and returns the result.
  - Example: `http://localhost:3000/add/5/3`

- **GET /multiply/:num1/:num2**
  - Multiplies two numbers and returns the result.
  - Example: `http://localhost:3000/multiply/5/3`

### Example Requests

- Addition:
  ```bash
  curl http://localhost:3000/add/5/3
  ```

- Multiplication:
  ```bash
  curl http://localhost:3000/multiply/5/3
  ```

## Folder Structure

```
node-docker-app/
|-- app.js
|-- server.js
|-- package.json
|-- package-lock.json
|-- Dockerfile
|-- README.md
```

- **`app.js`**: Contains basic functions to add and multiply numbers.
- **`server.js`**: Express.js server with routes for addition and multiplication.
- **`package.json`**: Node.js project configuration.
- **`Dockerfile`**: Docker configuration to build the image.
- **`README.md`**: This documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
