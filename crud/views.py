import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import shutil
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from crud.forms import fileForm
from django.contrib.auth.hashers import make_password
import base64,traceback,logging
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from cryptography.fernet import Fernet
from .models import setField,setFile,singleImage,logIn,signUp
from .forms import fileForm,textForm,singleImgForm,loginForm,signUpForm
from .functions import handle_single_image,handle_jpg_image_file,handle_png_image_file,handle_audio_file,handle_video_file,handle_pdf_file,handle_text_file,handle_doc_file,handle_html_file,handle_css_file,handle_java_file,handle_psd_file,delete_file

# Create your views here.
LogIn = False

def location(request):
    global LogIn
    if LogIn == False:
        return render(request,"html/login.html",{"form":loginForm})
    else:
        return redirect("/")


def viewFile(request):
    forms = setFile.objects.all()
    return render(request,"html/modify_setFile.html",{"forms":forms})

def set_File(request):
    if request.method == "POST":
        data = fileForm(request.FILES)
        if data.is_valid:
            jpg = handle_jpg_image_file(request.FILES['jpg_image'])
            png = handle_png_image_file(request.FILES['png_image'])
            audio = handle_audio_file(request.FILES['audio'])
            video = handle_video_file(request.FILES['video'])
            pdf = handle_pdf_file(request.FILES['pdf'])
            text = handle_text_file(request.FILES['text'])
            doc = handle_doc_file(request.FILES['doc'])
            html = handle_html_file(request.FILES['html'])
            css = handle_css_file(request.FILES['css'])
            java = handle_java_file(request.FILES['java'])
            psd = handle_psd_file(request.FILES['psd'])
            result = setFile(jpg_image = jpg,png_image=png,audio=audio,video=video,pdf=pdf,text=text,doc=doc,html=html,css=css,java=java,psd=psd)
            result.save()
            form = fileForm()
            return render(request, 'html/setFile.html', {'form': form })
        else:
            return render(request, 'html/base.html')
    else:
        form = fileForm
        return render(request,'html/setFile.html', {'form':form })

def update_files(request,id):
    files = setFile.objects.get(id=id)
    data = fileForm(instance=files)
    if request.method == "POST":
        try:
            if request.FILES['jpg_image']:
                deltPath = files.jpg_image.name
                deltPath = "crud" + deltPath
                try:
                    os.remove(deltPath)
                    files.jpg_image = handle_jpg_image_file(request.FILES['jpg_image'])
                    files.save()
                except:
                    files.jpg_image = handle_jpg_image_file(request.FILES['jpg_image'])
                    files.save()
        except:
            pass
        try:
            if request.FILES['png_image']:
                deltPath = files.png_image.name
                deltPath = "crud" + deltPath
                try:
                    os.remove(deltPath)
                    files.png_image = handle_png_image_file(request.FILES['png_image'])
                    files.save()
                except:
                    files.png_image = handle_png_image_file(request.FILES['png_image'])
                    files.save()
        except:
            pass
        try:
            if request.FILES['text']:
                deltPath = files.text.name
                deltPath = "crud" + deltPath
                try:
                    os.remove(deltPath)
                    files.text = handle_text_file(request.FILES['text'])
                    files.save()
                except:
                    files.text = handle_text_file(request.FILES['text'])
                    files.save()
        except:
            pass
        try:
            if request.FILES['html']:
                deltPath = files.html.name
                deltPath = "crud" + deltPath
                try:
                    os.remove(deltPath)
                    files.html = handle_html_file(request.FILES['html'])
                    files.save()
                except:
                    files.html = handle_html_file(request.FILES['html'])
                    files.save()
        except:
            pass
        try:
            if request.FILES['css']:
                deltPath = files.css.name
                deltPath = "crud" + deltPath
                try:
                    os.remove(deltPath)
                    files.css = handle_css_file(request.FILES['css'])
                    files.save()
                except:
                    files.css = handle_css_file(request.FILES['css'])
                    files.save()
        except:
            pass
        return redirect("/crud/viewFile")
    filePath = {
        "id":files.id,
        "jpg":files.jpg_image,
        "png":files.png_image,
        "video":files.video,
        "audio":files.audio,
        "pdf":files.pdf,
        "text":files.text,
        "doc":files.doc,
        "html":files.html,
        "css":files.css,
        "java":files.java,
        "psd":files.psd,
        "form":data,
    }
    return render(request,'html/editFiles.html',filePath)

