from django.shortcuts import render, redirect
from .forms import ContentForm
from barcode import EAN13
from barcode.writer import ImageWriter
from barcode.ean import IllegalCharacterError, NumberOfDigitsError
import pyqrcode
import png



def home(request):
    template_name = 'app/home.html'
    context = {}
    return render(request, template_name, context)
    

def generate_bar_view(request):
    
    """ generate content into barcode"""
    
    form = ContentForm(request.POST or None)
    try:
        if form.is_valid():
            content_data = form.cleaned_data.get("content")
            
            
            #Generate Bar Code
            barcode = EAN13(content_data)
            barcode_img = EAN13(content_data, writer=ImageWriter())   
            barcode.save("app/static/app/bar")
            barcode_img.save("app/static/app/bar")
            
            
            return redirect('/bar-generated')
        
        
        template_name = 'app/bar-home.html'
        context = {'form':form}
        return render(request, template_name, context)
    except IllegalCharacterError:
        template_name = 'app/bar-home.html'
        error = "EAN code can only contain numbers."
        context = {'form':form, 'error': error}
        return render(request, template_name, context)
    except NumberOfDigitsError:
        template_name = 'app/bar-home.html'
        content_length = str(len(content_data))
        error = "EAN must have 12 digits, not " + content_length
        context = {'form':form, 'error': error}
        return render(request, template_name, context)
    



def generated_bar_view(request):
    
    """ display generated barcode """
    
    template_name = 'app/bar-generated.html'
    context = {}
    return render(request, template_name, context)


def generate_qr_view(request):
    
    """ generate content into qrcode"""
    
    form = ContentForm(request.POST or None)
    if form.is_valid():
        content_data = form.cleaned_data.get("content")
    
        
        # Generate QR code
        qrcode = pyqrcode.create(content_data)
        qrcode.svg("app/static/app/qr.svg", scale = 8)        
        qrcode.png('app/static/app/qr.png', scale = 6)
        
        
        return redirect('/qr-generated')
    
    
    template_name = 'app/qr-home.html'
    context = {'form':form}
    return render(request, template_name, context)

        

def generated_qr_view(request):
    
    """ display generated qrcode """
    
    template_name = 'app/qr-generated.html'
    context = {}
    return render(request, template_name, context)
