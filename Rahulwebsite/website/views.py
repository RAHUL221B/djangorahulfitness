from django.shortcuts import render,redirect
from django.core.mail import send_mail
from . models import Contact
from . models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django . http import HttpResponse
from .forms import PostForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
# Create your views here.

def home(request):
    
    return render(request,'home.html',)

def Allaboutabs(request):
    return render(request,'Allaboutabs.html',)

# def fatloss(request):
#     allPosts = Post.objects.all()
#     context = {'allPosts': allPosts}
#     return render(request,'fatloss.html',context)

class fatloss(ListView):
    model = Post
    cats = Category.objects.all()
    template_name = 'fatloss.html'
    ordering = ['-pk']
    paginate_by = 3
   



    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(fatloss,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
        

   
        
def Nutrition(request):
    return render(request,'Nutrition.html',{})

def supplements(request):
    return render(request,'supplements.html',{})

def Training(request):
    return render(request,'Training.html',{})

def calcount(request):
    return render(request,'calcount.html',{})

# def fatlossPost(request,slug):
#     post = Post.objects.filter(slug=slug).first()
#     context = {'post' : post}
#     return render(request,'fatlossPost.html',context)

class fatlossPost(DetailView):
       model = Post
       template_name = 'fatlossPost.html' 

   
def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()

    else:
         allPostsTitle = Post.objects.filter(title__icontains=query)
         allPostsContent = Post.objects.filter(content__icontains=query)
         allPosts = allPostsTitle.union(allPostsContent)

    params = { 'allPosts' : allPosts, 'query':query }
    return render(request,'search.html',params)



def contact(request):
     if request.method == "POST":
         name = request.POST.get('message-name',''),
         email = request.POST.get('message-email',''),
         message = request.POST.get('message',''),

         contact = Contact(name = name,email = email , message = message),
        #  contact.save()
         
        #  Contact = contact('name'),
        #  name = request.POST.get('name'),
        #  email = request.POST.get('email'),
        #  message = request.POST.get('message'),
         
        #  Contact.name = name
        #  Contact.email = email
        #  Contact.message = message

         
         contact.save(self)
         
        #  contact.name=name
        #  contact.email=email
        #  contact.message= message
         
        #   send an email
         send_mail(
                'Welcome to Fitness Inshorts',#subject
                'Thankyou for contacting us ..We will reach you soon',#message
                'email',#email
                ['rrpatil444@gmail.com'],#to email
                fail_silently=False,

                   )
                    
                    
                  
         
         
               

         

         return render(request,'contact.html', {'name' : name } )

     
     else:
          return render(request,'contact.html',{})
        
           
class  Addpostview(CreateView):
       model = Post
       form_class = PostForm
       template_name = 'addpost.html'
    #    fields = '__all__'  

class  Addcategoryview(CreateView):
       model = Category
    #    form_class = PostForm
       template_name = 'addcategory.html'
       fields = '__all__'  

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    paginator = Paginator(category_posts,3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1) 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '),'category_posts':posts,'page':page,})
    # category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    # context = {}
    # context['cats'] = cats.title().replace('-', ' ')
    # context['category_posts'] = category_posts
    # cat_menu = Category.objects.all()
    # context['cat_menu'] = cat_menu
    # return render(request, 'categories.html', context)



class Updatepostview(UpdateView):
    model = Post
    template_name = "updatepost.html"
    fields = '__all__'  

class Deletepostview(DeleteView):
    model = Post
    template_name = "deletepost.html"  
    success_url = reverse_lazy('fatloss')    

# def  Addpostview(request):
#        model = Post
#     #    namey = PostForm()
#        context = {}
#        context['form']= PostForm()
#     #    namey.save()
#        if request.method == 'POST':
#          form = PostForm(request.POST)
#          if form.is_valid():
            
#             context = {}
#             context['form']= PostForm()
#             form.save(commit = True)
#             return redirect('home')

#        else:
#         form = PostForm()

 
#     #    context = { 'form' = form}
#     #    template_name = 'addpost.html'
#     #    fields = '__all__'             
#        return render(request,'addpost.html',context)
       
 

       
     

