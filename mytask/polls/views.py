from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from . models import Expense
def index(request):
    return render(request,'index.html')



def submit(request):
        if request.method == 'POST':
                travel=request.POST.get('travel')
                eduction=request.POST.get('eduction')
                gifts=request.POST.get('gifts')
                investments=request.POST.get('investments')
                bills=request.POST.get('bills')
                food=request.POST.get('food')
                health=request.POST.get('health')
                personal=request.POST.get('personal')
                fees=request.POST.get('fees')
                sum=int(travel+eduction+gifts+investments+bills+food+health+personal+fees)
                if sum>5000:
                    print("you cross your montly limit")
                    Table=Expense(travel=travel,eduction=eduction, gifts=gifts, Investments=investments,Bills=bills,Food=food,Health=health,Personal=personal,fee=fees)
                    Table.save()
                else:
                    Table=Expense(travel=travel,eduction=eduction, gifts=gifts, Investments=investments,Bills=bills,Food=food,Health=health,Personal=personal,fee=fees)
                    Table.save()
        return render(request, 'submit.html')   


def show(request):
        data=Expense.objects.all()
        # print(type(data))
        # print("data"+ str(data))
        # print(data[0])
        context={'key':data}
        # print(context)
        return render(request, 'showexpence.html', context)