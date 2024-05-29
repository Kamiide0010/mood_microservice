import requests

def get_user_input():
    def validate_name(name):
        # Check if all characters are alphabetic or spaces
        return all(char.isalpha() or char.isspace() for char in name)

    while True:
        name = input("Enter your name: ")
        if isinstance(name, str) and validate_name(name):
            break
        else:
            print("Invalid input, letters and spaces only, please try again.")

    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid input, numbers only, please try again.")

    while True:
        mood = input("Enter your mood/emotion: ")
        if isinstance(mood, str) and mood.isalpha():
            break
        else:
            print("Invalid input, letters only, please try again.")

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
