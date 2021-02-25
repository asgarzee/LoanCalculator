import math


class Loan(object):
    """
    Class to handle Loan calculations
    """
    INTEREST_RATE = 0.06  # Preconfigured interest rate

    def __init__(self, loan_amount):
        self.loan_amount = float(loan_amount)
        self.rate = self.INTEREST_RATE / 12

    def get_no_of_payments(self, monthly_repayment_amount: float) -> int:
        """
        Calculate the number of monthly payments
        :param monthly_repayment_amount:
        :return: no of payments
        """
        temp = 1 + (self.rate * self.loan_amount / float(monthly_repayment_amount))
        num = (math.log(temp) / math.log(1 + self.rate))
        return math.ceil(num)

    def get_monthly_repayment_amount(self, no_of_payments: int) -> float:
        """
        Calculates the monthly repayment amount
        :param no_of_payments:
        :return: monthly repayment amount
        """
        no_of_payments = int(no_of_payments)
        month_pay = (self.loan_amount * self.rate * math.pow(1 + self.rate, no_of_payments)) / (math.pow(1 + self.rate,
                                                                                                         no_of_payments) - 1)
        return month_pay

    def is_interest_high(self, no_of_payments: int, monthly_repayment_amount: float) -> bool:
        """
        Returns if interest calculated iss higher than pre-configured or not.
        :param no_of_payments:
        :param monthly_repayment_amount:
        :return:
        """
        no_of_payments = float(no_of_payments)
        monthly_repayment_amount = float(monthly_repayment_amount)
        q = math.log(1 + (1 / no_of_payments)) / math.log(2)
        interest_rate = math.pow(math.pow((1 + (monthly_repayment_amount / self.loan_amount)), 1 / q) - 1, q - 1)
        return self.INTEREST_RATE < interest_rate


def custom_response(data, msg="success", success=True):
    """
    To Generated custom API response
    :param data:
    :param msg:
    :param success:
    :return:
    """
    return {"data": data, "msg": msg, "success": success}
