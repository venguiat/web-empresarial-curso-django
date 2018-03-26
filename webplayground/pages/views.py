from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForm
from django.shortcuts import redirect
# Create your views here.

class StaffRequiredMixin(object):
		@method_decorator(staff_member_required)
		def dispatch(self, request, *args, **kwargs):
			return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class PageListView(ListView):
	model = Page
	template_name = 'pages/pages.html'

class PageDetailView(DetailView):
	model = Page
	template_name = 'pages/page.html'

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
	model = Page
	form_class = PageForm
	success_url = reverse_lazy('pages:pages')



class PageUpdate(StaffRequiredMixin, UpdateView):
	model = Page
	form_class = PageForm
	template_name_suffix = '_update_form'
	

	def get_success_url(self):
		return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(StaffRequiredMixin, DeleteView):
	model = Page
	success_url = reverse_lazy('pages:pages')


