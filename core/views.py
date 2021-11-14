from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
import pyrebase

import os

# Upload Files
config = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "databaseURL": ""
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_storage = 'files/'
name_file = ''

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload_file(request):
    
    if request.method == 'POST':
        file = request.FILES['file']
        name_file = file.name
        file_save = default_storage.save(file.name, file)
        storage.child(path_storage + file.name).put("media/" + file.name)
        delete = default_storage.delete(file.name)
        return redirect('open/')
    else:
        return render(request, 'index.html')


def open(request):
    file_storage = storage.child(path_storage + 'bom dia.jpg').get_url(token='')#.download("media/" + 'bom dia.jpg')
    content = {
        'link': file_storage,
    }
    return render(request, 'file.html', content)