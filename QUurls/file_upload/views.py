# file_upload/views.py

from django.shortcuts import render, redirect
from .forms import FileUploadForm
from django.core.signing import Signer
from django.http import HttpResponseBadRequest
from django.core.files.uploadedfile import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            signer = Signer()
            signed_value = signer.sign(uploaded_file.pk)
            link = request.build_absolute_uri('/file/{0}/'.format(signed_value))
            return render(request, 'file_upload/link_generated.html', {'link': link})
    else:
        form = FileUploadForm()

    return render(request, 'file_upload/upload_file.html', {'form': form})

def view_file(request, signed_value):
    signer = Signer()
    try:
        file_id = signer.unsign(signed_value)
        uploaded_file = UploadedFile.objects.get(pk=file_id)
    except (signer.BadSignature, UploadedFile.DoesNotExist):
        return HttpResponseBadRequest("Invalid Link")

    return render(request, 'file_upload/view_file.html', {'uploaded_file': uploaded_file})
