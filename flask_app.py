from flask import Flask, request, json
from settings import *
from predictor import Predictor
from simulating import Generator
import messageHandler

app = Flask(__name__)


@app.route('/', methods=['POST'])
def processing():
    predictor = Predictor()
    generator = Generator()
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token, predictor, generator)
        return 'ok'

if __name__ == '__main__':
    app.run()
