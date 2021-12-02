from django.contrib import admin
from apps.actions.models import actionDetection, action, risk

# Register your models here.
admin.site.register(action)
admin.site.register(risk)
admin.site.register(actionDetection)