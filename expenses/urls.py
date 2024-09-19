from django.urls import path
from expenses.api.views import ( ExpenseListCreateView, 
																ExpenseDetailView ,
																PastWeekExpensesView, 
																PastMonthExpensesView, 
																Past3MonthsExpensesView,
																CustomExpensesView ,
																UserRegistrationView ) 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
		path('expenses/past-week/', PastWeekExpensesView.as_view(), name='past-week-expenses'),
		path('expenses/past-month/', PastMonthExpensesView.as_view(), name='past-month-expenses'),
		path('expenses/past-3-months/', Past3MonthsExpensesView.as_view(), name='past-3-months-expenses'),
		path('expenses/custom/', CustomExpensesView.as_view(), name='custom-expenses'),
		path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
		path('register/', UserRegistrationView.as_view(), name='user-register'),
]