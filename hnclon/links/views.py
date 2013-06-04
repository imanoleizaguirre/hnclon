from django.views.generic import ListView
from links.models import Link, Vote


class LinkListView(ListView):
    model = Link