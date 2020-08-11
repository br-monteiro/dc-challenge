#### Part-1
This is my submission to DC-Team for `part-1`.

### Dependencies
- docker
- docker-compose
- *Python 3.5
- *Redis 6.0.6

>*provide in docker container

### Setup
To start the project, just run the command bellow:

```bash
$ docker-composer up -d
```

This command provide a Docker container with the application (API and Cache Server).
After start, the address `http://localhost:5000/v1/products` is available for HTTP Post method.

### Solution
First, we order the body content (JSON) received on route `/v1/products`,
then we make a hash string using `sha1` algoritme. With this value, so check
in the Cache Server by the value of the hash. The registers expires in 10min.

### Test
To run the unit tests, just run the command bellow:

```bach
$ python3 -m unittest
```

#### LAUS DEO ∴
