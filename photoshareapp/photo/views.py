from django.shortcuts import render,render_to_response, redirect

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from .models import Photo, PhotoCategory
from .forms import PhotoForm
import re


def error404_view(request):
    print ('Naveen')
    return render(request, '404.html')

def HomePageView(request):
    users=User.objects.all()
    for user in users:
        p_count=Photo.objects.public_photo_count(user)
        c_count=Photo.objects.community_photo_count(user)
        user.public_photo_count=p_count
        user.community_photo_count=c_count
    return render(request, 'newhome.html', {'users': users})

def UserDetail(request,pk):
    if re.compile('\d+').match(pk):
        user=User.objects.filter(id=pk)
    else:
        user=User.objects.filter(username=pk)
    if not user :
        return redirect('home')
    cat1=PhotoCategory.objects.filter(category='Public')
    cat2=PhotoCategory.objects.filter(category='Community')
    photos=None
    if user[0].id == request.user.id:
        photos=Photo.objects.filter(uploaded=user[0])
    elif request.user.is_authenticated():
        photos=Photo.objects.filter(uploaded=user,category=(cat1 | cat2))
    else:
        photos=Photo.objects.filter(uploaded=user,category=(cat1))
    return render(request, 'auth/user_detail.html', {'photos': photos,'user_to_show':user[0]})


class PhotoCreateView(CreateView):
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        f=form.save(commit=False)
        f.uploaded=self.request.user
        return super(PhotoCreateView,self).form_valid(form)

def PhotoDetail(request,pk):
    photo=Photo.objects.get(id=pk)
    if photo:
        if request.user.id ==  photo.uploaded.id:
            print ("Logged in match")
            return render(request, 'photo/photo_detail.html', {'photo': photo})
        elif request.user.id:
            if photo.category.category == 'Private':
                return redirect('home')
            else:
                return render(request, 'photo/photo_detail.html', {'photo': photo})
        else:
            if photo.category.category == 'Public':
                return render(request, 'photo/photo_detail.html', {'photo': photo})
            else:
                return redirect('home')
    else:
        return redirect('home')








