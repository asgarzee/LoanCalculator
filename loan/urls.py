from django.urls import path

from .apis import LoanCalculatorView
from .views import LoanView

urlpatterns = [
    path('', LoanView.as_view()),
    path('get-quote/', LoanCalculatorView.as_view()),
]