def delete_files(request,id):
    data = setFile.objects.get(id=id)
    try:
        delPng = "crud"+data.png_image.name
        os.remove(delPng)
    except:
        pass
    try:
        delJpg = "crud"+data.jpg_image.name
        os.remove(delJpg)
    except:
        pass
    try:
        delTxt = "crud"+data.text.name
        os.remove(delTxt)
    except:
        pass
    try:
        delHtml = "crud"+data.html.name
        os.remove(delHtml)
    except:
        pass
    try:
        delCss = "crud"+data.css.name
        os.remove(delCss)
    except:
        pass
    delJava = "crud"+data.java.name
    delPsd = "crud"+data.psd.name
    delDoc = "crud" + data.doc.name
    delVdo = "crud" + data.video.name
    delAdio = "crud" + data.audio.name
    delPdf = "crud" + data.pdf.name
    data.delete()
    dlt = "File and Text Deleted"
    forms = setFile.objects.all()
    return render(request, "html/modify_setFile.html", {"forms": forms,"dlt":dlt})


def view_singleFile(request):
    form = singleImgForm()
    return render(request, "html/singleImage.html", {"form": form})

def saveSingleImg(request):
    if request.method == "POST":
        data = singleImgForm(request.POST,request.FILES)
        try:
            if data.is_valid:
                Path = handle_single_image(request.FILES['myImg'])
                save = singleImage(imgname=request.POST['imgname'],myImg=Path)
                save.save()
                messages.success(request,"Data Save Successfully")
                form = singleImgForm()
                return render(request, "html/singleImage.html", {"form": form})
        except:
            messages.error(request,"some error")
            form = singleImgForm()
            return render(request, "html/singleImage.html", {"form": form})
    form = singleImgForm()
    return render(request, "html/singleImage.html", {"form": form})


def modiSingleImg(request):
    data = singleImage.objects.all()
    return  render(request,"html/singleDel.html",{"forms":data})

def updateSingleImg(request,id):
    try:
        item = singleImage.objects.get(id=id)
        data = singleImgForm(instance=item)
        if request.method == "POST":
                name = request.POST['imgname']
                item.imgname = name
                item.save()
                if request.FILES['myImg']:
                    deltPath = item.myImg.name
                    deltPath = "crud"+item.myImg.name
                    os.remove(deltPath)
                    item.myImg = request.FILES['myImg']
                Path = handle_single_image(request.FILES['myImg'])
                item.myImg = Path
                item.save()
                return redirect("/crud/modi_single_file/")
        return render(request, "html/editSingleImg.html", {"form": data,"id":item.id,"url":item.myImg})
    except:
        return redirect("/crud/modi_single_file/")

def delete_single_files(request,id):
    try:
        data = singleImage.objects.get(id=id)
        deltPath = "crud"+data.myImg.name
        os.remove(deltPath)
        data.delete()
        data = singleImage.objects.all()
        return render(request, "html/singleDel.html", {"forms": data})
    except:
        try:
            data = singleImage.objects.get(id=id)
            data.delete()
            return redirect("/crud/modi_single_file/")
        except:
            return redirect("/crud/modi_single_file/")


def viewText(request):
    forms = setField.objects.all()
    return render(request,'html/modify_setText.html',{"forms":forms})

def setText(request):
    if request.method == 'POST':
        forms = textForm(request.POST, request.FILES)
        if forms.is_valid():
            name = request.POST['characterField']
            Path = handle_single_image(request.FILES['image'])
            try:
                forms.save()
                forms.instance.image = Path
                forms.save()
                text_form = textForm()
                return render(request, 'html/setText.html', {'forms': text_form})
            except:
                text_form = textForm()
                return render(request, 'html/setText.html', {'forms': text_form})
    else:
        text_form = textForm()
        return render(request,'html/setText.html',{'forms':text_form})

