import logging
logger = logging.getLogger('main')

from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .form import Feedbackform
from .models import Lesson, Task, Feedback
logger.debug("main started")
# Create your views here.
def show_index(request):
    logger.info("index showed")
    return render(request, "main/index.html")

def show_schedule(request):
    lessons = Lesson.objects.all()
    logger.info("schedule showed")
    return render(request, "main/schedule.html", {'lessons':lessons})

def show_about(request):
    logger.info("about showed")
    return render(request, "main/about.html")

def show_feedback(request):
    feedbacks = Feedback.objects.all()
    logger.info("feedback showed")
    return render(request, "main/feedback.html", {'feedbacks':feedbacks})

def show_homework(request):
    tasks = Task.objects.order_by('id')
    logger.info("homework showed")
    return render(request, "main/homework.html",{'tasks':tasks})

def feedback_create(request):
    if request.method == 'POST':
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            logger.info("feedback created")
            return redirect('home_student')
        else:
            logger.warning("feedback form is not valid")
    try:
        form = Feedbackform()
        data = {
            'form': form
        }
    except:
        logger.error("error with a creation form")

    return render(request, "main/feedback_create.html", data)