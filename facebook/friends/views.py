from django.shortcuts import render

# Create your views here.
def fb(request):
return render(request,'friends/friendbook.html')