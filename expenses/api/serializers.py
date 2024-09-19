from rest_framework import serializers
from expenses.models import Expense
from django.contrib.auth.models import User

class ExpenseSerializer(serializers.ModelSerializer):

    read_only_fields = ('created_at',)

    class Meta:
        model = Expense
        fields = '__all__'
    


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in response

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Create the user and hash the password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user