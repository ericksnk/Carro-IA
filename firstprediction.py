from imageai.Classification.Custom import ClassificationModelTrainer
from imageai.Classification.Custom import CustomImageClassification
import os

execution_path = os.getcwd()

#model_trainer = ClassificationModelTrainer()
#model_trainer.setModelTypeAsDenseNet121()
#model_trainer.setDataDirectory("BancoDeImagens")
#model_trainer.trainModel(num_experiments=5, batch_size=20)

prediction = CustomImageClassification()
prediction.setModelTypeAsDenseNet121()
prediction.setModelPath(os.path.join(execution_path, "BancoDeImagens/models/densenet121-BancoDeImagens-test_acc_0.64667_epoch-4.pt"))
prediction.setJsonPath(os.path.join(execution_path, "BancoDeImagens/models/BancoDeImagens_model_classes.json"))
prediction.loadModel() 

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "imagens/carro.jpg"), result_count=3 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)