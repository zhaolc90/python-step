import os
from django.http import Http404
from django.shortcuts import render
# from django.template import loader
from django.utils._os import safe_join
from django.template import Template
BASE_PAGE_DIR = os.path.dirname(__file__)

# Create your views here.
def get_template_or_404(name):
    path_name = os.path.join(BASE_PAGE_DIR, 'pages')
    file_path = safe_join(path_name, name)
    if not os.path.exists(file_path):
        raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        page = Template(f.read())
    
    return page

def page(request, slug='index'):
    # template = loader.get_template('sitebuilder/page.html')
    file_name = '{}.html'.format(slug)
    page = get_template_or_404(file_name)
    context={
        'slug':slug,
        'page':page,
    }
    return render(request, 'page.html',context)