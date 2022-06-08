from typing import Dict, Any

from django.views.generic import DetailView
from .models import Course
from loguru import logger


class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    http_method_names = ['get']

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        logger.debug(context)
        return context