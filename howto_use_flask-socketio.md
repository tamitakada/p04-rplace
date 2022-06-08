# how-to :: USE FLASK-SOCKET.IO
---
## Overview
In traditional HTTP requests, the client connects to a server, sends a request, receives a response and then closes the connection. On the other hand, Websockets opens a 'tunnel' between the client and the server. The client and server can easily send requests and responses through it. This tunnel reduces unnecessary network traffic and provides speedier website responses.

Traditionally, Flask doesn't support Websockets because of the maintenance required for the Websocket tunnels. So, Flask-SocketIO comes to the rescue! Flask-socketio is an extension that allows Flask apps to have Websocket-like functionality. Essentially, this extension will allow us to use Websocket's streamlined server-client communication in Flask.

### Estimated Time Cost: 15 Minutes

### Prerequisites:

- Before you start following the steps, be sure to activate your virtual environment!

1. Install SocketIO package by typing `pip install flask-socketio` in terminal
2. Now you have to create a SocketIO server in your Flask application. To do so, add the code below to the top of your init file.
  ```python
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' #remember to make your own secret key
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app) #this function starts up the Socket-io server
  ```
3. Now you have to create a client connection in your HTML file. Using Javascript, add this code below
```javascript
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js" integrity="sha512-q/dWJ3kcmjBLU4Qc47E4A9kTB4m3wuTY7vkFJDTZKjTs8jhyGQnaUrxa0Ytd0ssMZhbNua9hE+E7Qv1j+DyZwA==" crossorigin="anonymous"></script>
<script type="text/javascript" charset="utf-8">
    var socket = io();
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
</script>
```
4. 

2. Step, with `inline code`, and/or...
1. Step, with
    ```
    generic code block or terminal command
    ```
   and/or...
    ```javascript
    var foo = "this that JS tho";
    ```
   and/or...
    ```python
    print("this that Python tho")
    ```
   and/or...
1. Step, with [hyperlink](https://xkcd.com)s...


### Resources
* https://flask-socketio.readthedocs.io/en/latest/
* thing2

---

Accurate as of (last update): 2022-07-08

#### Contributors:
Liesel Wong, PD1  

_Note: the two spaces after each name are important! ( <--burn after reading)  _
