from flask import Flask, render_template, request
import os

from flask_cors import CORS,cross_origin
from flask import *


app=Flask (__name__,static_folder='static')
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/", methods=['GET'])
def Voice_Api():
    return 'shit'

if __name__== '__main__':
    app.run(debug=True, port=5665)


