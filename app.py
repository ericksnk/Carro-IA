from flask import Flask, request, jsonify, render_template
import os
import IA.firstprediction as ia

app = Flask(__name__)

diretorio = os.getcwd()
diretorio_img = diretorio + "\images"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'imagem' not in request.files:
        return jsonify({'error': 'Nenhuma imagem encontrada'}), 400
    
    imagem = request.files['imagem']
    # Salvar a imagem em um arquivo no servidor
    imagem.save(os.path.join(diretorio_img, imagem.filename))

    recebidos = ia.previsao(imagem.filename)

    #print(recebidos)

    os.remove(os.path.join(diretorio_img, imagem.filename))
    
    if(recebidos == -1):
        return jsonify({'message': 'Erro no processamento do arquivo', 'teste': recebidos}), 300
    else:
        return jsonify({'message': 'Imagem recebida e salva com sucesso', 'teste': recebidos}), 200



if __name__ == '__main__':
    app.run(debug=True)

