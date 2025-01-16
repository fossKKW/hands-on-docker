# hands-on-docker

### Docker Installation

To get started with the hands on tutorial make sure you have git and docker installed on your system  

Install Git: [Download Git](https://git-scm.com/downloads)  

Install docker:
[Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-windows&_gl=1*1uf1m91*_gcl_au*MjA4NTE3MDExNi4xNzM3MDA0NzMz*_ga*MzUwNDMzNjA3LjE3MzcwMDQ3MzQ.*_ga_XJWPQMJYHQ*MTczNzAwNDczNC4xLjEuMTczNzAwNzAwOS4xMS4wLjA.) | [Linux](https://docs.docker.com/desktop/setup/install/linux/) | [MacOS](https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64&_gl=1*1pthec7*_gcl_au*MjA4NTE3MDExNi4xNzM3MDA0NzMz*_ga*MzUwNDMzNjA3LjE3MzcwMDQ3MzQ.*_ga_XJWPQMJYHQ*MTczNzAwNDczNC4xLjEuMTczNzAwNjk2Ni41NC4wLjA.)

- In case you are new to linux follow this step by step [video](https://www.youtube.com/watch?v=J4dZ2jcpiP0) to install docker on your linux system.

---

### What is Docker?  
Docker is a containerization application that helps you ship, test and deploy your application in a isolated environment.

- ***Note**: By isolation we mean that the environment is not affected by external changes in the host. (Don't worry if this does not make sense to you right now, we'll deep dive into each aspect of it later in the tutorial.)*

## Docker usecase

Docker makes development easier by letting developers work in consistent, ready-to-use environments called containers. These containers hold your applications and services and are perfect for CI/CD (Continuous Integration and Continuous Delivery) processes.

## Run your first Container

Open terminal and run the below command  
```
docker run -d -p 8000:80 docker/welcome-to-docker
```

Open [localhost](http://localhost:8000/) to view the frontend of the containerized application.
