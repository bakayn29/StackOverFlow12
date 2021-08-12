from rest_framework import serializers

from account.models import CustomUser
from account.utils import send_activation_code


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password',
                  'password_confirmation')

    def validate(self, attrs):
        password = attrs.get('password')
        password_conf = attrs.pop('password_confirmation')
        if password != password_conf:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user

