from django.urls import path

from . import views

''''
The views detail, results, and vote are now linked to this urls using these paths.
If we access this paths through the browser it would link us to that specific view following that pattern.
'''
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
