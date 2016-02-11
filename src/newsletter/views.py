from django.shortcuts import render
from .forms import SignUpForm
from .models import SignUp
# Create your views here.
def home(request):

	title = "Join Us / Signup Now "
	
	# if request.user.is_authenticated():
	# 	title = "Title context %s" %(request.user)
	
	# if request.method == "POST":
	# 	print(request.POST)

	form = SignUpForm(request.POST or None)
	context = {
	    "template_title": title,
	    "form": form,
	}
	
	if form.is_valid():
		#form.save()
		#print(request.POST["email"]) # not recomended
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "John Doe"
		instance.save()
		context = {
	        "template_title":"Thank you"
	    }

	if request.user.is_authenticated() and request.user.is_staff:
		# print(SignUp.objects.all())
		# i = 1
		# for instances in SignUp.objects.all():
		# 	print(i)
		# 	print(instances.full_name)
		# 	i += 1
		# queryset = SignUp.objects.all().order_by('-timestamp')
		queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="sagar")
		# print(SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="sagar").count())
		context = {
		    "queryset": queryset
		}

	return render(request, "home.html", context)