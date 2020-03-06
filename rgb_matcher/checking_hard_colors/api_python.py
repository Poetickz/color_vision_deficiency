from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import colorchange as color
from flask import jsonify


app = Flask(__name__)
api = Api(app)


def parse_rgb(rgb):
    new_rgb = rgb.split('-')
    return (int(new_rgb[0]),int(new_rgb[1]),int(new_rgb[2]))


class ChangeColor(Resource):
    def get(self, rgb, level):
        response = jsonify({'data': color.modify_rgb(parse_rgb(rgb), float(level))})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

        

api.add_resource(ChangeColor, '/changecolor/<rgb>/<level>') # Route_1

if __name__ == '__main__':
     app.run(port='5002')