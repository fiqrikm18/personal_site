from django.views.generic import TemplateView
from django.http import JsonResponse
from system_details.models import WorkingExperience, SkillSet, Portfolio, PortfolioImages
from enum import Enum

from django.db.models.functions import JSONObject
from django.contrib.postgres.expressions import ArraySubquery


class ResponseMessage(Enum):
    SUCCESS = "Success"
    FAILED = "Failed"


class LandingPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["work_experiences"] = WorkingExperience.objects.order_by("-id").all()
        context["skill_sets"] = SkillSet.objects.order_by("-id").all()
        context["portfolios"] = Portfolio.objects.select_related().order_by("-id").all()
        return context


def get_portfolio_detail(request, pk):
    response = {"code": 200, "message": ResponseMessage.SUCCESS.value, "data": []}

    portfolio_images = PortfolioImages.objects.filter(portfolio=pk).values(json=JSONObject(
        image='file'
    )).values_list('file', flat=True)

    portfolio = Portfolio.objects.annotate(images=ArraySubquery(portfolio_images)).filter(pk=pk).values().first()
    if not portfolio:
        response["code"] = 404
        response["message"] = ResponseMessage.FAILED.value
        return JsonResponse(response, status=404)

    response["data"] = portfolio
    return JsonResponse(response, status=200)
