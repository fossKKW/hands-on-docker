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

## What are Docker Container?

## What are Images?

## Build your first Image

## Understanding registries and pushing your first image to Dockerhub

## Docker Basics 

### Understanding Docker Containers

### Understanding Docker Images

### What is Docker compose?

---
type: Page
title: Docker Session
description: null
icon: null
createdAt: '2025-01-15T19:19:45.490Z'
creationDate: 2025-01-16 00:49
modificationDate: 2025-01-16 16:31
tags: []
coverImage: null
---

# Understanding image layers

A Docker image is like a blueprint of an application and everything it needs to run. Think of it as a box that holds all the files, settings, libraries, and dependencies that the application needs to work, so it can run consistently on any computer that has Docker installed. Each layer in an image contains a set of filesystem changes - additions, deletions, or modifications.

A docker image is like a blueprint of an application and everything it needs to run. Think of it like a new   TV box, the box contains everything from parts of TV to instructor's manual on how to assemble Tv, likewise an image contains eveything needed to create a container as well as steps on how to make the container. 

Now the real question is how does an image stores this, well image stores everything in layers. Everytime there are changes in file systems, settings or anything that change will be stored as an layer in image. Let's run a container and see what layers were used to run that container : -

```shell
docker pull ubuntu
```

```shell
docker run -it ubuntu
```

```shell
apt-get upgrade && update
apt-get install curl
```

after the "curl" package gets installed  :-

```shell
exit
docker ps -a
```

your output will look like this :- 

[Screenshot from 2025-01-16 14-10-09](https://app.capacities.io/c4aeec86-9b73-4a6a-957d-a01eb5abc119/ac850266-5cde-42a7-a595-980d5ea6b424)

copy the container id 

```shell
docker commit <container id> <new image name>
```

```shell
docker image ls
docker history <new image name>
```

[Screenshot from 2025-01-16 14-15-11](https://app.capacities.io/c4aeec86-9b73-4a6a-957d-a01eb5abc119/d59c0ea0-3a61-4613-9d19-7fdcd63ba7ea)

The 53.9 mb which is added is due to the "apt-get update && upgrade" and the "apt-get install curl" commands, because those made changes to various files and also downlaoded some files as a result a new image layer got created for that.

# Sequence of Layers in image

Now one thing to realise is that the chronology in which the image layers should be created such that the every layer to be created has its dependecy in one of the previous layers. e.g. in order to run a python application we should obviously have python in our container and in order to run python we should have base such as ubuntu or alpine. 

# Let's create an Image of your app

First let's see how our Image layers would look like :- 



[container_image_layers](https://app.capacities.io/c4aeec86-9b73-4a6a-957d-a01eb5abc119/3564521a-92d3-43ee-a971-0c763771e85c)

This is beneficial because it allows layers to be reused between images. For example, imagine you wanted to create another Python application. Due to layering, you can leverage the same Python base.

[container_image_layer_reuse](https://app.capacities.io/c4aeec86-9b73-4a6a-957d-a01eb5abc119/e1112121-0f65-4c8b-ba39-b3a11d760e3f)

Now let's create a simple python script/app image, execute the following commands step by step :- 

```shell
docker run -it ubuntu
apt-get update && upgrade
apt-get install -y python3
#now let's create our python script/app
echo 'print(f"Hello from app")' > app.py
exit
```

Now let's create the image of our app : - 

```shell
sudo docker ps -a
#copy the container id or learn the contianer name 
sudo docker commit -m "ADD python application" <container id or container name> <new image name>
```

The above command will create a image of our application and store it. The image will also have a layer which will have our python app, to see which layer has our python app :-

```shell
docker history <your image name>
```

Now lets create and run a container from our app image :- 

```shell
docker run -it <your image name>
$python3 -m <app name>
```

TADA.....! We just ran a container from our customised image.

# What is a Dockerfile ? 

A Dockerfile is a text-based document that's used to create a container image. It provides instructions to the image builder on the commands to run, files to copy, startup command, and more.

Let's create a dockerfile for our python  application, but before we write our dockerfile there are some steps we need to follow first :- 

1. create a folder named app

2. create a file name app.py in app folder

3. copy the following text into that app.py file "print(f"Hello from app")"

4. create a file named "Dockerfile" in to the app folder



Now let's create our Dockerfile 

```dockerfile
FROM python:3.12

WORKDIR /python-app

COPY . .

CMD ["python3", "-m", "app"]
```

now let's understand our Dockerfile step-by-step : -

- `FROM <image>` - this specifies the base image that the build will extend.

- `WORKDIR <path>` - this instruction specifies the "working directory" or the path in the image where files will be copied and commands will be executed.

- `COPY <host-path> <image-path>` - this instruction tells the builder to copy files from the host and put them into the container image.

- `RUN <command>` - this instruction tells the builder to run the specified command.

Now that we have understood how to create images let's understand how to upload those images to registries.

The Tagging and pushing/publishing of images follows a convetion to name them, before we push our first image to repository, first create an account on docker hub using your email address, then verify the email address otherwise we won't be able to create a repository.

Now the dockerhub follows a naming convention for docker images , the format is as follows:- 

```shell
docker tag <local-image>:<tag> <dockerhub-username>/<repository-name>:<tag>
```

e.g. if you have an image name app-image you can tag it as follows :-

docker tag app-image:latest <you dockerhub user>/<your dockerhub repository name>:<tag>

if you didn't tagged your image docker by-defualt tags your image as latest.

since we have tagged our image let's push the image to dockerhub, but before that first we need to login to our account from teminal for that :-

```shell
docker login
```

after logging in let's push the image:- 

```shell
docker push <your-dockerhub-username>/<your-dockerhub-repository-name>:<your-image-tag>
```

### Multi-stage builds

### Build cache

## Learning more about Containers

### Know more about ports

### Container defaults

### Share data with container

### Multi-container applications