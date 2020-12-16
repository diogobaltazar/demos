# intro

Containers are OSs. Containers share the same host OS kernel. Eaxmples of types of containers: LXC, LXT, LXCFX. Docker uses LXC containers but simplifies the creation of the container. Linux containers can only run on a Linux docker host.
Running linux docker containers on windows means that windows creates a linux VM that will run the container. Hypervisors virtualizes different kernels on the same hardware. Docker does not attempt to do that. Docker's purpose is to containerize applications in a specifically tailored operating system configuration. Virtual machines require a hypervisor becuase they virtualize the kernel. Docker does not need to do that and so is faster. VMs are completely isolated from each other, containers share the kernel. Containerizing an application makes it easier to deploy it because the container ships both the application and all its' dependencies. These containers are made available in docker hubs/stores. An `image` is a package/template (`vms`/`containers` are created with `images`). `Containers` are running instances of `images`. the `image` for a docker container is specified in a `dockerfile`.

[src](https://www.youtube.com/watch?v=fqMOX6JJhGo)

run command in image
    $ docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]

``--rm`` – Specifies to clean up the container after the command exits.
``-it`` – Specifies to open a pseudo-TTY with stdi\n. This enables you to provide input to the AWS CLI version 2 while it's running in a containe
`-V` - Because the AWS CLI version 2 is run in a container, by default the CLI can't access the host file system, which includes configuration and credentials. To share the host file system, credentials, and configuration to the container, mount the host system’s ~/.aws directory to the container at /root/.aws with the -v flag
