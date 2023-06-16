# Sentiment Analysis API

This API accepts a text input and returns the sentiment analysis result using a pre-trained ML model.

## Used Model:

[https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis)

## Endpoint:

| Method | URL            | Description                                     |
| :----- | :------------- | :---------------------------------------------- |
| POST   | `/api/analyze` | Return the sentiment result of the request text |

## Example:

#### Request:

```json
{
	"text": "I am so happy!"
}
```

#### Response:

```json
{
	"status": "success",
	"data": {
		"text": "I am so happy!",
		"sentiment": "Positive"
	}
}
```
