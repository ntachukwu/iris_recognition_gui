from django.urls import path
from .views import home_view, eval_casia1_view, verification_view

urlpatterns = [
    path("", home_view, name='home'),
    path("eval/", eval_casia1_view, name='eval'),

    path("verify/", verification_view, name="verify")
]
