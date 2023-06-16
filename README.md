# Sentiment Analysis API

This API accepts a text input and returns the sentiment analysis result using a pre-trained ML model.

## Used Pre Trained Model:

[https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis)

### Installation:

- Transformers:

```
pip install transformers
```

- Transformers and Pytorch:

```
pip install 'transformers[torch]'
```

- Transformers and Flax:

```
pip install 'transformers[flax]'
```

### Usage:

```Python
from transformers import pipeline

model = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
pred = model('I am happy today!')
```

---

## Endpoint:

| Method | URL            | Description                                                                  |
| :----- | :------------- | :--------------------------------------------------------------------------- |
| POST   | `/api/analyze` | Return the sentiment result of the request text as Positive/Neutral/Negative |

## Example:

### Request:

```json
{
	"text": "I am so happy!"
}
```

### Response:

```json
{
	"status": "success",
	"response": {
		"text": "I am so happy!",
		"sentiment": "positive"
	}
}
```

## Project Setup:

### Install Dependencies:

```
pip install -r requirements.txt
```

### Make Migrations:

```
python manage.py makemigrations
python manage.py migrate
```

### Run server:

```
python manage.py runserver
```

### Test the API:

```
http://127.0.0.1:8000/api/analyze/
```
