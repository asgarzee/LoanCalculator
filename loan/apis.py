from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from loan.serializers import LoanQuotesSerializer
from loan.utils import Loan, custom_response


class LoanCalculatorView(APIView):
    """
    View to get the quotes.
    """

    def post(self, request, *args, **kwargs):
        """
        Return a list of loan response.
        """
        print(request.data)
        data = request.data
        serializer = LoanQuotesSerializer(data=data)
        if serializer.is_valid():
            loan_obj = Loan(float(serializer.data.get('loan_amount')))
            if (no_of_payment := serializer.data.get('no_of_payments')) and (
                    monthly_repayment_amount := serializer.data.get('monthly_repayment_amount')):
                if loan_obj.is_interest_high(no_of_payments=no_of_payment,
                                             monthly_repayment_amount=monthly_repayment_amount):
                    return Response(
                        custom_response(data={"is_interest_higher": True},
                                        msg="Interest is higher than pre-configured threshold"),
                        status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        custom_response(data={"is_interest_higher": False},
                                        msg="Interest is lower than pre-configured  threshold"),
                        status=status.HTTP_200_OK
                    )
            elif no_of_payment := serializer.data.get('no_of_payments'):
                month_pay = loan_obj.get_monthly_repayment_amount(no_of_payment)
                return Response(
                    custom_response(data={"result": month_pay},
                                    msg="Monthly Repayment: "),
                    status=status.HTTP_200_OK
                )
            else:
                no_of_payment = loan_obj.get_no_of_payments(serializer.data.get('monthly_repayment_amount'))
                return Response(
                    custom_response(data={"result": no_of_payment},
                                    msg="Number of payments: "),
                    status=status.HTTP_200_OK
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
