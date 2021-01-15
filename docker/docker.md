<<<<<<< HEAD
ls images
`docker image ls`

``docker rm --force <img-name>``
``docker build --tag <img-name>:<img-version> .``
``docker run --publish 127.0.0.1:8000:8000 --detach --name <img-name> <img-name>:<img-version>``
=======
# intro

`Containers` are like OSs but they are not meant to host entire OSs, they are meant to host a task, and should terminate once the task terminates. Containers **share the same host OS kernel**. Examples of types of containers: `LXC`, `LXT`, `LXCFX`. Docker uses LXC containers but simplifies the creation of the container. Linux containers can only run on a Linux `docker host` or `docker engine`. DOS containers can only run on a DOS docker host.
Running linux docker containers on windows means that windows creates a linux VM that will run the container. `Hypervisors` virtualize different kernels on the same hardware. Docker does not attempt to do that. Docker's purpose is to containerize applications in a specifically tailored operating system configuration. Virtual machines require a hypervisor because they virtualize the kernel. Docker does not need to do that and so is faster. Docker for windows creates a VMs for linux docker containers, that's why it requires Hypervisor. VMs are completely isolated from each other, containers share the kernel. Containerizing an application makes it easier to deploy it because the container ships both the application and all its' dependencies. These containers are made available in `docker hubs` or `docker stores`. An `image` is a package/template (`vms`/`containers` are created with `images`). `Containers` are running instances of `images`. the `image` for a docker container is specified in a `dockerfile`.

Every container running on the host has a unique identifier (`IP`) `ip-container` whose scope is restricted to the host, *i.e.*, the host knows it's containers (also) by their IPs. Every container running in a docker host has (also) an unique identifier (`PORT`) `port-host` inside the host, whose scope is restricted to the OS hosting docker. Likewise, the host has a unique identifier (`IP`) `ip-host` whose scope is restricted to the OS hosting docker. So a container can be referenced from the OS hosting docker by `ip-host:port-host`. Every app running in a container has (also) an unique identifier (`PORT`) `port-container` inside the container, whose scope is restricted to the host. So an app running on a container can be referenced from the OS hosting docker by `ip-host:port-host:[ip-container:]port-container`. Indeed the `ip-container` is optional and I'm clueless why.

[src](https://www.youtube.com/watch?v=fqMOX6JJhGo)

# commands

run image in container. The image is either on the local host or on the docker hub. If the image is not present in the local host, it will fetch it from the hub.

    $ docker run [-e <var-name>=<var-value>] [[-it] | [[<ip-host>]:<port-host>:<port-container>] [-v <dir-host>:<dir-container>] <img>:[<img-version>|latest]

`-i` – **interactive** map parent proccess stdin to container stdin  
`-t` – **pseudo-terminal** create terminal for the mapping  
`[<ip-host>]:<port-host>:<port-container>` – port mapping between host-port and container-app-port  
`-v <dir-host>:<dir-container>` – mount host directory to container directory, meaning that operations performed to `<dir-container>` will be persisted because they are in fact performed to `<dir-host>`  
`-e <var-name>=<var-value>` – create container environment var `<var-name>` with value `<var-value>`. These variables are found in the container environment by running from the OS `docker inspect <container-name>` under `Config.Env`.      

run command in container

    $ docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]

`--rm` – Specifies to clean up the container after the command exits.
`-it` – Specifies to open a pseudo-TTY with stdi\n. This enables you to provide input to the AWS CLI version 2 while it's running in a containe
`-V` – Because the AWS CLI version 2 is run in a container, by default the CLI can't access the host file system, which includes configuration and credentials. To share the host file system, credentials, and configuration to the container, mount the host system’s ~/.aws directory to the container at /root/.aws with the -v flag

show running containers

    $ docker ps [-a]

`-a` show history of executed containers

show information of running containers

    $ docker inspect <container-name>

show `stdout` of running command

    $ docker logs <container-name>

stop container

    $ docker stop <container-id>|<container-name>

remove container

    $ docker rm <container-id>|<container-name>

list images

    $ docker images

remote image

    $ docker rmi <image-name>

pull image from hub

    $ docker pull <iamge-name>

run command in container

    $ docker exec <container-id>|<container-name> <command>

run container in detach mode (background of parent process)

    $ docker run -d <container-id>|<container-name>

attach container to proccess

    $ docker attach <container-id>|<container-name>
<<<<<<< HEAD

build image

    $ docker build <container-image-path> -t <image-tag-name> 

`-t` – **pseudo-terminal** create terminal to map parent process stdin to image stdin  

push image to docker registry

    $ docker push <image-tag-name>
=======
>>>>>>> 018418985ef860e87b5e9f2a3a3153a24d471bd3
>>>>>>> 10080358e245b46731c7cd9c7511b329281985ff
