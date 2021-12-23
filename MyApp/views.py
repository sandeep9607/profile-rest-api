from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from MyApp import serializers


class HelloAPIView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIs features"""
        an_apiview = [
            'Uses HTTP menthods a function (get, post, patch)',
            'Is similar to a traditional Django View',
            'Gives you most control over application logic',
            "Is mapped manually to URLs",
        ]

        return Response({'message': 'Hello!','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'meethod':'PUT'})

    def  patch(self, request, pk=None):
        """Handle updating partial object"""
        return Response({'method':'PATCH'})



    def  delete(self, request, pk=None):
        """Handle updating partial object"""
        return Response({'method':'DELETE'})
