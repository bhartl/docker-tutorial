# Docker with [Mosh](https://www.youtube.com/watch?v=pTFZFxd4hOI)
a beginners-to-pro hands-on tutorial by [*Mosh Hamedani*](codewithmosh.com), implemented by [B. Hartl](bhartl.github.io).

**Prerequisites**:
- 3 months of programming experience
- basic knowledge of front- and backend terminologies, git-commands

## What is Docker?
A platform for **building**, **running** and **shipping** applications - so if a software is running on your docker-machine, it will also run on others like it.

This might be caused by
- one or more missing files
- software version mismatch
- different configurations settings (such as environment variables)

Here, [docker](https://www.docker.com/) comes to the rescue:
- **Package-up your application**, with everything it needs, then **run it everywhere and anywhere** using docker.
- With `docker-compuse up`, all application-dependencies can _automatically_ be setup, on any machine, in an _isolated environment_, called a _container_.
- This allows, for instance, to run different versions of your application in different containers on a single machine.
- With docker, each application runs in its isolated environment, which can be turned down with `docker-compose down --rmi all`.
- So, docker helps us to **consistently** *build, run and ship* our *applications*.

## Virtual Machines vs Containers

### Virtual Machine 
_An abstraction of a machine (or of physical hardware)_

Several virtual machines (VMs) may be run from a single hardware. These VMs are managed by a so-called *hypervisor* (see, e.g., [VirtualBox](https://www.virtualbox.org/) or [VMware](https://www.vmware.com/)).
Software can then be written/installed/... on different VMs on the same physical hardware *in isolation*.

**Problems with VMs**:
- **Each VM** needs a **full-blown operating system** (OS) - so a copy of the entire OS it emulates (including licenses, ...).
- Vms are thus **slow to start** (the entire OS needs to be loaded such as starting your computer)
- They are **resource intensive**, since they rely on the physical hardware they run on (CPUs, RAM, Storage, ...).

### Container 
_An isolated environment for running applications_

Just like VMs, **containers allow**
- **running multiple apps in isolation**, 
- but they are **more lightweight**.
- All containers running on a system **share** the **same OS as the host** (thus, only a single OS needs to be licensed, hashed and monitored).
- Containers can be **started quickly** (often in less than a second), and they
- need **less hardware resources**, compared to VMs (no CPUs or memory needs to be especially assigned to containers).

## Architecture of Docker
Docker uses a **client-server architecture**. 
The client component communicates with the server component using a REST API. 
The server (i.e., the *docker engine*) manages docker-containers. 

Technically, containers are just *processes*, running on a computer.
All containers share the OS of the host, or, more accurately, the host's kernel.
Thus, Linux-containers can be run on all Linux-kernels (e.g., on a _Linux_ machine, on _Windows>=10_ systems, or on MACs' *Linux VM*).

## Installing Docker 
Install instructions for docker can be found at [docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).
*Note: be sure to check the system prerequisites!*

For *Ubuntu 20.04* users: 
follow the instructions on [docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/).

To **verify** the **installation** of the Docker Engine, run the hello-world image.
```bash
sudo docker run hello-world
```

This command downloads a test image and runs it in a container. When the container runs, it prints a message and exits.

## Development Workflow
In short, any project (or application) can be *dockerized*:
 simple add a `Dockerfile` to the application.
(Depending on the editor you are using, such as PyCharm or VSCode, there should be Docker-plugins available to help you to manage a `Dockerfile`.)

A `Dockerfile` is a plain text files that includes instructions which docker uses to *package-up an application* into an *image*.

This *image* contains everything the application needs to run:
- A cut-down OS
- A runtime environment (e.g., Node or Python)
- Application files
- Thirds-party libraries
- Environment variables
- ...

Once we have an image, we tell docker to start a container using that image. 

As mentioned above, a container is a just a process - but a special one: 
it has its own file-system, provided by the image.

Our application gets loaded into a container (or a process).
So instead of directly running an app via
```bash
my-app
```
we use docker to run the application in a container, an isolated environment
```bash
docekr run ...
```

Docker provides registries (such as [dockerhub](https://hub.docker.com/)), which is a storage for docker images that anyone can use.
Thus, images that are used locally for development can easily be transferred to either testing- or production machines (with all dependencies etc.). 

With docker, we can package an application into an image and let it run virtually anywhere.

### Examples

For the hands-on example of using docker in a real-world application, checkout the [hello-docker](hello-docker) app.

Also checkout the simple [hello-flask](hello-flask) app, following [G. Singh's Blog-Post](https://towardsdatascience.com/docker-made-easy-for-data-scientists-b32efbc23165).