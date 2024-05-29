from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def get_user_data():
    try:
        name = request.json.get('name')
        age = request.json.get('age')
        mood = request.json.get('mood')
        
        if not name or not age or not mood:
            raise ValueError("Missing name, age, or mood in the request")

        response = {
            "name": name,
            "age": age,
            "mood": mood
        }

        print(f"Received data: Name={name}, Age={age}, Mood={mood}")

        # Store the data in a text file
        with open("user_data.txt", "a") as file:
            file.write(f"Name: {name}, Age: {age}, Mood: {mood}\n")
        
        return jsonify(response), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
