from django.http import JsonResponse
from polls.models import *
from django.contrib.auth.decorators import login_required


def get_questions(request):
    jsonData = list( Question.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "questions": jsonData,
        }, safe=False)

@login_required
def get_choices(request,question_id):
    print(request.user)
    jsonData = list( Choice.objects.filter(question__id=question_id).values() )
    return JsonResponse({
            "status": "OK",
            "choices": jsonData,
        }, safe=False)

