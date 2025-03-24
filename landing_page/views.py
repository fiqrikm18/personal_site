from django.views.generic import TemplateView
from system_details.models import WorkingExperience


# Create your views here.
class LandingPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_experiences'] = WorkingExperience.objects.order_by('-id').all()

        return context
