from django.urls import path
from .views import *
from .forms import *

app_name = "psychotherapy"
urlpatterns = [
	path('', WizardFormView.as_view(FORMS), name='wizard_step_one_url'),
]