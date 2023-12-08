submitInput = document.getElementById('fileInput')


function enviarImagem() {
    //var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];
    fileType = fileInput.files[0].type
    fileSize = fileInput.files[0].size

    //document.getElementById("imgPreview").src = URL.createObjectURL(file);
    if(fileType == 'image/jpeg' || fileType == 'image/png' && fileSize < 15000000){
        var formData = new FormData();
        formData.append('imagem', file);
        console.log(formData)
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if(data.teste == -1){
                document.getElementById('aviso').innerHTML = "Arquivo de tipo inválido"
            }
            else{
                for(let i = 1; i < 4; i++){
                    document.getElementById('p' + i).innerHTML = data.teste[i - 1] + "%"
                }
            }
            console.log(data); //USAR DATA COMO VARIAVEL DE RETORNO, USAR ELA PRA INSERIR NA PAGINA A PRECISAO
        })
        .catch(error => {
            console.error(error);
        });
    }
        
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

submitInput.addEventListener('change', () => {
    fileType = fileInput.files[0].type
    fileSize = fileInput.files[0].size

    document.getElementById('aviso').innerHTML = ""
    for(let i = 1; i < 4; i++){
        document.getElementById('p' + i).innerHTML = ""
    }
    document.getElementById("imgPreview").src = ""

    if(fileType == 'image/jpeg' || fileType == 'image/png' && fileSize < 15000000){
        document.getElementById("imgPreview").src = URL.createObjectURL(fileInput.files[0])

    }
    else if(fileType != 'image/jpeg' && fileType != 'image/png'){
        document.getElementById('aviso').innerHTML = "Arquivo de tipo inválido"
    }
    else{
        document.getElementById('aviso').innerHTML = "Arquivo excede o tamanho máximo (15MB)"
    }
    
})