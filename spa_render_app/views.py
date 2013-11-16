from django.http import HttpResponse
import subprocess

def home(request):
    text = subprocess.check_output([
                'phantom/phantomjs-linux', 
                'phantom/phantom-server.js', 
                'http://www.nerdeez.com'
            ])
    return HttpResponse(text)