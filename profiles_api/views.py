from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status

from profiles_api import serializers


# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    #function that will return the API results
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditioanl djagno view',
            'Gives you the most control over your app logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        # Let's check that the data is valid as per our seraliser validation function
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                #Here we are customising the http response send. By default: 200
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handles a full update of an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
