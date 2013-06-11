# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Poll
from django.contrib.auth import logout, authenticate, login

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def user_login(request):
    if request.method == 'GET':
        return render(request, 'polls/login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'polls/index.html')
            else:
                pass
	        context = {'error_msg': 'Disabled account'}
	        return render(request,'polls/login.html',context)
                # Return a 'disabled account' error message
        else:
            pass
	    context = {'error_msg': 'Invalid login. Try again.'}
	    return render(request,'polls/login.html',context)
            # Return an 'invalid login' error message.

def user_logout(request):
    logout(request)
    return render(request, 'polls/index.html')

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
