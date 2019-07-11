import vkapi

def get_answer(body, predictor, generator):
    message = predictor.chainer([body])
    if message[0] == 1:
        return generator.make_chain()
    else:
        return 'Х*ли пришел???'

def create_answer(data, token, predictor, generator):
   user_id = data['user_id']
   message = get_answer(data['body'].lower(), predictor, generator)
   vkapi.send_message(user_id, token, message)