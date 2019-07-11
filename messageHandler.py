import vkapi
from predictor import Predictor


def get_answer(body):
    predictor = Predictor()
    message = predictor.chainer()
    if message:
        return '*текст про космос*'
    else:
        return 'Х*ли пришел???'


def create_answer(data, token):
    user_id = data['user_id']
    message = get_answer(data['body'].lower())
    vkapi.send_message(user_id, token, message)
