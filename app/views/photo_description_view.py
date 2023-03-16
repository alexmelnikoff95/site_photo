from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from app.models import PhotoDescription


class PhotoDescriptionListView(PermissionRequiredMixin, ListView):
    """Категории разделов с фотографиями"""
    model = PhotoDescription
    paginate_by = 2
    context_object_name = 'photo'
    template_name = 'photo/photo_description_list.html'

    def get_queryset(self):
        # if self.request.user.view_photodescription:
        #     raise Http404
        return PhotoDescription.objects.filter(publication=True)

    def has_permission(self):
        if self.request.user.is_staff:
            return True
        return False


class PhotoDescriptionDetailView(DetailView):
    """Категория"""
    model = PhotoDescription
    context_object_name = 'photo'
    template_name = 'photo/photo_description_detail.html'
