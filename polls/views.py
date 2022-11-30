from django.shortcuts import render
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Question
# from django.template import loader
#
#
# # This is the simplest way to call a view for Django application, which would be linked to
# # a URL.
# #
#
#
# def index(request):
#     return HttpResponse("Welcome! You're at the polls index.")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
#
#
# # Adding view which will display the question text with no results but with a form to vote.
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# # This view will display the results for a specific question
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# # The vote view controls the process of voting for a specific option in a specific question.
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
