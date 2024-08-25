import requests
import json

# emotion_dector -> calls the Watson NLP Library
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=header)

    dict_response = json.loads(response.text)
    emotion_predictions = dict_response['emotionPredictions'][0]['emotion']
    scores = {
        'anger': emotion_predictions['anger'],
        'disgust': emotion_predictions['disgust'],
        'fear': emotion_predictions['fear'],
        'joy': emotion_predictions['joy'],
        'sadness': emotion_predictions['sadness']
    }

    dominant_emotion = max(scores, key=scores.get)
    return {
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': dominant_emotion
    }

# {'emotionPredictions': [
#     {'emotion': 
#     {'anger': 0.0043339236, 
#     'disgust': 0.00037549555, 
#     'fear': 0.0034732423, 
#     'joy': 0.9947189, 
#     'sadness': 0.012704818}, 
#     'target': '', 
#     'emotionMentions': [
#         {'span': {'begin': 0, 'end': 25, 'text': 'I am so happy doing this.'}, 
#         'emotion': {'anger': 0.0043339236, 'disgust': 0.00037549555, 'fear': 0.0034732423, 'joy': 0.9947189, 'sadness': 0.012704818}}]}], 
#         'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}