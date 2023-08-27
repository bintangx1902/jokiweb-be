from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import *
from .forms import *
from django.db.models import Q as __
from .utils import *
from django.contrib import messages
from itertools import chain


class LandingPage(View):
    template_name = get_template('index')

    def get(self, *args, **kwargs):
        form = UploadFileForms()
        q = self.request.GET.get('q')
        mos = len(Certification.objects.filter(type_certification__icontains='MOS'))
        mta = len(Certification.objects.filter(type_certification__icontains='MTA'))
        mce = len(Certification.objects.filter(type_certification__icontains='MCE'))
        context = {'form': form, 'mos': mos, 'mce': mce, 'mta': mta}
        if q:
            query = Certification.objects.filter(
                __(full_name__icontains=q) | __(batch__icontains=q) | __(no_participant__icontains=q) | __(
                    type_certification__icontains=q))
            query3 = LecturerCertification.objects.filter(
                __(full_name__icontains=q) | __(batch__icontains=q) | __(no_participant__icontains=q) | __(
                    program__icontains=q))

            messages.info(self.request, 'data tidak ditemukan !') if not query and not query3 else None
            context['query'] = list(chain(query, query3))

        return render(self.request, self.template_name, context)


class UploadFileView(CreateView):
    form_class = UploadFileForms
    model = Certification
    template_name = get_template('upload')

    def form_valid(self, form):
        nim = form.cleaned_data.get('nim')
        type = form.cleaned_data.get('type')
        slug_list = [x.slug for x in self.model.all()]

        if find_data(self.model, nim, type):
            messages.info(self.request, f"Data {type} untuk {nim} sudah ada!")
            return redirect(reverse('certifi:landing-page'))
        else:
            messages.info(self.request, f"Data {type} untuk {nim} berhasiil di simpan!")

        while True:
            slug = create_slug(12)
            if slug not in slug_list:
                break

        form.instance.slug = slug

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('certifi:landing-page')


class FindFile(ListView):
    model = Certification
    template_name = get_template('data-list')
    context_object_name = 'files'

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET else None
        model = self.model
        query = model.objects.filter(__(nim__icontains=q) | __(full_name__icontains=q)) if q else model.objects.all()
        return query


class DataDetails(DetailView):
    model = Certification
    template_name = None
    context_object_name = 'data'
    query_pk_and_slug = True
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
