from rest_framework import serializers

from apps.users.models import User 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id',  'username', 'first_name', 
                  'last_name', 'email', 'profile_image', 'bio')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, write_only=True
    )
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
                  'last_name', 'email', 'bio', 'password', 'password2')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password' : 'Пароли отличаются'})
        return attrs

    def create(self, values):
        user = User.objects.create(
            username=values['username'], first_name=values['first_name'],
            last_name=values['last_name'], email=values['email'], bio=values['bio']
        )
        user.set_password(values['password'])
        user.save()
        return user