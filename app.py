from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import urllib.request, json
import random

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/image', methods=['POST'])
def image():
    print(request.method)
    data = request.json
    print(data)
    try:
        data_id = int(data['id'])
        print(data_id)
        if(data_id > 2709 or data_id < 1):
            raise ValueError
        statusCode=200
    except ValueError:
        # Handle the exception
        data_id = random.randrange(0,2709)
        statusCode=201
    url = "https://xkcd.com/{}/info.0.json".format(data_id)
    response = urllib.request.urlopen(url)
    xkcd_res = response.read()
    print(xkcd_res)
    xkcd = json.loads(xkcd_res)
    print(xkcd)
    return jsonify(statusCode=statusCode, img=xkcd["img"]), 200