from django.shortcuts import render, get_object_or_404
from django.urls  import  reverse
from django.http  import  HttpResponse, Http404, HttpResponseRedirect
from django.template  import  loader
from .models import Candidate, Party
# Create your views here.

def index(request):
	latest_party_list = Party.objects.order_by('-party_date_registered')[:5]
	template  = loader.get_template('ballots/index.html')
	output = ', '.join([q.party_name for  q  in latest_party_list])
	context = {
		'latest_party_list' : latest_party_list,
	}
	return render(request, 'ballots/index.html' ,context)
	

def  detail(request, party_id):
	party = get_object_or_404(Party, pk=party_id)
	return render(request, 'ballots/detail.html',{'party': party}) 


def results(request, party_id):
	# response = 'party %s results' 
	# return HttpResponse( response % party_id)
	party = get_object_or_404(Party, pk=party_id)
	return  render(request, 'ballots/results.html',{
		'party': party
		})


def vote_party(request, party_id):
	party  = get_object_or_404(Party, pk=party_id)
	print('Candidate  Post  Request', party.candidate_set.get(pk=request.POST['candidate']))
	try:
		selected_candidate = party.candidate_set.get(pk=request.POST['candidate'])
		print('**&%%^%$$%$')
		print(selected_candidate)
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