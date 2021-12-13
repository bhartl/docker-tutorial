# Simple Flask APP
following [G. Singh's Blog-Post](https://towardsdatascience.com/docker-made-easy-for-data-scientists-b32efbc23165).

This is a very simple app that prints ‘Hello World!’ on a browser’s screen.
The Python-code can be found in [app.py](app.py).

All Python-dependencies are listed in [requirements.txt](requirements.txt).

## Containerizing the app

Here is the outline, what we are going to do:

1. We will create a [Dockerfile](Dockerfile) that will contain information about the Docker Image which runs our application. (It includes a base-image, python, python environment and then running the app itself.)
2. Then we will build a Docker Image,
3. and start a Docker Container thereof.

### The Dockerfile
1. We pull an ubuntu image (using the `:latest` tag): `FROM ubuntu:latest`
2. Since the Image is _fesh_, we have to update the local database via: `RUN sudo apt update -y`
3. We install python (there is no need to setup a virtual environment, since we will be using only one application in the container): `RUN apt install -y python3-pip`
4. Next, we copy all files from the current directory to the Docker Image folder `/app`: `COPY . /app`
5. We set the working-directory to the `/app` folder: `WORKDIR /app`
6. We install all python-dependencies using `pip3`: RUN pip3 install -r requirements.txt
7. We start the application: `CMD python3 app.py

### Build the Docker Image
To build the Image, we simply execute:
```bash
docker build -t hello-flask .
```
(Depending on your Docker installation, you might need to execute the command as `sudo`) 

And you can check all available Docker Images via 
```bash
> docker image ls
REPOSITORY            TAG       IMAGE ID       CREATED              SIZE
hello-flask           latest    b1a58b5390bc   About a minute ago   417MB
```
where we can find our `hello-flask` image. 

### Run the App in a Docker Container
The next task will be to run that Docker Image as a container on our local machine:
```bash
docker run -d -p 5000:5000 hello-flask
```

- `5000:5000` means we have attached port `5000` of our system to Docker. The latter port is of Flask, which runs on port `5000` per default.
- The `-d` flag means we want to run it in daemon mode (in background).

To check whether our container is running or not, we run
```bash
> docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS                                       NAMES
ac82cb1876b8   hello-flask    "/bin/sh -c 'python3…"   12 seconds ago      Up 11 seconds                  0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   great_nobel
```

If so, we can see the `Hello World` output when browsing our [Hello-Flask](http://127.0.0.1:5000/) at [http://127.0.0.1:5000](http://127.0.0.1:5000/).

To access the `print_square(arg)` function in the [app.py](app.py), we can use, for instance, `curl`:
```bash
> curl -X POST http://127.0.0.1:5000/square -d 5
25
```

To stop the Docker Container (if it is running as daemon), we simply execute 
```bash
docker stop ac82cb1876b8
```

where `ac82cb1876b8` is the `CONTAINER ID` of our Docker `helo-flask` Image.
