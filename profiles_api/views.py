from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import permissions
from profiles_api import serializers
from profiles_api import models


# Create your views here.
# You use API View to add support to the HTTP functions you want to support

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



# A ViewSet allows you to add an API to perform actions
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message with our name"""
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


    def retrieve(self, request, pk=None):
        """Get an object by its ID."""
        return Response({'http_method': 'GET'})


    def update(self, request, pk=None):
        """Update an object"""
        return Response({'http_method': 'PUT'})


    def partial_update(self, request, pk=None):
        """Partial Update an object"""
        return Response({'http_method': 'PATCH'})


    def destroy(self, request, pk=None):
        """Partial Update an object"""
        return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)



class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
