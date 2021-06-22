from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function'
            'Is similar to a traditional Django view',
            'Gives you most control over your application Logic',
            'Is mapped manually to urls'
        ]

        return Response({
            'message': 'Hello', 'an_apiview': an_apiview
        })
