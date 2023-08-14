from flask import Flask, render_template, request, jsonify
from modelo.model import model

app = Flask(__name__)
model = model()


@app.route('/')
def index():
    '''
    Index de la app, te mada un html para enviar una oracion a mano
    '''
    return render_template('index.html')


@app.route('/send_text', methods=['POST'])
def send_text():
    '''
    Response a una sola peticion 
    '''
    text = request.form['text-input']
    nouns = model.get_entidades(text)
    return render_template('index.html', prediction = nouns) 


@app.route('/receive-list', methods=['POST'])
def receive_list():
    '''
    Responde a lista de oraciones 
    return: json con entidades
    '''
    data = request.json
    lst = model.get_lista(data['oraciones'])
    return jsonify(lst), 200

if __name__ == '__main__':
    app.run(port=3000, debug=True)