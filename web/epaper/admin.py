# epaper/admin.py

from django.contrib import admin

# Register your models here.
from epaper.models import EPaperEmail

admin.site.register(EPaperEmail)