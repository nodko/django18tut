from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
from .forms import ContactForm

def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center,
	}
	if form.is_valid():

		# for key, value in form.cleaned_data.items():
		# 	print(key,value)
		# 	#print(form.cleaned_data.get(key))
		contact_full_name = form.cleaned_data.get("full_name")
		contact_email = form.cleaned_data.get("email")
		contact_message = form.cleaned_data.get("message")
		
		subject = "Site contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, "hemasagarm@gmail.com"]
		contact_message = "%s: %s via %s" %(
			contact_full_name, 
			contact_message, 
			contact_email)
		print(contact_message)
		some_html_message = """
        <h1>Hello buddy</h1>
        """
		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email,
			#html_message = some_html_message, 
			fail_silently=False)

	return render(request, "contact.html", context)