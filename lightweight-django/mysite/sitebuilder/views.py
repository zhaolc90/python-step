from django.shortcuts import render
# from django.template import loader

# Create your views here.
def page(request, slug='index'):
    # template = loader.get_template('sitebuilder/page.html')
    file_name = '{}.html'.format(slug)
    page = file_name
    context={
        'slug':slug,
        'page':page,
    }
    return render(request, 'page.html',context)