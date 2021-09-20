import requests

# response = requests.get('http://127.0.0.1:5000/status')
# print(response.status_code)
# print(response.text)
# print(response.json()['status'])

data = {
    'name': 'Алёша',
    'text': 'Привет'
}

response = requests.post(
    'http://127.0.0.1:5000/send',
    json={
        'name': 'Алёша',
        'text': 'Привет'
    }
)
