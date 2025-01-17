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

### Understanding image layers

A docker image is like a blueprint of an application and everything it needs to run. Think of it like a new   TV box, the box contains everything from parts of TV to instructor's manual on how to assemble Tv, likewise an image contains eveything needed to create a container as well as steps on how to make the container. 

Now the real question is how does an image stores this, well image stores everything in layers. Everytime there are changes in file systems, settings or anything that change will be stored as an layer in image. Let's run a container and see what layers were used to run that container : -

First we will pull the official ubuntu image from dockerhub :- 

```shell
docker pull ubuntu
```

now we will run that image :- 

```shell
docker run -it ubuntu
```

exit from the container using  :- 

```shell
exit
docker ps -a
```

![Screenshot from 2025-01-17 19-39-04](/app/static/1.png?raw=true)

now let's see the layers in that image :- 

```shell
docker history ubuntu
```

![Screenshot from 2025-01-17 19-36-38](/app/static/2.png?raw=true)

The layer with 78.1 mb size stores the ubuntu image, rest of the layers are created by docker to run container and define environment variables. 

Now that we have seen what image layers looks like let's create our customized image :- 

First run 

```shell
docker run -it ubuntu
```

After the container is running type :- 

```shell
apt-get upgrade && update
apt-get install curl
```

after the "curl" package gets installed  type :-

```shell
exit
docker ps -a
```

the output will look like this :- 
![docker ps -a](/app/static/3.png?raw=true)
now copy the container id of recently runned image and execute this command to create a new image:-  

```shell
docker commit <container id> <new image name>
```

```shell
docker history <new image name>
```

![Screenshot from 2025-01-17 19-40-24](/app/static/4.png?raw=true)

The 53.9 mb which is added is due to the "apt-get update && upgrade" and the "apt-get install curl" commands, because those made changes to various files and also downloaded some files as a result a new image layer got created for that.

# Sequence of Layers in image

Now one thing to realise is that the chronology in which the image layers should be created such that the every layer to be created has its dependecy stored in one of the previous layers. e.g. in order to run a python application we should obviously have python in our container and in order to run python we should have python compiler and the list goes on. 

# Let's create an Image of your app

First let's see how our Image layers would look like :- 

![image](/app/static/5.png?raw=true)

This is beneficial because it allows layers to be reused between images. For example, imagine you wanted to create another Python application. Due to layering, you can leverage the same Python base.

![image](/app/static/6.png?raw=true)

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

3. copy the following code into that app.py file 

    ```python
    print(f"Hello from app")
    ```

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

Let's create an image using the docker file, in the terminal run the following command :- 

```shell
docker build -t <your-new-image-name> .
```

Your output should look like this:- 

![Screenshot from 2025-01-17 20-45-23](/app/static/7.png?raw=true)

***Note:- Notice the time it took to build our image. You can see the building time in terminal near the "Building" keyword.***

Now that our image has been created let's tag and publish that image.

The Tagging and pushing/publishing of images follows a convention to name them, before we push our first image to repository, first create an account on docker hub using your email address, then verify the email address otherwise we won't be able to create a repository.

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

# Understanding build cache

To understand what a build cache is, let's create an image from the same Dockerfile from which we created the previous image. 

```shell
docker build -t <new-image-name>:<v2> .
```

Notice the time it took docker to build the image :- 

![Screenshot from 2025-01-17 20-46-17](/app/static/8.png?raw=true)

The time got largely reduced. How did that happen ? 

Well docker stores the layers in cache for future use, whenever we tell docker to create a new image it first checks if the cache has any required layers stored in it so that the build time gets reduced. 

# Multi-stage Builds

One thing you may have noticed is that the size of docker images or containers gets very big as a result it occupies very large space. The dockerfile that builds such image isn't optimized. In order to optimize dockerfile we create the dockerfile in multiple stages. What does this mean ? 

Let's say you want to containerize an application which is written in a compiled language e.g. go.So when you write a go application and run it what happens, the compiler of GO compiles your programme into a native machine binary code (differs based on architecture).This binary can be executed directly without needing an external interpreter or runtime environment. 

 So in multi-stage build what we do is, compile our app/programm in one stage and copy that compiled programm in final stage. This final stage includes only the necessary files as a result the image size gets drastically reduced. 

```dockerfile
FROM golang:1.20 AS builder

WORKDIR /app

COPY . .

RUN go mod tidy
RUN go build -o app .

FROM alpine:latest

RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /app/app .

EXPOSE 8080

CMD ["./app"]
```

Each "FROM" word in Dockerfile signifies a stage, everything that follows the "FROM" belongs to that stage until the next "FROM" word. In the above example we use the golang:1.20 as our base image. Then we create a working directory and copy all of the contents of directory in which dockerfile is present. The "RUN go mod tidy"  and "RUN go build -o app ." checks for dependencies if not present then it imports them and compiles a binary of your go app respectively. After the binary gets created, we create a second and final stage of dockerfile which uses apline image as the base image. Then we create a working directory and gets necessary certificates downloaded, then compiled app is copied from builder stage to working directory. And the rest of the part has already been explained.

## Learning more about Containers

### Know more about ports

### Container defaults

### Share data with container

### Multi-container applications