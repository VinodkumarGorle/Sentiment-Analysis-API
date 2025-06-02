# Sentiment Analysis API

This is a simple Flask-based sentiment analysis API using the VADER sentiment analysis tool from the `vaderSentiment` library.

## Features

- Accepts POST requests with JSON payloads
- Analyzes sentiment of the input text as POSITIVE, NEGATIVE, or NEUTRAL
- Returns confidence score
- Built with Flask and vaderSentiment

## Endpoint

### POST `/sentiment`

**Request Body:**
```
{
  "input": "Your text here"
}
```

**Response:**
```
{
  "Status": [{"MessageCode": "S", "MessageText": "OK"}],
  "ReturnData": [{"Sentiment": "POSITIVE", "Confidence": 0.823}],
  "DevelopedBy": "Vinod Kumar"
}
```

## Error Handling

- If input is missing or invalid, the API responds with a message code "E" and a message text indicating the error.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/VinodkumarGorle/Sentiment-Analysis-API.git
cd Sentiment-Analysis-API
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Developed By

**Vinod Kumar**
