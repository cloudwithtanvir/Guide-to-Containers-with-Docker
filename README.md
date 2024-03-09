# Dockerized Python Flask App
This repository contains a simple Python Flask application Dockerized for easy deployment and testing.This project was created for the DevOps bootcamp class taken by Tanvir Ahmed.

## Prerequisites
Docker installed on your local machine. If you don't have Docker installed, follow the official installation guide.
Getting Started
These instructions will help you run the Dockerized Flask app on your local machine.

### Building the Docker Image

Clone this repository to your local machine:

``` git clone https://github.com/cloudwithtanvir/Guide-to-Containers-with-Docker.git ``` .

``` cd Guide to Containers with Docker ```

### Build the Docker image:


``` docker build -t my-python-app . ```

### Running the Docker Container

After building the image, you can run the Docker container:

```docker run -p 4000:80 my-python-app ```

The app will be accessible at http://localhost:4000.

### Stopping the Container
To stop the running container, use Ctrl + C in your terminal.


## Contributing
If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.