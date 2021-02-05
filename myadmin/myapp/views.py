from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Mycontact

def home(request):
    # return HttpResponse("Welcome to admin Portal:")
    return render(request, "index.html")


def about(request):
    # return HttpResponse("Welcome to About portal:")
    return render(request, "about.html")

def contact(request):
    # return HttpResponse("Welcome to Contact page:")
    return render(request, "contact.html")

def portfolio_details(request):
    return render(request, "portfolio_details.html")

# Create your views here.
def jain(request):
    database=Mycontact.objects.all()
    print(database)
    for item in database:
        print(item.your_name,
            item.your_email,
            item.Subject,
            item.Message)
    return render(request, "jain.html")

# To get from data using post method:
user_info={}
def get_content(request):

    if request.method=='POST':
        # print("Post method:")
        user_info['name']=request.POST.get('name')
        user_info['email']=request.POST.get('email')
        user_info['subject']=request.POST.get('subject')
        user_info['message']=request.POST.get('message')
    Mycontact1 = Mycontact()
    Mycontact1.your_name=user_info['name']
    Mycontact1.your_email=user_info['email']
    Mycontact1.Subject=user_info['subject']
    Mycontact1.Message=user_info['message']
    Mycontact1.save()
    print(user_info)
    return render(request,"jain.html")
