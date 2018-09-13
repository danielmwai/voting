from django.contrib import admin

# Register your models here.
from.models import  Party, Candidate

class  PartyAdmin(admin.ModelAdmin):
	fields = ['party_name', 'party_registered_no', 'party_date_registered',]

class CandidateAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['candidate', ]}),
	('Candidate Info', {'fields': ['party','date_registered', 'votes']}),
	]



admin.site.register(Party, PartyAdmin)
admin.site.register(Candidate, CandidateAdmin)