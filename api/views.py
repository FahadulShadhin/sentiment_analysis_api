from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import SentimentSerializer
from .utils import getSentimentResult


class SentimentAnalyzeView(generics.GenericAPIView):
    serializer_class = SentimentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        text = request.data['text']
        sentiment = getSentimentResult(text)

        if serializer.is_valid():
            serializer.save(text=text, sentiment=sentiment)
            return Response(
                {
                    'status': 'success',
                    'data': {
                        'text': text,
                        'sentiment': sentiment
                    }
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    'status': 'fail',
                    'message': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
