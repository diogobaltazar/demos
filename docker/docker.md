ls images
`docker image ls`

``docker rm --force <img-name>``
``docker build --tag <img-name>:<img-version> .``
``docker run --publish 127.0.0.1:8000:8000 --detach --name <img-name> <img-name>:<img-version>``
