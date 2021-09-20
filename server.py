import time
from datetime import datetime
from flask import Flask, request, abort

app = Flask(__name__)
db = [
    {
        'time': time.time(),
        'name': 'Олег',
        'text': 'ммм хуита'
    },
    {
        'time': time.time(),
        'name': 'Женя',
        'text': 'и правда хуита'
    }
]


@app.route('/')
def hello_world():
    return 'Messenger is running!' '<br> <a href="/status">тык</a>'


@app.route('/status')
def status():
    return {
        'messages_count': len(db),
        'status': True,
        'name': 'Messenger',
        # 'time': time.asctime(),
        'time2': datetime.now().strftime('%m.%d.%Y')
    }


# @app.route("/api/Messenger", methods=['POST'])
# def SendMessage():
#    message = request.json
#    print(message)
#    ListOfMessages.append(message)
#    print(message)
#    message_text = f"{message['UserName']} <{message['TimeStamp']}>: {message['MessageText']}"
#    print(f"Всего сообщений: {len(ListOfMessages)}. Посланное сообщение: {message_text}")
#    return f"Сообщение отправлено! Всего сообщений: {len(ListOfMessages)} ", 200


# @app.route("/api/Messenger/<int:id>")
# def GetMessage(id):
#    print(id)
#    if 0 <= id < len(ListOfMessages):
#        print(ListOfMessages[id])
#        return ListOfMessages[id], 200
#    else:
#        return "Not found", 400

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if set(data.keys()) != {'name', 'text'}:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str) or name == '' or text == '':
        return abort(400)

    message = {
        'time': time.time(),
        'name': name,
        'text': text
    }

    db.append(message)
    return {'ok': True}


@app.route('/messages')
def get_message():
    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
    return result


if __name__ == '__main__':
    app.run()
