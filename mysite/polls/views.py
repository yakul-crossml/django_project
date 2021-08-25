from django.shortcuts import render
from .models import table
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

class IndexView(generic.ListView):
    model = table
    template_name = 'showtable.html'
    context_object_name = 'list'
    # context_object_name = 'latest_question_list'
    # def homepage(request):
    # return render(request, 'index.html')
        

    def get_queryset(self):
        """Return the last five published questions."""
        return table.objects.all()













# # from mysite import settings
# # Create your views here.
def homepage(request):
        return render(request, 'index.html')
        
     
        
# def submit(request):
#         if request.method == 'POST':
#                 name=request.POST.get('name')
#                 document=request.POST.get('document')
#                 doc_type=request.POST.get('doc_type')
#                 link=request.POST.get('link')
#                 Table=table(name=name, Document_name=document, category=doc_type, link=link)
#                 Table.save()
#         return render(request, 'submit.html')    


# def show(request):
#         data=table.objects.all()
#         print(type(data))
#         print("data"+ str(data))
#         print(data[0])
#         context={'key':data}
#         print(context)
#         return render(request, 'showtable.html', context)