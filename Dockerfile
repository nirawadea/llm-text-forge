## use the official python 3.9 image
FROM python:3.9

## set the working directory to /code
WORKDIR /code

## copy the current directory contents in the container at /code
COPY ./requrements.txt /code/requirements.txt