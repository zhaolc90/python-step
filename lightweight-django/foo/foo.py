# django==1.7.0
import sys
import os
import hashlib
from io import BytesIO
from PIL import Image,ImageDraw
from django.views.decorators.http import etag 

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms
from django.conf import settings
DEBUG = os.environ.get('DEBUG', 'on') ==  'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'c+baojq!^z-2vw#e^ep=&1!r#acaodq4rr3d0lb#&kw9vbyxhx')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    APP_DIRS= True,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),
    TEMPLATE_DIRS=(
        os.path.join(BASE_DIR, 'templates/'),
    ),
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
    ),
    DIRS=(
        os.path.join(BASE_DIR, 'templates'),
    ),
    STATIC_URL='/static/',
)
class ImageForm(forms.Form):
    height= forms.IntegerField(min_value=1,max_value=2000)
    width= forms.IntegerField(min_value=1,max_value=2000)
    def generate(self, image_format='PNG'):
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        image=Image.new('RGB', (width,height))
        draw = ImageDraw.Draw(image)
        text = '{} X {}'.format(width, height)
        textwidth, textheight = draw.textsize(text)
        if textwidth < width and textheight < height:
            texttop = (height - textheight) // 2
            textleft = (width - textwidth) // 2
            draw.text((textleft, texttop), text, fill=(255, 255, 255))
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        return content
def generate_etag(request, width, height):
    content = 'Placeholder: {0} x {1}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()

@etag(generate_etag)
def placeholder(request, width, height):
    print(width)
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        image=form.generate()
        return HttpResponse(image,content_type='image/png' )
    else:
        return HttpResponseBadRequest('Invalid Image Request')

def index(request):
    example = reverse('placeholder',kwargs={'width':50,'height':50})
    context = {
        'example':request.build_absolute_uri(example)
    }
    return render(request, 'home.html', context)

urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder,
        name='placeholder'),
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)