from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

from .models import *


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    theQuestion = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": theQuestion})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'
class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Pregunta:", max_length=100)
    date = forms.DateTimeField(label="Data:")
    """forms.DateTimeField(label="Data:",
            widget=DateTimePickerInput(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            ))"""

def new_question(request):
    myform = QuestionForm()
    return render(request,"polls/new_question.html",{"form":myform})

def new_question_add(request):
    if request.method=="POST":
        # crear Question
        form = QuestionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["question_text"]
            question = Question(question_text=text)
            #question.pub_date = timezone.now()
            question.pub_date = form.cleaned_data["date"]
            question.save()
            message = "Pregunta enregistrada correctament"
        return render(request,"polls/new_question_add.html",{"message":message})
    # ERROR: retorn a form
    return HttpResponseRedirect(reverse("polls:add_question"))



class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ("votes",)

def new_choice(request):
    form = ChoiceForm()
    if request.method =="POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"polls/new_choice.html",{"form":form})



def dynamic(request):
    return render(request,"polls/dynamic.html")

