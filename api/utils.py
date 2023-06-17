from transformers import pipeline


def getSentimentResult(text) -> str:
    model = pipeline("sentiment-analysis",
                     model="finiteautomata/bertweet-base-sentiment-analysis")
    prediction = model(text)[0]
    label = prediction['label']
    sentiment_result = 'positive' if label == 'POS' else 'negative' if label == 'NEG' else 'neutral'
    return sentiment_result
