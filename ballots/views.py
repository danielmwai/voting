from django.shortcuts import render, get_object_or_404
from django.http  import  HttpResponse, Http404
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
	response = 'party %s results' 
	return HttpResponse( response % party_id)


def vote_party(request, party_id):
	party  = get_object_or_404(Party, pk=party_id)
	print('********')
	print(party)
	try:
		selected_party = party.candidate_set.get(pk=request.POST['party'])
	except (KeyError, Candidate.DoesNotExist):
		# Redisplay the canidate  ballot  form
		return render(request, 'ballots/detail.html', {'party': party ,
			  'error_message': 'You didnt select a  Candidate'})
	else:
		selected_party.votes +=1
		selected_party.save()

		# Always  return  a  HttpResponseRedirect after  successful dealing with Post Data
		# This prevents data  from being  posted twice  if a user hits the  Back Button
		return  HttpResponseRedirect(reverse('ballots:results',
			args=(party.id,)))