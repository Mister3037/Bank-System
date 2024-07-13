from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# Branch Data APIView with (GET, POST) methods
class BranchAPIView(APIView):
    def get(self, request):
        branch = Branch.objects.all()
        serializers = BranchSerializer(branch, many=True).data
        
        return Response(
            {
                "status": True,
                "data": serializers
            }
        )
    
    def post(self, request):
        serializers = BranchSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
        else:
            return Response(
                {
                    "status": False,
                    "message": serializers.errors
                }
            )
        return Response(
            {
                "status": True,
                "data": serializers.data
            }
        )
        

# Branch Detail APIView with (GET, PUT, DELETE) methods
class BranchDetailAPIView(APIView):
    def get(self, request, pk):
        branch = Branch.objects.get(id=pk)
        serializers = BranchSerializer(branch).data
        
        return Response(
            {
                "status": True,
                "data": serializers
            }
        )
    
    def put(self, request, pk):
        branch = Branch.objects.get(id=pk)
        serializers = BranchSerializer(branch, data=request.data, partial=True)
        
        if serializers.is_valid():
            serializers.save()
        else:
            return Response(
                {
                    "status": False,
                    "message": serializers.errors
                }
            )
            
        return Response(
            {
                "status": True,
                "data": serializers.data
            }
        )
    
    def delete(self, request, pk):
        branch = Branch.objects.get(id=pk)
        branch.delete()
        
        return Response(
            {
                "status": True,
                "message": "Ma'lumot muvaffaqiyatli o'chirildi!"
            }
        )


# Bank Data APIView with (GET, POST)

class BanksAPIView(APIView):
    def get(self, request):
        try:
            
            banks = Bank.objects.all()
            serializers = BankSerializer(banks, many=True).data
            
            return Response(
                {
                    "status": True,
                    "data": serializers
                }
            )
       
        except Bank.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "Ma'lumot topilmadi!"
                }
            )
    
    def post(self, request):
        serializers = BankSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
        else:
            return Response(
                {
                    "status": False,
                    "message": serializers.errors
                }
            )
        return Response(
            {
                "status": True,
                "data": serializers.data
            }
        )
        

# Bank Detail APIView with (GET, PUT, DELETE)

class BankDetailAPIView(APIView):
    
    def get(self, request, pk):
        try:
            bank = Bank.objects.get(id=pk)
            serializers = BankSerializer(bank)
            
            return Response(
                {
                    "status": True,
                    "data": serializers.data
                }
            )
        except Bank.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "Bank nomi topilmadi"
                }
            )
    
    def put(self, request, pk):
        bank = Bank.objects.get(id=pk)
        serializers = BankSerializer(bank, data=request.data, partial=True)
        
        if serializers.is_valid():
            serializers.save()
        else:
            return Response(
                {
                    "status": False,
                    "message": serializers.errors
                }
            )
        
        return Response(
            {
                "status": True,
                "data": serializers.data
            }
        )
        
    def delete(self, request, pk):
        bank = Bank.objects.get(id=pk)
        bank.delete()
        return Response(
            {
                "status": True,
                "message": "Ma'lumot muvaffaqiyatli o'chirilidi!"
            }
        )
        
        
# Account Create APIView, (POST) 
class CreateAccountAPIView(APIView):
    def post(self, request):
        client = Client.objects.create(
            name = request.data["name"],
            address = request.data["address"]
        )
        bank = Bank.objects.get(id=request.data["bank"])
        account = Account.objects.create(
            client = client,
            open_date = request.data["open_date"],
            account_type = request.data["account_type"],
            bank = bank
        )
        serializers = AccountSerializer(account)
        return Response(
            {
                "status": True,
                "data": serializers.data
            }, status=status.HTTP_201_CREATED
        )


# Accounts Lists APIView
class AccountsAPIView(APIView):
    def get(self, request):
        try:
            accounts = Account.objects.all()
            serializers = AccountSerializer(accounts, many=True)
            
            return Response(
                {
                    "status": True,
                    "data": serializers.data
                }
            )
        except Account.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "Account topilmadi!"
                }
            )


# Account Detail APIView (GET)

class AccountDetailAPIView(APIView):
    def get(self, request, pk):
        account = Account.objects.get(id=pk)
        serializers = AccountDetailSerializer(account).data  
        return Response(serializers)    
    

# Deposit List Create APIView (GET, POST)
class DepositAPIView(APIView):
    def get(self, request):
        try:
            deposits = Deposit.objects.all()
            serializers = DepositSerializer(deposits, many=True)
            return Response(
                {
                    "status": True,
                    "data": serializers.data
                }
            )
        except Deposit.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "Ma'lumot topilmadi!"
                }
            )
    
    def post(self, request):
        serializers = DepositSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
        else:
            return Response(serializers.errors)
        return Response(serializers.data)
            
            
# Deposit List Create APIView (GET, POST)
class WithdrawAPIView(APIView):
    def get(self, request):
        try:
            withdraws = Withdraw.objects.all()
            serializers = WithdrawSerializer(withdraws, many=True)
            return Response(
                {
                    "status": True,
                    "data": serializers.data
                }
            )
        except Withdraw.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "Ma'lumot topilmadi!"
                }
            )
   
    def post(self, request):
        serializers = WithdrawSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        else:
            return Response(serializers.errors)
        return Response(serializers.data)
            
    
        