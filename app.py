from flask import Flask, request, jsonify, render_template
import os
import teste as t
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

    print(recebidos)

    os.remove(os.path.join(diretorio_img, imagem.filename))
    
    return jsonify({'message': 'Imagem recebida e salva com sucesso', 'teste': recebidos}), 200

@app.route('/exec-python', methods=['POST'])
def executar():
    if 'nome_imagem' not in request.form:
        return jsonify({'error': 'Nenhuma imagem encontrada', 'teste': request.form['nome_imagem']}), 400
    
    nome_imagem = request.form['nome_imagem']
    t.executarPlot(nome_imagem)

    return jsonify({'message': 'sucesso'}), 200 #USAR O JSONIFY PRA VOLTAR UMA INFORMAÇÃO PRO JAVASCRIPT


if __name__ == '__main__':
    app.run(debug=True)

