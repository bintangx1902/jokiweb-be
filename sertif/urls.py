from django.urls import path
from .views import *

app_name = 'certifi'

urlpatterns = [
    path('', LandingPage.as_view(), name='landing-page'),
    path('upload', UploadFileView.as_view(), name='upload-page'),
    path('find', FindFile.as_view(), name='find-page')
]
