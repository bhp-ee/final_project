import requests
import json

def emotion_detector(text_to_analyze):
    

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers=headers, json=input_json)

    data = json.loads(response.text)
    emotions = data['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)

    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    result = print(json.dumps(output,indent=4))

    return result