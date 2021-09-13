from flask import Flask, request

app = Flask(__name__)
ListOfMessages = []


@app.route('/')
def hello_world():
    return 'Messenger is running! ' \
           '<br> <a href="/status">Кто нажмёт тот пидор</a>'


@app.route('/status')
def status():
    return {
        'messages_count': len(ListOfMessages)
    }


@app.route("/api/Messenger", methods=['POST'])
def SendMessage():
    message = request.json
    print(message)
    ListOfMessages.append(message)
    print(message)
    message_text = f"{message['UserName']} <{message['TimeStamp']}>: {message['MessageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)}. Посланное сообщение: {message_text}")
    return f"Сообщение отправлено! Всего сообщений: {len(ListOfMessages)} ", 200


@app.route("/api/Messenger/<int:id>")
def GetMessage(id):
    print(id)
    if 0 <= id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "Not found", 400


if __name__ == '__main__':
    app.run()
