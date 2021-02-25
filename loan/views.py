from django.views.generic import TemplateView


class LoanView(TemplateView):
    template_name = "loan/index.html"
