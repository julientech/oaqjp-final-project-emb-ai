"""Flask web server for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Render the homepage with input form."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detection_route():
    """Handle emotion detection and format the response."""
    if request.method == "POST":
        text_to_analyze = request.form["textToAnalyze"]
    else:
        text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_result = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_result

if __name__ == "__main__":
    app.run(debug=True)
