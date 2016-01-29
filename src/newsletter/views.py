from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def home(request):

	title = "welcome"
	
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
	return render(request, "example_fluid.html", context)