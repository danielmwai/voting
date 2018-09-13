from django.contrib import admin

# Register your models here.
from.models import  Party, Candidate

admin.site.register(Party)
admin.site.register(Candidate)