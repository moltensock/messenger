import random
import time

def send_message(name, text):
    message = {
        'time': time.time(),
        'name': name,
        'text': text
    }
    db.append(message)

def get_message(after):
    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
    return result

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

# for message in db:
#    print(message['time'], message['name'])
#    print(message['text'])
#    print()

print(db)
t1 = db[-1]['time']
print(get_message(t1))

send_message('123', '123')
send_message('123', '456')
print(get_message(t1))

t2 = db[-1]['time']
print(get_message(t2))

send_message('123', '789')
print(get_message(t2))