# Sample Python Code Executer in Docker

This project contains a simple Python script that generates a CSV file with sample data. The script can be run inside a Docker container.

## Prerequisites

- Docker installed on your system.

## Files

- `script.py`: The Python script that generates the CSV file.
- `Dockerfile`: The Dockerfile used to create the Docker image.

## Instructions

### 1. Clone the repository or download the files

Ensure you have `script.py` and `Dockerfile` in the same directory.

### 2. Build the Docker image

Open a terminal and navigate to the directory containing `script.py` and `Dockerfile`. Run the following command to build the Docker image:

```
docker build -t sample-csv .
```

### 3. Run the Docker container

Run the following command to create and run a Docker container from the image you just built:

```
docker run --rm -v "$(pwd)":/app sample-csv
```

This command does the following:

- `--rm`: Automatically remove the container when it exits.
- `-v "$(pwd)":/app`: Mounts the current directory to the /app directory in the container. This ensures that the generated sample_data.csv file is available in your local directory.