from django.contrib import admin
from .models import *

model_list = [Reminder, Project, Category, Task]
admin.site.register(model_list)