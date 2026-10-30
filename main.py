from flask import Flask
import os
import requests
from dotenv import load_dotenv
from livereload import Server

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")





if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('templates/*.html')
    server.watch('static/*.css')
    server.serve(port=5000, debug=True)