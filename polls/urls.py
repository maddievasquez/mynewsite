from django.urls import path

from . import views

''''
The views detail, results, and vote are now linked to this urls using these paths.
If we access this paths through the browser it would link us to that specific view following that pattern.
'''
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/4/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/4/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
