function enviarImagem() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('imagem', file);
    console.log(formData)
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        for(let i = 1; i < 6; i++){
            document.getElementById('p' + i).innerHTML = data.teste[i - 1]
        }
        console.log(data); //USAR DATA COMO VARIAVEL DE RETORNO, USAR ELA PRA INSERIR NA PAGINA A PRECISAO
    })
    .catch(error => {
        console.error(error);
    });
}

function processarImagem() {
    var nome = 'LED.png';
    var formData = new FormData();
    formData.append('nome_imagem', nome);

    fetch('/exec-python', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error(error);
    });
}