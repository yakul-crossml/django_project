from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Document
from .forms import DocumentForm
from django.contrib.auth.models import User, update_last_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime


def index(request):
    user = User.objects.get(username=request.user.username)
    user_files = Document.objects.filter(user=user)
    context = {'files': user_files}
    return render(request, 'doc_manage/index.html', context)


@login_required
def upload(request):
    doc_form = DocumentForm()
    if request.method == 'POST':
        doc_form = DocumentForm(request.POST,request.FILES)
        user = request.user.username
        user_obj = User.objects.get(username=user)
        daily_limit = Document.objects.filter(user=user_obj.pk).filter(created_at__date=timezone.now())
        users_today_uploads = daily_limit.count()
        if users_today_uploads == 5:
            messages.info(request, "You can Only upload 5 docs/day !")
            return redirect(reverse('upload'))
        else:
            if doc_form.is_valid():
                if request.FILES['pdf'].size > 5242880:
                    messages.info(request, "Size can't be more than 5 MiB")
                    return redirect(reverse('upload'))
                else:
                    doc_obj=doc_form.save(commit=False)
                    user = User.objects.get(pk=request.user.id)
                    doc_obj.user=user
                    doc_obj.save()
                    return redirect('/')
            else:
                doc_form = DocumentForm()
    
    return render(request,'doc_manage/upload.html',{'form':doc_form})



@login_required
def report(request):
    form=DocumentForm
    doc=Document.objects.all()
    if request.user.is_authenticated:
            today = datetime.date.today()
            print(today)
            current_month = datetime.date.today().month
            print(current_month)
            current_year = datetime.date.today().year
            user=request.user.id
            user_obj=User.objects.get(pk=user)
            print(user_obj)
            pdf_list=Document.objects.all().filter(user=user_obj.pk)
            print(pdf_list)
            if request.method == 'GET':
                report_type = request.GET.get('report_type')
                if report_type == 'sort_by_name':
                    user_data = Document.objects.filter(user=User.objects.get(username=request.user.username)).order_by('title')
                    return render(request, 'doc_manage/uploads.html',{'form':form,'context':user_data})
                elif report_type=='current_month':
                    user_data = Document.objects.filter(user=User.objects.get(username=request.user.username)).filter(created_at__month=current_month)
                    return render(request, 'doc_manage/uploads.html', {'form':form,'context': user_data})
                elif report_type=='current_year':
                    user_data = Document.objects.filter(user=User.objects.get(username=request.user.username)).filter(created_at__year=current_year)
                    return render(request, 'doc_manage/uploads.html', {'form':form,'context': user_data})
                elif report_type=='doc_range':
                    start_date = request.POST['startdate']
                    end_date = request.POST['enddate']
                    print(start_date,end_date)
                    user_data = Document.objects.filter(user=User.objects.get(username=request.user.username)).filter(created_at__range=[start_date, end_date])
                    print(user_data)
                    return render(request, 'doc_manage/uploads.html', {'form':form,'context': user_data})
            elif request.method=='POST':
                start_date = request.POST['startdate']
                end_date = request.POST['enddate']
                user_data = pdf_list.filter(user=request.user, created_at__range=[start_date,end_date])
                return render(request, 'doc_manage/uploads.html', {'form':form,'context': user_data})
            return render(request, 'doc_manage/uploads.html',{'form':form,'context':pdf_list})

