from flask import Blueprint, request, render_template
import json

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # Read config file
    config = json.loads(open('config.json').read())
    return render_template("home/index.html", config=config)


@main.route('/read/json', methods=['POST', 'GET'])
def read_json():
    with open('data/objects.json') as data_file:
        json_data = json.load(data_file)

    result = {}
    data = {}
    for obj in json_data:
        data[obj['name']] = obj
        data[obj['name']]['dependedOnBy'] = []

    for key, value in data.items():
        for name in value['depends']:
            temp = []
            if data[name]:
                print(value['name'])
                temp.append(value['name'])
                data[name]['dependedOnBy'] = temp

    result['data'] = data
    return json.dumps(result)
