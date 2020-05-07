from django import forms
from django.core.files.storage import default_storage

class MultipleUploadForm(forms.Form):
    file = forms.ImageField(
        label='image file',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )
# need to change < input type="file"> into <input type="file" multiple>
# to achieve this, we overwrite widget like above

    def save(self):
        url_list = []
        for upload_file in self.files.getlist('file'):
            file_name = default_storage.save(upload_file.name, upload_file)
            file_path = default_storage.url(file_name)
            url_list.append(file_path)
        return url_list

# cleaned_data only receives the lastly uploaded file data, so we use self.files.getlist().
# uploaded files are passed to form side as files=request.FILES. So, from form side perspective,
# we can access request.FILES by self.files.