from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


# A Model serializer allows to interact with the db model
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # The Meta class allows to point to a specific model
    # Here UserProfile
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # The following allows to have extra config/variables
        extra_kwargs = {
            'password': {
                # Make the password write write_only
                # i.e can't be read via the api call
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


    # Let's override the default user create functions
    # given that in that function the password is not encrypted
    def create(self, validated_data):
        """Create and return a new user profile"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # The user profile is a foreign key for the feed so we don't
        # want the value to be editable
        extra_kwargs = {'user_profile': {'read_only': True}}
