run command in image
    $ docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]

``--rm`` – Specifies to clean up the container after the command exits.
``-it`` – Specifies to open a pseudo-TTY with stdin. This enables you to provide input to the AWS CLI version 2 while it's running in a containe
`-V` - Because the AWS CLI version 2 is run in a container, by default the CLI can't access the host file system, which includes configuration and credentials. To share the host file system, credentials, and configuration to the container, mount the host system’s ~/.aws directory to the container at /root/.aws with the -v flag
