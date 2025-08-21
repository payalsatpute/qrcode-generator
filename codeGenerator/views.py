from django.shortcuts import render
from .forms import qrcodeform
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):

    if request.method == 'POST':
        form = qrcodeform(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['restaurant_url']

            # generate qr code here
            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_").lower() + 'menu.png'
            file_path =os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            # craeting img url
            qr_url =settings.MEDIA_URL + file_name
            print("Final QR URL:", qr_url)


            context = {
                'res_name': res_name,
                'qr_url': qr_url,   #actally this line show qrcode on web-page
                'file_name': file_name,
            }

            return render(request, 'qr_result.html', context)



           
    else:

        form = qrcodeform()
        context = {
            'form':form
        }
        return render(request, 'generate_qr_code.html', context)

