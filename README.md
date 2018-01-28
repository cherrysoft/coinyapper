# coinyapper
Quick and dirty coin monitor in Python

# Configuration
The configuration, at present, is simply to manage the display headings for the table.

# The docker version
If you prefer to run the app inside a container just clone the repo, build the container and run the app inside the container (see below).

## Build the container
docker build -t coinyapper .

## Run the app
docker run --rm -ti coinyapper
