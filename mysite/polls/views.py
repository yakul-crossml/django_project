from django.shortcuts import render
from .models import table
# from mysite import settings
# Create your views here.
def homepage(request):
        return render(request, 'index.html')
        
     
        
def submit(request):
        if request.method == 'POST':
                name=request.POST.get('name')
                document=request.POST.get('document')
                doc_type=request.POST.get('doc_type')
                link=request.POST.get('link')
                Table=table(name=name, Document_name=document, category=doc_type, link=link)
                Table.save()
        return render(request, 'submit.html')    


def show(request):
        data=table.objects.all()
        print(type(data))
        print("data"+ str(data))
        print(data[0])
        context={'key':data}
        print(context)
        return render(request, 'showtable.html', context)