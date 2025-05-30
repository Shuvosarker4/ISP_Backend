
from django.urls import path
from dashboard.views import DashboardSummaryView,ExpenseSummaryView

urlpatterns = [
    path('summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
    path('expense-summary/', ExpenseSummaryView.as_view(), name='expense-summary'),
]
