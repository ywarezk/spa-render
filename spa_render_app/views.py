from django.http import HttpResponse
import subprocess

def home(request):
    '''
    will render a page with its javascript
    @param url: passed via get param containing the url to render
    '''
    url = request.GET.get('url')
    text = subprocess.check_output([
                'phantom/phantomjs-linux', 
                'phantom/phantom-server.js', 
                url
            ])
    return HttpResponse(text)