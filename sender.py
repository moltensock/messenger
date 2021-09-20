import requests

response = requests.get('http://127.0.0.1:5000/status')
print(response.status_code)
print(response.text)
print(response.json())

# data = {
#    'name': 'Алёша',
#    'text': 'Привет'
# }

