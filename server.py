from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from geometry import Shape

shape = Shape()

app = Flask(__name__)
api = Api(app)


class Body(Resource):
    def __init__(self):
        self.body = {
            "id": "",
            "x": "",
            "y": "",
            "z": "",
            "w": "",
            "h": "",
            "d": "",
            "id2": "",
        }

    def get_args(self):
        parser = reqparse.RequestParser()
        for i in self.body:
            parser.add_argument(i)
        args = parser.parse_args()
        return parser, args

    def get(self):
        parser = self.get_args()[0]
        args = self.get_args()[1]
        parser.add_argument("id2")
        args = parser.parse_args()
        id = int(args["id"])
        if args["id2"] == None:
            args.pop("id2")
            numbers = [i for i in shape.fetch_shape(id)]
            numbers.insert(0, id)
            for i, j in zip(numbers, args):
                args[j] = i
            return args, 200
        else:
            id2 = int(args["id2"])
            first = shape.fetch_shape(id)
            first_vertices = shape.get_vertices(*first)
            second = shape.fetch_shape(id2)
            second_vertices = shape.get_vertices(*second)
            return shape.compare_distances(first_vertices, second_vertices), 200

    def post(self):
        parser = self.get_args()[0]
        args = self.get_args()[1]
        args.pop("id2")
        iter_args = iter(args)
        next(iter_args)
        stats = []
        for i in iter_args:
            stats.append(int(args[i]))
        result = shape.add_shape(*stats)
        if result == False:
            return 400
        else:
            return result, 201

    def put(self):
        parser = self.get_args()[0]
        args = self.get_args()[1]
        if shape.modify_shape(*[int(args[i]) for i in list(args)[0:4]]) == True:
            return 200
        else:
            return 400


api.add_resource(Body, "/bodies")

app.run(debug=True)
