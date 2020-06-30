# Pull official base image
FROM python:3.7-alpine

# set working dir
WORKDIR /usr/src/app

# set environment variables
# console output should not be buffered by docker
# python won't write to .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy files to aid in dependency installation
COPY Pip* /usr/src/app/

# install dependencies
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile


# Copy project
COPY . /usr/src/app/

# expose port to be mapped by the docker daemon
EXPOSE 5000

# Run app
CMD ["flask", "run"]

