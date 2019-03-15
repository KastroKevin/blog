from django.contrib.auth import mixins
from django.shortcuts import redirect, render
from django.views import generic
from .models import ImageUser
from .forms import ImageUserForm
# Create your views here.

class CreateImageUserView(mixins.LoginRequiredMixin, generic.CreateView):
    queryset = ImageUser
    form_class = ImageUserForm
    template_name = 'profile/new.html'
    login_url = '/accounts/login/'
    success_url = '/profile/show/'

    def post(self, request, *args, **kwargs):
        imageuser = ImageUser()
        imageuser.user = request.user

        form = self.form_class(request.POST, request.FILES, instance=imageuser)
        if form.is_valid():
            form.save()
            return redirect('/profile/show/')

        return render(request, self.template_name, {'form': form})


class ListImageUserView(mixins.LoginRequiredMixin, generic.ListView):
    queryset = ImageUser
    template_name = 'profile/show.html'
    login_url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        user = request.user
        usuario = self.queryset.objects.get(user=user)
        return render(request, self.template_name, {'usuario': usuario})