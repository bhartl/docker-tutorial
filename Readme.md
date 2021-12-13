# Docker-Tuorial
Here, we mostly follow [*Mosh Hamedani*](codewithmosh.com)'s [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=pTFZFxd4hOI).
Also check out G. Singh's [Blog-Post](https://towardsdatascience.com/docker-made-easy-for-data-scientists-b32efbc23165), or the [docker-curriculum](https://docker-curriculum.com/) by [P. Srivastav](https://prakhar.me/).

## What is Docker?
A platform for **building**, **running** and **shipping** applications. 
If a software is running on your docker-machine, it will also run on others like it.

For many modern software-projects, this is already a large deal. 
Transfering software from a developing machine to a test- or production machine might be cumbersome and often does not work out of the box.
This might be caused by
- one or more missing files
- software version mismatch
- different configurations settings (such as environment variables)
- ...

Here, [Docker](https://www.docker.com/) comes to the rescue:
- With Docker, we can **package-up our application**, with everything it needs, in a Docker **Image**, and **run it everywhere and anywhere** using Docker.
- With Docker, all application-dependencies can automatically be setup on any machine in an **isolated environment**, called a **Container**.
- This allows, for instance, to run different versions of your application in different containers on a single machine or on multiple machines.

So, Docker helps us to **consistently** **build, run** and **ship** our **applications**.

### Basic Terminologies

- **Docker Image**: In very simple terms, a docker image is just like an ISO image file used to install any OS. You can view all (publicly available) docker images on DockerHub
- **Docker Container**: When a Docker Image runs it becomes a Docker Container.
- **Dockerfile**: A Dockerfile contains all the code to set up a docker container, from downloading the docker image, over setting up the environment to running an application.

## Virtual Machines vs Containers

### Virtual Machine
_An abstraction of a machine (or of physical hardware)_

Several virtual machines (VMs) may be run from a single hardware. These VMs are managed by a so-called *hypervisor* (see, e.g., [VirtualBox](https://www.virtualbox.org/) or [VMware](https://www.vmware.com/)).
Software can then be written/installed/... on different VMs on the same physical hardware *in isolation*.

**Problems with VMs**:
- **Each VM** needs a full **operating system** (OS), so a copy of the entire OS.
- Vms are thus **slow to start** (the entire OS needs to be loaded, comparable to starting your computer)
- They are **resource intensive** since they rely on the physical hardware they run on (CPUs, RAM, Storage, ...).

### Container 
_An isolated environment for running applications_

Just like VMs, **containers allow**
- **running multiple apps in isolated environments**
- while being **more lightweight** than VMs.
- All containers running on a system **share** the **same OS as the host** (thus, only a single OS needs to be licensed, hashed and monitored).
- Containers can be **started quickly** (often in less than a second), and they
- need **less hardware resources** compared to VMs (no CPUs or memory needs to be especially assigned to containers).

## Architecture of Docker
Docker uses a **client-server architecture**. 
The client component communicates with the server component using a REST API. 
The server (i.e., the *docker engine*) manages docker-containers. 

Technically, containers are just *processes*, running on a computer.
All containers share the OS of the host, or, more accurately, the host's kernel.
Thus, Linux-containers can be executed on all Linux-kernels (e.g., on a _Linux_ machine, on _Windows>=10_ systems, or on MACs' *Linux VM*).

## Installing Docker 
Install instructions for docker can be found at [docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).
*Note: be sure to check the system prerequisites!*

For *Ubuntu 20.04* users: 
follow the instructions on [docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/).

To **verify** the **installation** of the Docker Engine, run the hello-world image.
```bash
sudo docker run hello-world
```

This command downloads a test image and runs it in a container. 
When the container runs, it prints a message and exits.

## Development Workflow
In short, any project (or application) can be *dockerized* simply by adding a `Dockerfile` to the application.
(Depending on the editor you are using, such as PyCharm or VSCode, there should be Docker-plugins available to help you to manage a `Dockerfile`.)

A `Dockerfile` is a plain text file that includes instructions which docker uses to *package-up an application* into an *Image*.

This *Image* contains everything the application needs to run:
- A cut-down OS
- A runtime environment (e.g., Node, Python, etc.)
- Application files
- Thirds-party libraries
- Environment variables
- ...

Once we have an Image, we tell Docker to start a Container using that Image. 

As mentioned above, a Container is a just a process - but a special one:  it has its own file-system, provided by the Image.

### Run a Container

Our application gets loaded into a Container (or a process).
So instead of directly running an app via
```bash
<my-app>
```
we use Docker to run the application in a Container, an isolated environment
```bash
docker run <my-app>
```

Docker provides registries (such as [dockerhub](https://hub.docker.com/)), which is a storage for Docker Images that anyone can use.
Thus, Images that are used locally for development can easily be transferred to either testing- or production machines (with all dependencies etc.). 

With Docker, we can package an application into an Image and let it run virtually anywhere.

### Delete a Container

Running docker multiple times leaves stray containers that may eat up disk space. 
Hence, as a rule of thumb, we can clean up containers once we are done with them. 
To do that, we can run the `docker rm` command: Just copy the container IDs (we can find those via the `docker ps -a` command) and execute

```bash
docker rm <container ID_i> <container ID_j>
```

With the following command
```bash
docker rm $(docker ps -a -q -f status=exited)
```
we can delete all containers that have a status of exited.

### Examples

For the hands-on example of using Docker in a 'real-world' application, checkout the [hello-docker](hello-docker) directory.

Also, checkout the simple [hello-flask](hello-flask) directory, following [G. Singh's Blog-Post](https://towardsdatascience.com/docker-made-easy-for-data-scientists-b32efbc23165).
