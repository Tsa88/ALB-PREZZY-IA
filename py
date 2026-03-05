from flask import Flask, render_template, jsonify

app = Flask(__name__)

presentation_data = {
    "objects": [
        {"id": "1", "type": "text", "content": "Bem-vindo ao Prezi Clone", "x": 500, "y": 500, "scale": 1, "rotation": 0},
        {"id": "2", "type": "text", "content": "O que é ZUI?", "x": 1500, "y": 500, "scale": 0.5, "rotation": 15},
        {"id": "3", "type": "text", "content": "Zooming User Interface", "x": 1500, "y": 600, "scale": 0.2, "rotation": 0},
        {"id": "4", "type": "frame", "content": "Área de Detalhes", "x": 1500, "y": 550, "scale": 2, "rotation": -10}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_presentation')
def get_presentation():
    return jsonify(presentation_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
