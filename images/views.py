from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Image,Category,Tag, Location, NewsLetterRecipients, Editor, Comment, Profile
from django.db.models import Q
from .forms import SubscribeForm, NewArticleForm, CommentsForm, updateProfileForm
from .email import registered 
from django.contrib.auth.decorators import login_required




# @login_required(login_url='/auth/login/')
def homePageElements(request):
    all_images = Image.view_all_pictures()
    user_details = Editor.view_editor_details()
    rel_categories = Category.objects.all()
    rel_tags = Tag.objects.all()
    date = dt.date.today()
    location = Location.objects.all()
    title = "home"

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            registered(name, email)
            HttpResponseRedirect('homePageElements')
    else:
        form = SubscribeForm()
        return render(request, 'main/homepage.html', {"date": date, "all_images": all_images, "rel_categories":rel_categories, "rel_tags":rel_tags, "location": location, "title":title, "form":form, "user_details":user_details })


@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
            return redirect(homePageElements)
            
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})

    
# @login_required(login_url='/accounts/login/')
def profile_page(request):
    title = "View profile"
    profile = Profile.objects.all()
    user = request.user
    return render(request,'profile.html', {"title":title, "profile":profile, "user":user})


def updateProfile(request):
    date = dt.date.today()
    title = "Change profile"
    user = request.user

    profile = Profile.objects.all()

    if request.method == 'POST':
        form = updateProfileForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.profile=profile
            feedback.save()
            return redirect('profile', image_id=image_id)
    else:
        form = CommentsForm()
    
    return render(request,'change_profile.html', {"profile":profile, "date":date, 'form':form, 'user':user})







def images_by_date(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    # if date == dt.date.today():
    #     return redirect(news_today)
    
    img = Image.pictures_by_date(date)
    return render(request, 'all_images/image.html', {"date": date, "img":img})




def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article") 
        searched_images = Image.search_by_title(search_term) or Tag.search_by_tag(search_term) or Category.search_by_cat(search_term)
        message = f"{search_term}"
        date = dt.date.today()

        return render(request, 'all_images/search.html', {"message":message, "images": searched_images, "date":date})
    else:
        message = "You havne't searched for any term"
        date = dt.date.today()
        return render(request, 'all_images/search.html',{"message":message, "date":date})

def image(request, image_id):
    date = dt.date.today()
    # comment = Comment.view_all_comments()
    comments = Comment.objects.all()
    # comment = comment

    
    image = Image.objects.get(id = image_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.iamge = image
            feedback.save()
            return redirect('image', image_id=image_id)
    else:
        form = CommentsForm()
    
    return render(request,'image.html', {"image":image, "date":date, 'form':form, 'comments':comments})

# def categories(request):
#     category = Category.objects.all()
#     return render(request,'projects/article.html', {"category":category})
