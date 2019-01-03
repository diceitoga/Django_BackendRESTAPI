from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user.
           When deserializing data, you always need to call is_valid()
           before attempting to access the validated data, or save an object instance.
           If any validation errors occur, the .errors property will
           contain a dictionary representing the resulting error messages
        """

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
            #serializer.errors   ##this is if serializers.is_valid() is 'False'
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
class ProfilesFeedItemSerializer(serializers.ModelSerializer):
    '''
    A serializer for profile feed items.
    '''
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
