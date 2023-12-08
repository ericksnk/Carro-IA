from imageai.Classification.Custom import ClassificationModelTrainer
from imageai.Classification.Custom import CustomImageClassification
import os

image_path = os.getcwd() + "\images"
execution_path = os.getcwd() + "\IA\BancoDeImagens\models"

model = "densenet121-BancoDeImagens-test_acc_0.87747_epoch-3.pt"
json_model = "BancoDeImagens_model_classes.json"

prediction = CustomImageClassification()
prediction.setModelTypeAsDenseNet121()
prediction.setModelPath(os.path.join(execution_path, model))
prediction.setJsonPath(os.path.join(execution_path, json_model))
prediction.loadModel() 

def previsao(image_name):
    text = []

    try:
        predictions, probabilities = prediction.classifyImage(os.path.join(image_path, image_name), result_count=3 )
    except:
        return -1
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        predict = str(eachPrediction)
        probability = str(round(eachProbability, 2))
        if predict == 'NemCarroNemCachorro' :
            predict = 'Nenhum dos dois'
        text.append(predict + " : " + probability)

    return text