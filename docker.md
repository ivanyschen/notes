# Docker Cheatsheet

## Long way to create and run container
- `docker container create <image-name>`: create a container
- `docker ps`: show containers that are actively running.
- `docker ps --all`: show all containers
- `docker container start <container-id>`: run the container
- `docker logs <container_id>`: show logs of the container
- `dockere container start --attach <container-id>`: attach terminal to container's output

## short way to create and run container
- `docker run <image-name>` = `docker container creater <image_name>` + `dockere container start --attach <container-id>`

## Dockerfile
### keywords
- `FROM`: Which exisiting image to base the image off.
- `LABEL`: Add additional information to the image
- `USER`: Tell Docker which user to use to run command underneath it. `root` is the default
- `COPY`: Copy files to Docker image
- `RUN`: Commands to customize the image
- `ENTRYPOINT`: ENTRYPOINT command is overwritten before the image with its own command line flag (`docker run --entrypoint="override" image`). Then, all CMD arguments will be added after ENTRYPOINT as its parameters. In many cases, the entrypoint is set as sh -c. You can find this with `docker inspect image -f '{{ .Config.Entrypoint }}'`
- `CMD`: CMD sets default command and/or parameters to the entrypoint, which can be overwritten from command line when docker container runs (`docker run example "override"`).


- `docker build -t <image-name> /path/to/app`
- `docker kill <container-id>`
- `docker run -d <server-container-id>`: run the contain in the background
- `docker exec --neractive --tty <container-id> bash`: start a bash shell within a container
- `docker stop <container-id>` stop the container gracely
- `docker stop -t 0 <container-id>`: stop the container forcefully
- `docker rm <container-id>`: remove container
- `docker ps -aq | xargs docker rm`: remove all conotainers
- `docker rmi <image-id>`: remove the image

## Port Binding
- `docker run -d -p 5001:5000 <image-name>`: outside port 5001 is binded to inside port 5000

## volumn Mounting (-volumn)
- `docker run --rm --entrypoint sh -v /tmp/container:/tmp ubuntu -c "echo 'Hello there.' > /tmp/file && cat /tmp/file"`