def update(request,id):
    data = setField.objects.get(id=id)
    forms = textForm(instance=data)
    if request.method == "POST":
        data.dropdown = request.POST['dropdown']
        data.choice = request.POST['choice']
        data.multichoice = request.POST['multichoice']
        data.characterField = request.POST['characterField']
        data.textField = request.POST['textField']
        data.intField = request.POST['intField']
        data.dateField = request.POST['dateField']
        data.timeField = request.POST['timeField']
        data.datetimeField = request.POST['datetimeField']
        data.decimalField = request.POST['decimalField']
        data.emailField = request.POST['emailField']
        data.floatField = request.POST['floatField']
        data.positiveintField = request.POST['positiveintField']
        data.positivebigintField = request.POST['positivebigintField']
        if request.FILES['image']:
            try:
                os.remove("crud"+data.image.name)
            except:
                pass
        Path = handle_single_image(request.FILES['image'])
        data.image=Path
        data.save()
        return redirect("/crud/viewText/")
    return render(request, 'html/editText.html', {'forms': forms,'id':data.id})


def delete(request,id):
    data = setField.objects.get(id=id)
    deltPath = "crud" + data.image.name
    try:
        os.remove(deltPath)
        data.delete()
    except:
        data.delete()
    return redirect("/crud/viewText/")

fernet = ''
def encryptions(param):
    global fernet
    f = Fernet.generate_key()
    fernet = Fernet(f)
    enc = fernet.encrypt(bytes(param,'ascii'))
    return enc
def decryptions(param):
    global fernet
    dec = fernet.decrypt(param)
    return str(dec,'ascii')

def logInPage(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"LogIn SuccessFully")
                return redirect("/crud/settext/")
            else:
                context = { "form" : loginForm() ,"result":"Not matching"}
                return render(request, 'html/login.html',context)
    logInPage = loginForm()
    return render(request,'html/login.html',{'form':logInPage})


def creataAccount(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        try:
            checkName = signUp.objects.filter(userName=request.POST['userName'])
            checkEmail = signUp.objects.filter(email=request.POST['email'])
            if len(checkName) == 0 and len(checkEmail) == 0:
                if form.is_valid():
                    if request.POST['password'] == request.POST['repassword']:
                        user = User.objects.create_user(first_name=request.POST['firstName'],last_name=request.POST['lastName'],email=request.POST['email'],username=request.POST['userName'],password=request.POST['password'])
                        user.save()
                        createAcc = signUpForm()
                        context = {'form': createAcc,'result':'Account Create Successfully',}
                        return render(request, 'html/signUp.html', context)
                    else:
                        createAcc = signUpForm()
                        context = {'form': createAcc, 'result': 'Password Not Matched', }
                        return render(request, 'html/signUp.html', context)
            else:
                createAcc = signUpForm()
                context = {'form': createAcc, 'result': 'UserName or Email Alredy Exists', }
                return render(request, 'html/signUp.html', context)
        except:
            createAcc = signUpForm()
            context = { 'form': createAcc,'result': 'Invalid Input',}
            return render(request, 'html/signUp.html', context)
    else:
        createAcc = signUpForm()
        return  render(request,'html/signUp.html',{'form':createAcc})


def auth_reg(request):
    if request.user.is_authenticated:
        return redirect("/crud/settext/")
    forms = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registrations Success")
            return redirect("/crud/")
        else:
            messages.error(request, "Registrations Not Success")
            return redirect("/crud/")
    return render(request,'html/auth_reg.html',{'forms':forms})

def auth_login(request):
    if request.user.is_authenticated:
        return redirect("/crud/settext/")
    forms = loginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usr = authenticate(request,username=username,password=password)
        if usr is not None:
            login(request,usr)
            messages.success(request,"LogIn Success")
            return redirect("/crud/settext/")
        else:
            messages.error(request, "Not Matched UserName or Password")
            return redirect("/crud/auth_login")
    return render(request,'html/auth_login.html',{"forms":forms})

def auth_logout(request):
    logout(request)
    return redirect("/crud/auth_login")