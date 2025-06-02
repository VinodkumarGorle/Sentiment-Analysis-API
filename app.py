from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/sentiment', methods=['POST'])
def sentiment():
    if not request.is_json or 'input' not in request.json:
        return jsonify({
            "Status": [{"MessageCode": "E", "MessageText": "No 'text' field in JSON"}],
            "ReturnData": [],
            "DevelopedBy": "Vinod Kumar"
        }), 400

    input_text = request.json['input']

    try:
        results = sentiment_pipeline(input_text)
        prediction = results[0]['label']
        score = results[0]['score']

        return jsonify({
            "Status": [{"MessageCode": "S", "MessageText": "OK"}],
            "ReturnData": [{"Sentiment": prediction, "Confidence": round(score, 3)}],
            "DevelopedBy": "Vinod Kumar"
        })

    except Exception as e:
        return jsonify({
            "Status": [{"MessageCode": "E", "MessageText": str(e)}],
            "ReturnData": [],
            "DevelopedBy": "Vinod Kumar"
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
