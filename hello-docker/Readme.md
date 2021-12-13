# The `hello-docker`  - Project

## Outline
1. We create an `app.js` file (within the [hello-docker](.) folder):
```bash
echo 'console.log("Hello Docker!");' > app.js
```

Let's say, this is an application (which it is, it prints a message to the terminal).

2 Now we want to **dockerize** this application: we want to 
  - **build**,
  - **run**, and
  - **ship it**, using docker.

## Run without Docker
If you want to use the app from a computer, here are the typical instructions to let the code run:
- Start with an OS
- **Install `node`** (to run javascript ocde, install with `sudo apt install nodejs`)
- Copy the app files.
- Run the application with the following command:
```bash
> node app.js
Hello Docker!
```

For this application, docker seems like an overkill - but what if there were many files, version-specific dependencies to the app, and so on?

## Docker Containerization
We add a [`Dockerfile`](./Dockerfile) to our application.

Typically, we start from a **base-image**
- which could be a [`alpine`-image](https://hub.docker.com/_/alpine) with a `nodejs` installation on top, or a 
- [`node`-image](https://hub.docker.com/_/node), which can directly be used for our project,

which you find both on [dockerhub](https://hub.docker.com/) (a registry for docker images).

1. We simply start with defining the **base-image** in the [`Dockerfile`](./Dockerfile) via
```bash
FROM node:alpine
```
where the tag `:apline` specifies the linux distribution we want to use ([`alpine`](https://hub.docker.om/_/alpine) is very light-weight, also see [`ubuntu`](https://hub.docker.om/_/ubuntu)). 

This will be the image we will download on build our application on top.

2. Then we need to **copy** our program-files (the entire application) to the image:
```bash
COPY . /app
```
Here, we are copying every file within the [hello-docker](.) directory into the `/app` directory of the image (remember, a docker-container has its own file-system).

3. Finally, we want to execute our `app.js` command using `node`, which we achieve via the last two lines
```bash
WORKDIR /app
CMD node app.js
```


Note, that in the container, the `app.js` application is located within the `/app` directory in the image. Thus, we need to either run `CMD node /app/app.js` to execute the application, or, as in our case, we first `cd` into the `/app` directory using `WORKDIR /app` and execute `CMD node app.js` subsequently.

## Run with Docker
1. Build the Docker-Image (depending on your Docker installation, you might need to execute all `docker` commands as `sudo`)
```bash
docker build -t hello-docker .
```
With the `-t` option, we specify the `tag` of the image (its name, i.e. `hello-docker`), 
and we specify where `docker` can find the [`Dockerfile`](./Dockerfile) via `.`, i.e., in the (current) [hello-docker](.) directory.

2. Check the Docker-Image List
```bash
> docker image ls
REPOSITORY     TAG       IMAGE ID       CREATED              SIZE
hello-docker   latest    14d7b21bf6b5   About a minute ago   170MB
node           alpine    bb1fcdaff936   11 days ago          170MB
hello-world    latest    feb5d9fea6a5   2 months ago         13.3kB
```
Here we can find our `hello-docker` image with a size of `170MB` (we used Linux-alpine, thus the image is rather lightweight since alpine is a rather small engine). 

4. Run the Application in a Docker-Container
```bash
> run hello-docker
Hello Docker!
```

## Distribute via [dockerhub](https://hub.docker.om/_/ubuntu)
We could now distribute the `hello-docker` image via dockerhub, so we could use it from any computer (following this [how-to](https://docs.docker.com/docker-hub/repos/)).

To push an image to Docker Hub, you must first name your local image using your Docker Hub username and the repository name that you created through Docker Hub on the web.

Thus, we re-tag our local image using
```bash
sudo docker tag hello-docker bhartl/hello-docker
```

And `push` the container to `dockerhub` via
```bash
sudo docker push bhartl/hello-docker
```

The image can then be accessed, see [bhartl/hello-docker](https://hub.docker.com/repository/docker/bhartl/hello-docker).

*Note: make sure to be logged in to `dockerhub` on the command line via `docker login`.*

Vice-versa, a docker-image can be downloaded, i.e. `pulled`, from docker-hub via 
```bash
sudo docker pull bhartl/hello-docker
```
