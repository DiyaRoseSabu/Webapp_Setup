# Webapp_Setup
A simple web application using HTML, CSS and Flask.
This application allows us to create a blog and upload it.
# Flask 

With the help of the lightweight Python web framework Flask, you can create web apps rapidly and with little boilerplate code. 
Flask does make certain recommendations, but it is the developer's responsibility to install the necessary dependencies.


# Install Flask 
To install flask we 1st need to create an virtual environment  


```
pip install virtualenv
```   


Install Flask  


```
pip install flask
```

The app.py file contains the flask code, while the templates file is made up of html files. 


# Docker

To build the Docker image:
```
docker build -t webapp .
```

To run the Docker container:
```
docker run -dp 9999:5000 webapp
```

To view the web app:
```
http://localhost:9999/
```

