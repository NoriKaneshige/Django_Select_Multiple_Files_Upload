from django.views import generic
from .forms import MultipleUploadForm

class InputMultiUploadView(generic.FormView):
    form_class = MultipleUploadForm
    template_name = 'app/upload.html'

    def form_valid(self, form):
        download_url_list = form.save()
        context = {
            'download_url_list': download_url_list,
            'form': form,
        }
        return self.render_to_response(context)