from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import SentimentSerializer
from .utils import getSentimentResult


class SentimentAnalyzeView(generics.GenericAPIView):
    serializer_class = SentimentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            text = request.data['text']
            sentiment = getSentimentResult(text)
        except KeyError:
            return Response(
                {
                    'status': 'fail',
                    'messsage': 'Invalid key',
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except ValueError:
            return Response(
                {
                    'status': 'fail',
                    'message': 'Sentiment not found',
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        if serializer.is_valid():
            try:
                serializer.save(text=text, sentiment=sentiment)
            except:
                return Response(
                    {
                        'status': 'fail',
                        'message': 'Unable to create sentiment'
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
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
