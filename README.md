# Sentiment Analysis API

This API accepts a text input and returns the sentiment analysis result using a pre-trained ML model.

## Used Pre Trained Model:

[https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis)

### Installation:

- Transformers:

```bash
pip install transformers
```

- Transformers and Pytorch:

```bash
pip install 'transformers[torch]'
```

- Transformers and Flax:

```bash
pip install 'transformers[flax]'
```

### Usage:

```Python
from transformers import pipeline

model = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
pred = model('I am happy today!')
```

```Python
print(pred)
>> [{'label': 'POS','score': 0.99250328540802}]
```

---

## Endpoint:

| Method | URL            | Description                                                                  |
| :----- | :------------- | :--------------------------------------------------------------------------- |
| POST   | `/api/analyze` | Return the sentiment result of the request text as positive/neutral/negative |

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
	"data": {
		"text": "I am so happy!",
		"sentiment": "positive"
	}
}
```

## Project Setup:

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Make Migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### Run server:

```bash
python manage.py runserver
```

### Test the API:

```
http://127.0.0.1:8000/api/analyze/
```

## Project Structure:

```
.
├── api                 # main app for sentiment API
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py			  # pre-trained model used here
│   └── views.py
├── manage.py
└── sentiment_analysis  # root directory of the project
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
