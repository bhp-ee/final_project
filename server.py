from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector # Imported function

app = Flask(__name__)

@app.route("/emotionDetector")
def server_emotion_detector():  # <-- CHANGED THIS NAME to avoid conflict
    # Retrieve text from the query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    
    # This now correctly calls the imported package function!
    response = emotion_detector(text_to_analyze)
    
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."
    
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)