from flask import Flask, request, redirect, url_for, render_template
import requests, json
from pprint import pprint

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello():
    return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
 