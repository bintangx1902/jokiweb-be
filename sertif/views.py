from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import *
from .forms import *
from django.db.models import Q as __
from .utils import *
from django.contrib import messages


class LandingPage(View):
    template_name = get_template('index')

    def get(self, *args, **kwargs):
        form = UploadFileForms()
        context = {'form': form}
        return render(self.request, self.template_name, context)


class UploadFileView(CreateView):
    form_class = UploadFileForms
    model = UploadedFile
    template_name = get_template('upload')

    def form_valid(self, form):
        nim = form.cleaned_data.get('nim')
        type = form.cleaned_data.get('type')

        if find_data(self.model, nim, type):
            messages.info(self.request, f"Data {type} untuk {nim} sudah ada!")
            return redirect(reverse('certifi:landing-page'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certifi:landing-page')


class FindFile(ListView):
    model = UploadedFile
    template_name = get_template('data-list')
    context_object_name = 'files'

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET else None
        model = self.model
        query = model.objects.filter(__(nim__icontains=q) | __(full_name__icontains=q)) if q else model.objects.all()
        return query
