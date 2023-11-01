from imageai.Classification import ImageClassification
import os

image_path = os.getcwd() + "\images"
execution_path = os.getcwd() + "\IA"

prediction = ImageClassification()
prediction.setModelTypeAsDenseNet121()
prediction.setModelPath(os.path.join(execution_path, "densenet121-a639ec97.pth"))
prediction.loadModel()

def previsao(image_name):
    text = []
    predictions, probabilities = prediction.classifyImage(os.path.join(image_path, image_name), result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        text.append(str(eachPrediction) + " : " + str(eachProbability))
        #print(eachPrediction , " : " , eachProbability)
    return text