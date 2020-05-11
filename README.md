
---

# Cuta Docker

This project provides a collection of Docker images for [Cuta]. These
images are designed to make it easier to **build**, **test** and
**deploy** container-based applications (i.e. services, serverless).

How exactly does **Cuta Docker** make it easier to **build**, **test**
and **deploy** applications? By providing the following features:

### Ready-To-Go Environments

The images in this project are **ready-to-go** development environments.
This means you don't have to worry about installing things like runtimes,
package managers and many of the obscure libraries required to build
your software. It all comes pre-packaged in our environments. Of course,
if you want to customise the images with your favourite development tools,
you can! All our environments are publicly accessible as docker images.
You can extend them or replace them entirely.


### Consistent Environments

As mentioned, our **ready-to-go** development environments come with
everything you need to **build**, **test** and **deploy** your app. The
only software you'll need to install is the software required by your
app at runtime (and we provide an easy way to do that too!). Not only
that, our images provide consistency for you and your fellow developers.
You won't have to worry about version descrepancies or platform variants.


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

