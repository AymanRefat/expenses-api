from rest_framework import generics
from expenses.models import Expense
from .serializers import ExpenseSerializer
from datetime import timedelta
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.db.models import Sum

class ExpensesGetView(generics.ListAPIView):
		queryset = Expense.objects.all()
		serializer_class = ExpenseSerializer
		permission_classes = [IsAuthenticated]

		def get(self , request , *args , **kwargs): 
				expenses = self.get_queryset()
				serializer = ExpenseSerializer(expenses, many=True)
				total_count = expenses.count()

				total_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
				# Create the custom response data
				response_data = {
						'total_expenses_count': total_count,    # Total number of expenses
						'total_amount_spent': total_amount,     # Total amount spent
						'expenses': serializer.data             # The list of expenses
				}

				return Response(response_data)


class ExpenseListCreateView(ExpensesGetView , generics.ListCreateAPIView):
		queryset = Expense.objects.all()
		serializer_class = ExpenseSerializer
		permission_classes = [IsAuthenticated]

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
		queryset = Expense.objects.all()
		serializer_class = ExpenseSerializer
		permission_classes = [IsAuthenticated]

class PastWeekExpensesView(ExpensesGetView ):
		def get_queryset(self):
				return Expense.objects.filter(date__gte=timezone.now() - timedelta(days=7))

class PastMonthExpensesView(ExpensesGetView ,  generics.ListAPIView):
		def get_queryset(self):
				return Expense.objects.filter(date__gte=timezone.now() - timedelta(days=30))


class Past3MonthsExpensesView(ExpensesGetView ,  generics.ListAPIView):
		def get_queryset(self):
				return Expense.objects.filter(date__gte=timezone.now() - timedelta(days=90))


class CustomExpensesView(ExpensesGetView ,  generics.ListAPIView):
		def get_queryset(self):
				start_date = self.request.GET.get('start_date')
				end_date = self.request.GET.get('end_date')
				return Expense.objects.filter(date__gte=start_date, date__lte=end_date)


class UserRegistrationView(generics.CreateAPIView):
		serializer_class = UserSerializer

		def create(self, request, *args, **kwargs):
				serializer = self.get_serializer(data=request.data)
				if serializer.is_valid():
						serializer.save()
						return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)