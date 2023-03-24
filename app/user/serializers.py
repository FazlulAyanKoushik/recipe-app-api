"""
Serializer for the user API view
"""

from rest_framework import serializers
from django.contrib.auth import (
    get_user_model,
    authenticate
)
from django.utils.translation import gettext as _



class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user objects"""

    # tokens = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
            }
        }

    # def get_tokens(self, obj):
    #     """Method to generate and return access and refresh token"""
    #     refresh = RefreshToken.for_user(obj)
    #
    #     return {
    #         'access': str(refresh.access_token),
    #         'refresh': str(refresh),
    #     }

    def create(self, validated_data):
        """create and return a user with encrypted password"""

        return get_user_model().objects.create_user(**validated_data)
        # user = get_user_model().objects.create_user(**validated_data)
        # refresh = RefreshToken.for_user(user)
        # user.tokens = {
        #     'access': str(refresh.access_token),
        #     'refresh': str(refresh),
        # }
        # return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """validate and authenticate user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs