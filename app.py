from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/sentiment', methods=['POST'])
def sentiment():
    if not request.is_json or 'input' not in request.json:
        return jsonify({
            "Status": [{"MessageCode": "E", "MessageText": "Missing 'input' in JSON"}],
            "ReturnData": [],
            "DevelopedBy": "Vinod Kumar"
        }), 400

    input_text = request.json['input']
    try:
        scores = analyzer.polarity_scores(input_text)
        compound = scores['compound']
        sentiment = "POSITIVE" if compound > 0.05 else "NEGATIVE" if compound < -0.05 else "NEUTRAL"

        return jsonify({
            "Status": [{"MessageCode": "S", "MessageText": "OK"}],
            "ReturnData": [{"Sentiment": sentiment, "Confidence": round(abs(compound), 3)}],
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
