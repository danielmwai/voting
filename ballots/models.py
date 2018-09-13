from django.db import models
from django.utils import timezone

# Create your models here.

class Party(models.Model):
	party_name  = models.CharField(max_length=250)
	party_date_registered = models.DateTimeField('party date registered',default=timezone.now)
	party_registered_no  = models.PositiveIntegerField()

	def  __str__(self):
		return  self.party_name

	class Meta:
		ordering = ('party_name',)


class  Candidate(models.Model):
	candidate = models.CharField(max_length=200)
	date_registered = models.DateTimeField('date registered')
	party = models.ForeignKey(Party, on_delete=models.CASCADE, default=1)
	votes  =  models.PositiveIntegerField(default=0)

	def  __str__(self):
		return self.candidate

	def  was_registered_recently(self):
		return  self.date_registered >= timezone.now -datetime.timedelta(days=1)

	class Meta:
		ordering = ('date_registered',)

