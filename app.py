from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
sentiment_pipeline = pipeline("sentiment-analysis")

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
        results = sentiment_pipeline(input_text)
        response = []

        for res in results:
            response.append({
                "Sentiment": res["label"],
                "Confidence": round(res["score"], 3)
            })

        return jsonify({
            "Status": [{"MessageCode": "S", "MessageText": "OK"}],
            "ReturnData": response,
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
