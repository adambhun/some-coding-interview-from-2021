I forgot to copy the instructions for these tasks and I haven't finished all of them, because I was hired in the meantime.

The tasks were roughly the following:

- create a python application that places cuboids in a 3D coordinate system, and as input it takes a list of integers, which represent a coordinate and the length of the edges of the cuboid.

- create a web server for the app above

- Write some Ansible+Ruby script to deploy it in Kubernetes.


# Application

The application is split into two files; server.py is a restful Flask server which calls the methods defined in geometry.py.

## Server.py

Runs listens on port 5000.

Has one endpoint: "/bodies", which accepts the following xmlhttprequests (tested with Postman):
* GET - to get a single object. Request's body: x-www-form-urlencoded. Expected content:
  ```
  {
    "id": ""
  }
  ```

* GET - to calculate the distance of two objects. Request's body: x-www-form-urlencoded. Expected content:
  ```
  {
    "id": "",
    "id2": ""
  }
  ```

* POST - to add an object. Request's body: x-www-form-urlencoded. Expected content:

  ```
  {
    "x": "",
    "y": "",
    "z": "",
    "w": "",
    "h": "",
    "d": ""
  }
  ```

* PUT - to modify an object. Request's body: x-www-form-urlencoded. Expected content:

  ```
  {
    "id": "",
    "x": "",
    "y": "",
    "z": ""
  }
  ```


# architecture

## ruby

## ansible

## CLI
* kubectl & kops???

## scalability

cpu/mem/requests???
