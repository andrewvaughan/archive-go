# GO

Go is a URL shortening service written in Python.  It is intended to be a very bare-bones
implementation of a URL service, providing only a basic, RESTful API and the URL forwarding service.


## Dependencies

1. **[python 2.7](https://www.python.org/download/releases/2.7/)**
1. **[bottle](http://bottlepy.org/)** a lightweight web framework
1. **[redis](http://redis.io/)** a key-value cache and store


## Installation

After installing all required depencies, a manual install of GO can be installed by using the
included python installer:

```
python setup.py install
```


## Configuration

Create a `server.ini` file in the `/conf/` directory.  Refer to `default.ini` for options and a
description of each configuration option.


## Logging

TBD


## Usage

Invoke the GO service by calling `go` from the terminal after setup.