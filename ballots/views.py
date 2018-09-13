from django.shortcuts import render, get_object_or_404
from django.urls  import  reverse
from django.http  import HttpResponseRedirect
from  django.views import generic
from .models import Candidate, Party
# Create your views here.

class IndexView(generic.ListView):
	template_name = 'ballots/index.html'
	context_object_name = 'latest_party_list' 
	def get_queryset(self):
		"""
		Return last five  published questions
		"""
		return Party.objects.order_by('-party_date_registered')[:5]
	

class  DetailView(generic.DetailView):
	model = Party
	template_name = 'ballots/detail.html'


class ResultsView(generic.DetailView):
	model = Party
	template_name = 'ballots/results.html'
	

def vote(request, party_id):
	party  = get_object_or_404(Party, pk=party_id)
	try:
		selected_candidate = party.candidate_set.get(pk=request.POST['candidate'])
	except (KeyError, Candidate.DoesNotExist):
		# Redisplay the canidate  ballot  form
		return render(request, 'ballots/detail.html', {'party': party ,
			  'error_message': 'You didnt select a  Candidate'})
	else:
		selected_candidate.votes +=1
		selected_candidate.save()

		# Always  return  a  HttpResponseRedirect after  successful dealing with Post Data
		# This prevents data  from being  posted twice  if a user hits the  Back Button
		return  HttpResponseRedirect(reverse('ballots:results',
			args=(party.id,)))