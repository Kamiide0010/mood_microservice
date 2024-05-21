README

This microservice handles user input for name, age, and mood. It validates the input, processes it, and stores it in a text file.

Endpoint Information
URL: /user
Method: POST
Content-Type: application/json

**Request Data**
To request data from the microservice, use the following JSON format:

{
  "name": "Minca",
  "age": 24,
  "mood": "happy"
}

**Example Call**
Here is an example of how to send a request to the microservice using the requests library:
import requests

url = 'http://127.0.0.1:5000/user'
payload = {
    'name': 'Minca',
    'age': 24,
    'mood': 'happy'
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("Response from microservice:", response.json())
else:
    print("Failed to get response from microservice")

**Example of Receiving Data**
import requests

url = 'http://127.0.0.1:5000/user'
payload = {
    'name': 'Minca',
    'age': 24,
    'mood': 'happy'
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Received data from microservice:")
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"Mood: {data['mood']}")
else:
    print("Failed to get response from microservice")



![image](https://github.com/Kamiide0010/mood_microservice/assets/102687528/3377f6a0-119d-4976-b36d-6b94f4c63d7c)
