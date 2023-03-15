from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, write_only=True)
    cash_account = serializers.DecimalField(max_digits=11, decimal_places=2, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation', 'inn', 'cash_account')

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('User already exists!')
        return username

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Passwords don\'t match!')
        return validated_data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'inn', 'cash_account')

class TransactionSerializer(serializers.Serializer):
    for_users = serializers.ListSerializer(child=serializers.CharField())
    from_user = serializers.CharField()
    cash_amount = serializers.DecimalField(max_digits=11, decimal_places=2)

    def validate_for_users(self, for_users):
        users = User.objects.all()
        for user in for_users:
            user_exists = users.filter(inn=user)
            if not user_exists.exists():
                raise serializers.ValidationError(f'Recipient with INN: {user}, not found!')
        return for_users
    
    def validate_from_user(self, from_user):
        user = User.objects.filter(inn=from_user)
        if not user.exists():
            raise serializers.ValidationError(f'Sender with INN: {user}, not found!')
        return from_user

    def validate(self, validated_data):
        recipient_users = validated_data.get('for_users')
        sender_user_inn = validated_data.get('from_user')
        cash_amount = validated_data.get('cash_amount')
        users = User.objects.all()
        sender_user = users.get(inn=sender_user_inn)
        if(sender_user.cash_account < cash_amount):
            raise serializers.ValidationError('Sender has no cash for this operation!')
        cash_for_recipient = round(cash_amount / len(recipient_users), 2)
        for recipient in recipient_users:
            recipient_user = users.get(inn=recipient)
            recipient_user.cash_account += cash_for_recipient
            recipient_user.save()
        sender_user.cash_account -= cash_amount
        sender_user.save()
        return sender_user
