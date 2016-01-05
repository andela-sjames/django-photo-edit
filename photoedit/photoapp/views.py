import os

from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse,\
    HttpResponseBadRequest, HttpResponseNotAllowed
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.conf import settings

from photoapp.models import FacebookUser, Photo
from photoapp.forms import PhotoForm
from photoapp.effects import Applyeffects


class LoginRequiredMixin(object):

    '''View mixin which requires that the user is authenticated.'''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class HomeView(TemplateView):

    template_name = 'photoapp/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(
                reverse_lazy('photoview'))
        return super(HomeView, self).dispatch(request, *args, **kwargs)


class FacebookLogin(View):

    '''Class Used to Login existing and non-existing user.'''

    def post(self, request, *args, **kwargs):

        user_id = request.POST["id"]
        try:
            fb_user = FacebookUser.objects.get(facebook_id=user_id)
            user = User.objects.get(id=fb_user.contrib_user_id)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponse("success", content_type="text/plain")

        except FacebookUser.DoesNotExist:

            # proceed to create the user
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            picture = request.POST["picture[data][url]"]

            # Create the user
            user = User(
                username=u"%s, %s" % (first_name, last_name),
                email=request.POST["email"],
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            # Create the facebook user
            fb_user = FacebookUser(facebook_id=user_id,
                                   contrib_user=user,
                                   contrib_picture=picture)

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


class PhotoAppView(TemplateView, LoginRequiredMixin):

    '''Class used to view uploaded photos.'''

    template_name = 'photoapp/photoapp.html'

    def get(self, request, *args, **kwargs):

        userid = self.request.user.id

        context = self.get_context_data(**kwargs)
        context['facebook'] = FacebookUser.objects.get(
            contrib_user_id=request.user.id)
        context['photos'] = Photo.objects.filter(user_id=userid)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        photoform = PhotoForm(request.POST, request.FILES)

        if photoform.files['image'].size > settings.MAX_UPLOAD_SIZE:
            return HttpResponseNotAllowed('largefile')

        try:
            img = photoform.save(commit=False)
            img.user = request.user
            img.save()
            return HttpResponse("success", content_type="text/plain")

        except:
            return HttpResponseBadRequest('Unknownerror')


class DeletePhotoView(View, LoginRequiredMixin):

    '''class to delete existing photos.'''

    def get(self, request, *args, **kwargs):

        photoid = request.GET.get('id')

        try:
            photo = Photo.objects.get(id=photoid)
        except Photo.DoesNotExist:
            raise Http404

        photo.delete()

        return HttpResponse("success", content_type="text/plain")


class PillowImageView(TemplateView):

    ''' Class defined to apply effect to image.'''

    def get(self, request, *args, **kwargs):

        pilimage = str(request.GET.get('image'))
        effect = request.GET.get('effect')

        filepath, ext = os.path.splitext(pilimage)
        edit_path = filepath + 'edited' + ext

        image_effects = Applyeffects(pilimage)
        image_effects.effect(effect)

        return HttpResponse(os.path.relpath(edit_path, settings.BASE_DIR),
                            content_type="text/plain")


def custom_404(request):
    return render(request, 'photoapp/404.html')


def custom_500(request):
    return render(request, 'photoapp/500.html')
