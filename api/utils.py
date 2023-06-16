from transformers import pipeline


def getSentimentResult(text) -> str:
    model = pipeline("sentiment-analysis",
                     model="finiteautomata/bertweet-base-sentiment-analysis")

    prediction = model(text)[0]
    result = ""
    if prediction["label"] == "POS":
        result = "Positive"
    elif prediction['label'] == "NEG":
        result = "Negative"
    else:
        result = "Neutral"
    return result
