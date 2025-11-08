from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur mon API de dog images !"

@app.route('/api/images/search', methods=['GET'])
def get_dog_image():
    data = [
        {
            "id": "Z6h74tJ-D",
            "url": "https://cdn2.thedogapi.com/images/Z6h74tJ-D.jpg",
            "width": 1080,
            "height": 1080
        }
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
