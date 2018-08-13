from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile
from .forms import UserForm,ProfileForm,UploadForm
from django.http import HttpResponse
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def index(request):
    context = RequestContext(request)
    context_dict={}
    return render(request,'age_detection/index.html', context_dict, context)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
            pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'home/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
        
    })
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

from keras.preprocessing import image
from keras import optimizers
import numpy
from keras.models import load_model

def upload(request):
    context_dict = {}
    if request.method == 'POST' and request.FILES['image']:
        img = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(img)
        context_dict['name'] = request.POST['name']
        context_dict['gender'] = request.POST['gender']
        context_dict['weight'] = request.POST['weight']
        context_dict['uploaded_file_url'] = uploaded_file_url
        #DL part starts here

        model = load_model('models/catsAndDogs.h5')
        model.compile(optimizer=optimizers.RMSprop(lr=2e-5),loss='binary_crossentropy',metrics=['acc'])
        img_width, img_height = 150,150


        url_image = uploaded_file_url[1::]
        test_image= image.load_img(url_image, target_size = (img_width, img_height)) 
        test_image = numpy.expand_dims(test_image, axis = 0)
        result = model.predict_classes(test_image)
        if result[0][0] == 0:
            context_dict['age'] = 'Cat'
        else:
            context_dict['age'] = 'Dog'
        return render(request, 'age_detection/results.html', context_dict)
    return render(request, 'age_detection/upload.html')
