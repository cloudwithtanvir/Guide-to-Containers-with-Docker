# Daily Docker Commands

This document lists commonly used Docker commands for managing containers, images, and volumes in your Docker environment.

## 1. Managing Containers

### List Running Containers
```bash
docker ps
```

### List All Containers (including stopped ones)
```bash
docker ps -a
```

### Start a Container
```bash
docker start <container_id_or_name>
```

### Stop a Running Container
```bash
docker stop <container_id_or_name>
```

### Restart a Container
```bash
docker restart <container_id_or_name>
```

### Remove a Container
```bash
docker rm <container_id_or_name>
```

### Inspect Container Details
```bash
docker inspect <container_id_or_name>
```

### View Logs of a Container
```bash
docker logs <container_id_or_name>
```

## 2. Managing Images

### List Docker Images
```bash
docker images
```

### Pull an Image from Docker Hub
```bash
docker pull <image_name>:<tag>
```

### Remove an Image
```bash
docker rmi <image_id_or_name>
```

### Remove All Unused Images
```bash
docker image prune
```

## 3. Managing Volumes

### List Docker Volumes
```bash
docker volume ls
```

### Create a Volume
```bash
docker volume create <volume_name>
```

### Inspect a Volume
```bash
docker volume inspect <volume_name>
```

### Remove a Volume
```bash
docker volume rm <volume_name>
```

## 4. Container Operations

### Run a Command Inside a Running Container
```bash
docker exec -it <container_id_or_name> <command>
```

### Copy Files Between Host and Container
#### Copy from Host to Container
```bash
docker cp <host_path> <container_id_or_name>:<container_path>
```
#### Copy from Container to Host
```bash
docker cp <container_id_or_name>:<container_path> <host_path>
```

## 5. Docker Compose (for multi-container applications)

### Start Docker Compose Services
```bash
docker-compose up
```

### Start Docker Compose in Detached Mode
```bash
docker-compose up -d
```

### Stop Docker Compose Services
```bash
docker-compose down
```

### List Docker Compose Services
```bash
docker-compose ps
```

## Additional Commands

- **Cleanup Docker Resources** (containers, images, volumes):
  ```bash
  docker system prune
  ```

- **Show Docker System Info**:
  ```bash
  docker system info
  ```

- **Monitor Docker Events**:
  ```bash
  docker events
  ```

## References

- [Docker Documentation](https://docs.docker.com/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)
