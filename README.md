# Django project example

A basic Django 3.2 starter project.

## Usage with venv

1. Using Python 3.8, run `python3 -m venv env` to create a virtual environment.
2. Run `pip install -r requirements.txt` to install dependencies.
3. Run `cd app/` to change to `app/`.
4. Run `python3 manage.py runserver` to start development server.
5. Navigate to [http://localhost:8000](http://localhost:8000) to test.

## Usage with Docker

1. Using Docker, run `docker build .` to build the images.
2. Using docker-compose to manage our different services, run `docker-compose build`.
3. Run `docker-compose up` to start development server and services.
4. Navigate to [http://localhost:8000](http://localhost:8000) to test.
5. To run commands inside Docker containers, use the following command: `docker-compose run {django_project_container_name} python manage.py {command}`

## Usage with Kubernetes (Minikube)

1. Download `minikube`, `kubectl` CLI.
2. To start minikube, run `minikube start`.
3. Apply all kubernetes files with `kubectl apply -f server-files/postgres/` and `kubectl apply -f server-files/django/`.
4. In order to delete the previous applied files, run `kubectl delete -f server-files/postgres/` and `kubectl delete -f server-files/django/`.
5. To access to the Django service, run `minikube service django-hello-world`.
6. To check if pods, deployments or services are working correctly, run `kubectl get {pods | deployments | services}`. To check this with an interface, run `minikube dashboard`.

## Google Slides

For more information you could follow [these Google Slides](https://slagomarsino.github.io/django-hello-world/) about some Django basic information.
