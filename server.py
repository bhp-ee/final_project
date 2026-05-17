from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    """
    Route to handle emotion detection requests.
    Retrieves text from the request arguments, processes it using the 
    EmotionDetection package, and returns a formatted response string.
    """
    # Retrieve the text to analyze from the request query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_detector function
    response = emotion_detector(text_to_analyze)
    
    # Handle case where the input text is blank or invalid
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."
    
    # Format the output string exactly as required by the frontend application
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is **{response['dominant_emotion']}**."
    )

@app.route("/")
def render_index_page():
    """
    Route to render the main application page (HTML UI).
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application on localhost at port 5000
    app.run(host="0.0.0.0", port=5000)