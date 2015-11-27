from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email, ValidationError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from photoapp.models import FacebookUser
from django.http import Http404




def custom_404(request):
    return render(request, 'bucketlist/404.html')

def custom_500(request):
    return render(request, 'bucketlist/500.html')


class LoginRequiredMixin(object):

    '''View mixin which requires that the user is authenticated.'''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)

class HomeView(TemplateView):

    template_name = 'photoapp/index.html'
    #template_name = 'base.html'

class FacebookLogin(View):

    def post(self, request,*args, **kwargs):

        user_id=request.POST["id"]
        try:
            fb_user = FacebookUser.objects.get(facebook_id=user_id)
            user = User.objects.get(id=fb_user.contrib_user_id)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponse("success", content_type="text/plain")

        except ObjectDoesNotExist:

            #proceed to create the user
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            picture = request.POST["picture[data][url]"]
            # Create the user
            user = User()
            user.save()

            user.username = u"%s, %s" %(first_name,last_name)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            # Create the facebook user
            fb_user = FacebookUser(facebook_id=user_id,contrib_user=user, contrib_picture=picture)
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            fb_user.save()

            login(request, user)
            return HttpResponse("success", content_type="text/plain")


class SignOutView(View, LoginRequiredMixin):

    '''Logout User from session.'''

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse_lazy('homepage'))    

class PhotoAppView(TemplateView):

    template_name = 'photoapp/photoapp.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['facebook']=FacebookUser.objects.get(contrib_user_id=request.user.id)
        return self.render_to_response(context)



