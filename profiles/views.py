from profiles.models import PilotProfile
from django.shortcuts import get_list_or_404, get_object_or_404, render

# Create your views here.
def show_all(req):
    profiles_list = get_list_or_404(PilotProfile)
    return render(req, "templates/PilotProfile/all.html", {"pilots": profiles_list})


def show_one(req, pid):
    pilot = get_object_or_404(PilotProfile, pid)
