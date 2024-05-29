import requests

def get_user_input():
    while True:
        name = input("Enter your name: ")
        if not isinstance(name, str) or not name.isalpha():
            print("Invalid input, letters only, please try again.")
            continue

        age = input("Enter your age: ")
        if not age.isdigit():
            print("Invalid input, numbers only, please try again.")
            continue
        age = int(age)
        
        mood = input("Enter your mood/emotion: ")
        if not isinstance(mood, str) or not mood.isalpha():
            print("Invalid input, letters only, please try again.")
            continue

        return name, age, mood

def test_microservice(name, age, mood):
    url = 'http://127.0.0.1:5000/user'
    payload = {
        'name': name,
        'age': age,
        'mood': mood
    }
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        if response.status_code == 200:
            print("Response from microservice:", response.json())
        else:
            print("Failed to get response from microservice:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error during request:", e)

if __name__ == '__main__':
    name, age, mood = get_user_input()
    test_microservice(name, age, mood)
