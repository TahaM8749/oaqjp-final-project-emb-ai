from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import requests
import json

app = Flask("Emotion Detector")

@app.route("\emotionDetector", methods=['POST'])
def detect_emotion():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    analysis = emotion_detector(text)
    if "error" in analysis:
        return jsonify(analysis), 500 

    # Format the response as specified
    response_str = (
        f"For the given statment, the system response is 'anger': {analysis['anger']}, "
        f"'disgust': {analysis['disgust']}, 'fear': {analysis['fear']}, 'joy': {analysis['joy']} "
        f"and 'sadness': {analysis['sadness']}. The dominant emotion is {analysis['dominant_emotion']}."
    )
    return (response_str, 200)
text = request.json.get("text", "")
    if not text or request.staus_code == 400:
        return jsonify({"error": "Invalid text! Please try again"}), 400

    analysis = emotion_detector(text)
    if "error" in analysis:
        return jsonify(analysis), 500 

    # Format the response as specified
    response_str = (
        f"system response for this statement is 'anger': {analysis['anger']}, "
        f"'disgust': {analysis['disgust']}, 'fear': {analysis['fear']}, 'joy': {analysis['joy']} "
        f"and 'sadness': {analysis['sadness']}. The dominant emotion is {analysis['dominant_emotion']}."
    )
    return (response_str, 200)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)