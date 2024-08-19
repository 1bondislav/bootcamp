#!binbash

# Check if Docker is installed
if ! command -v docker & devnull
then
    echo Docker not found. Installing Docker...
    # Install Docker (specific commands might differ based on OS)
    sudo apt-get update
    sudo apt-get install -y docker.io
fi

# Build the Docker image
docker build -t flask-snowflake-app .

# Run the Docker container
docker run -d -p 50005000 flask-snowflake-app

# Verify the container is running
if [ $(docker ps -q -f name=flask-snowflake-app) ]; then
    echo Container is running and accessible on port 5000.
else
    echo Container failed to start.
fi
