from django import forms
import os,uuid


def handle_single_image(f):
    st = str(uuid.uuid4())
    with open('https://own-online-course.herokuapp.com/staticfiles/mycrud/static/crud/files/img/' + "_" + st + ".jpg", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/img/' + "_" + st + ".jpg"
        return viewPath


def handle_jpg_image_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/jpg/'+st+".jpg", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/jpg/'+st+".jpg"
        return viewPath

def handle_png_image_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/png/'+st+".png", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/png/' + st + ".png"
        return viewPath

def handle_audio_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/audio/'+st+".mp3", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath =  '/static/crud/files/audio/' + st + ".audio"
        return viewPath

def handle_video_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/video/'+st+".mp4", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/video/' + st + ".video"
        return viewPath

def handle_pdf_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/pdf/'+st+".pdf", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/static/crud/files/pdf/' + st + ".pdf"
        return viewPath


def handle_text_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/text/'+st+".text", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/text/' + st + ".text"
        return viewPath

def handle_doc_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/doc/'+st+".doc", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/doc/' + st + ".doc"
        return viewPath

def handle_html_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/html/'+st+".html", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/html/' + st + ".html"
        return viewPath

def handle_css_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/css/'+st+".css", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/css/' + st + ".css"
        return viewPath


def handle_java_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/js/'+st+".js", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/java/' + st + ".java"
        return viewPath

def handle_psd_file(f):
    st = str(uuid.uuid4())
    with open('crud/static/crud/files/psd/'+st+".psd", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/crud/files/psd/' + st + ".psd"
        return viewPath

class dateInput(forms.DateInput):
    input_type = 'date'


class timeInput(forms.TimeInput):
    input_type = 'time'

class datetimeInput(forms.DateInput):
    input_type = 'date'


def delete_file(arg):
        os.remove("/static/crud/files/jpg/new file added.jpg")
        print("File Deleted")
