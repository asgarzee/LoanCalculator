from rest_framework import serializers


class LoanQuotesSerializer(serializers.Serializer):
    loan_amount = serializers.DecimalField(required=True, decimal_places=2, max_digits=12)
    no_of_payments = serializers.IntegerField(required=False, min_value=1)
    monthly_repayment_amount = serializers.DecimalField(required=False, decimal_places=2, max_digits=12)

    def validate(self, attrs):
        if not attrs.get('no_of_payments') and not attrs.get('monthly_repayment_amount'):
            raise serializers.ValidationError(
                "At least one of the field between no_of_payments and monthly_repayment_amount is required")
        return attrs
