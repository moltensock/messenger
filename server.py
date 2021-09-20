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

    if message == '/help':
        message = {
            'time': time.time(),
            'name': 'Bot',
            'text': 'Правила'
        }
        db.append(message)

    return {'ok': True}


@app.route('/messages')
def get_message():
    result = []

    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    for message in db:
        if message['time'] > after:
            result.append(message)
            if len(result) >= 100:
                break

    return {'messages': result}


if __name__ == '__main__':
    app.run()
