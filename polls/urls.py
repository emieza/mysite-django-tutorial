from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # forms
    path("new_question/", views.new_question, name="new_question"),
    path("new_question_add/", views.new_question_add, name="new_question_add"),
    path("new_choice/", views.new_choice, name="new_choice"),

    # dynamic forms
    path("dynamic/", views.dynamic, name="dynamic"),

]
