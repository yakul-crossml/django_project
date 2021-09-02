from django.test import TestCase

# Create your tests here.



@login_required
def report(request):
	"""
	function to generate report of documents
	and sort by name, date, year, month
	"""
	user_docs = Document.objects.filter(user=User.objects.get(username=request.user.username))
	# breakpoint()
	daily_uploads = user_docs.filter(created_at__day=timezone.now().strftime("%d"))
	monthly_uploads = user_docs.filter(created_at__month=timezone.now().strftime("%m"))
	yearly_uploads = user_docs.filter(created_at__year=timezone.now().strftime("%Y"))

	daily_count = daily_uploads.count()
	monthly_count = monthly_uploads.count()
	yearly_count = yearly_uploads.count()
	# breakpoint()

	if 'doc_name' in request.GET:
		pdf_list = user_docs.filter(name__icontains=request.GET['doc_name'])
	elif 'month' in request.GET:
		pdf_list = user_docs.filter(created_at__month=request.GET['month'])
		# breakpoint()
	elif 'year' in request.GET:
		pdf_list = user_docs.filter(created_at__year=request.GET['year'])
	elif 'from' in request.GET and 'to' in request.GET:
		# breakpoint()
		pdf_list = user_docs.filter(created_at__range=[request.GET['from'],request.GET['to']])

	else:
		pdf_list = user_docs
	context = {'daily_count': daily_count, 'monthly_count': monthly_count, 'yearly_count': yearly_count, 'pdf_list':pdf_list}

	return render(request, 'document_manager/report.html', context)