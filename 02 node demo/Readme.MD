# Node.js Dockerized App

This is a simple Node.js application Dockerized for easy deployment and testing.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine

## Build and Run

### 1. Clone the Repository
```bash
git clone git clone https://github.com/cloudwithtanvir/Guide-to-Containers-with-Docker.git
cd Guide to Containers with Docker\02 node demo
```

### 2. Build the Docker Image
```bash
docker build -t node-docker-app .
```

This command builds a Docker image named `node-docker-app` based on the `Dockerfile` in the current directory (`.`).

### 3. Run the Docker Container
```bash
docker run -p 3000:3000 node-docker-app
```

This command runs a new Docker container based on the `node-docker-app` image, mapping port 3000 from the container to port 3000 on your local machine.

### 4. Access the Application
Open your web browser and visit `http://localhost:3000`. You should see the message "Hello from Dockerized Node.js App!".

## Customization

- **Application Code**: Modify the `index.js` file to customize the behavior of your Node.js application.
- **Dependencies**: Update the `package.json` file with any additional dependencies your application requires.

## Additional Commands

- **Stop the Docker Container**: Press `Ctrl + C` in the terminal where the container is running.
- **List Running Containers**:
  ```bash
  docker ps
  ```
- **Stop a Running Container** (if needed):
  ```bash
  docker stop <container_id>
  ```

## Troubleshooting

- If you encounter any issues during the build or run process, refer to the [Docker documentation](https://docs.docker.com/) for troubleshooting tips.
- Feel free to open an issue in this repository if you have specific problems related to this application.
