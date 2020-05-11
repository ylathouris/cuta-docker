
---

# Cuta Docker

This project provides a collection of Docker images for [Cuta]. These
images are designed to make it easier to **build**, **test** and
**deploy** container-based applications (i.e. services, serverless).

<br/>

## Images

### `aws-python`

This is the base image for [Cuta] apps that are written in [Python]
and deployed to [AWS]. It provides a base set of packages for python
development.

> **Note:** This image is not used directly by [Cuta]. It is used
> by other [Python] images.

### `aws-python3.8`

This image is for [Cuta] apps using [Python 3.8] with [AWS].


### `aws-python3.7`

This image is for [Cuta] apps using [Python 3.7] with [AWS]


### `aws-python3.6`

This image is for [Cuta] apps using [Python 3.6] with [AWS]


### `aws-python2.7`

This image is for [Cuta] apps using [Python 2.7] with [AWS]


<br/>


## Commands (CLI)

This section proviides an overview of the Command Line Interafce (CLI).


### `cuta-docker build <key>`

Use this command to build one of the [Cuta] images described above.

```bash
$ cuta-docker build aws-python
```

### `cuta-docker push <key>`

Use this command to push a [Cuta] image to docker hub.

```bash
$ cuta-docker push aws-python
```


<br/>


[Cuta]: https://github.com/ylathouris/cuta
[Docker]: https://www.docker.com/
[AWS]: https://aws.amazon.com/
[Python]: https://www.python.org/
[Python 3.8]: https://www.python.org/downloads/release/python-382/
[Python 3.7]: https://www.python.org/downloads/release/python-377/
[Python 3.6]: https://www.python.org/downloads/release/python-3610/
[Python 2.7]: https://www.python.org/downloads/release/python-2718/

