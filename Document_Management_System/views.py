from django.http import HttpResponse
from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyBvUElwQ1YlmrPCF3FC363mfd8iNW7LFFo",
    'authDomain': "dms-kp.firebaseapp.com",
    'databaseURL': "https://dms-kp.firebaseio.com",
    'projectId': "dms-kp",
    'storageBucket': "dms-kp.appspot.com",
    'messagingSenderId': "950229245673",
    'appId': "1:950229245673:web:3586b29d7b5f633e"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def login(request):
    return render(request,'html/login.html')
def postsign(request):
    email=request.POST.get('email')
    password=request.POST.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email,password)
    except:
        massage = "Username or password incorrect"
        return render(request,'html/login.html',{"messg":massage})
    print(user)
    return render(request,"html/welcome.html",{"e":email})



