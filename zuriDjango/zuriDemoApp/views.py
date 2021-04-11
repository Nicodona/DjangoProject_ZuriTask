from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('''<h1 style="color:slategray">hi django this is my new <span style="color: black">zuri task</span> project</h1>'
                        <h2> I love zuri </h2>
                        <a href ="https://i4g.zuriboard.com/"> this is zuri link</a>
                        <p> this page is written using http response</p>
                        
                       ''' )

def log(request):
    return render(request, 'log.html', {'django welcomes you':'myname'})
