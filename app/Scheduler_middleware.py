from django.shortcuts import get_object_or_404
from django.utils.deprecation import MiddlewareMixin
from .models import *
from datetime import datetime


class ScheduleHandler(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        now = datetime.now()
        exp_time = ExpireTime.objects.filter(exp_time__lte=now)
        for i in exp_time:
            data = get_object_or_404(UploadFileModel, pk=i.file.id)
            data.delete()
        return None
