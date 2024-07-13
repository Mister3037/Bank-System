from rest_framework import serializers

from .models import *


# Branch Data Serializer
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"
        

# Bank Data Serializer
class BankSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    class Meta:
        model = Bank
        fields = "__all__"
        

# Client Data Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        
        
# Account Data Serializer
class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = BankSerializer()
    class Meta:
        model = Account
        fields = "__all__"
        

# Account Detail Data Serializer
class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["client", "bank", "balance"]


# Transfer Data Serializer
class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')


# Withdraw Data Serializer
class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')


# Deposit Data Serializer
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')
        