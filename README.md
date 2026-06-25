# AWS Service Management Dashboard

## Project Overview

The AWS Service Management Dashboard is a Dockerized two-tier web application built using **Flask** and **MySQL**. It allows users to add and manage AWS service information through a simple web interface. The application is containerized using Docker, orchestrated with Docker Compose, and the Docker image is analyzed using Docker Scout.

---

## Features

* Add AWS service details
* Store AWS service information in MySQL
* Display all stored AWS services
* Automatic database creation
* Automatic table creation
* Dockerized Flask application
* MySQL database container
* Docker Compose orchestration
* Persistent storage using Docker Volumes
* Container communication using Docker Networks
* Docker Scout image vulnerability scanning

---

##  Tech Stack

* Python
* Flask
* MySQL
* Docker
* Docker Compose
* Docker Scout
* HTML

---

## Project Structure

```
AWS-Service-Management-Dashboard/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Anushka-codes438/AWS-Service-Management-Dashboard.git
```

### Move into the project

```bash
cd AWS-Service-Management-Dashboard
```

### Build and start the application

```bash
docker compose up -d --build
```

---

##  Access the Application

Open your browser:

```
http://localhost:5000
```

---

## Dashboard Features

Users can:

* Add AWS Service Name
* Select AWS Service Type
* Enter AWS Region
* Select Service Status
* View all stored AWS services in a table

---

## Database

Database:

```
flaskdb
```

Table:

```
aws_services
```

Columns:

* id
* service_name
* service_type
* region
* status

---

## Docker Features

* Dockerfile
* Docker Image
* Docker Container
* Docker Volume
* Docker Network
* Docker Compose
* Docker Scout Security Scan

---

## Future Enhancements

* Update AWS services
* Delete AWS services
* Search and filter services
* User authentication
* Deploy on AWS EC2
* CI/CD pipeline using GitHub Actions or Jenkins

---

## 👩‍💻 Author

**Anushka Gupta**

Aspiring Cloud & DevOps Engineer
