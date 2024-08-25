"""
server.py

This file sets up the localserver with Flask for the emotion detection 
integrated with the Watson AI algorithm.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

def run_emotion_detection():
    """
    Starts the Flask web application on port 5000.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/")
def render_index_page():
    """
    Renders the index.html page for the Emotion Detection application.
    Returns: str: The HTML template for the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """
    Passes the inputted argument text into the algorithm.
    Returns: str: A string describing the emotion scores and the dominant emotion.
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {response['anger']} "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    run_emotion_detection()
