from django.shortcuts import render

from .forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .tasks import sleepy


class ReviewEmailView(FormView):
    template_name = 'myapp/review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = 'get out of here now'
        return HttpResponse(msg)


def index(request):
    sleepy.delay(5)
    return HttpResponse('<h1>This task has been completed...<h1/>')
