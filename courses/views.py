from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.views import generic
from courses.models import Course

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class CourseListView(LoggedInMixin, generic.ListView):
    template_name = 'courses/list.html'
    context_object_name = 'courses'
    def get_queryset(self):
        return Course.objects.filter(group=self.request.user.groups.all()).order_by('publish')[:5]

class CourseDetailView(LoggedInMixin, generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk = pk,
            group = self.request.user.groups.all(),
        )
        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied
        return obj

from django.core.urlresolvers import reverse

class CourseCreateView(generic.CreateView):
   model = Course
   fields = ['title', 'description', 'author', 'group']
   template_name = 'courses/create.html'

class CourseDeleteView(generic.DeleteView):
   model = Course
   template_name = 'courses/delete.html'
   def get_success_url(self):
       return reverse('courses:course_list')

class CourseEditView(generic.UpdateView):
    model = Course
    fields = ['title', 'description', 'author']
    template_name = 'courses/edit.html'

