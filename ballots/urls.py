from django.urls  import  path

from . import  views

app_name =  'ballots'
urlpatterns = [
		path('', views.index, name='index'),
		path('specifics/<int:party_id>/', views.detail, name='detail'),
		path('<int:party_id>/results/', views.results, name='results'),
		path('<int:party_id>/vote/', views.vote_party, name='vote'),
]