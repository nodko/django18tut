from django import forms

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(widget = forms.Textarea)

	# def clean_email(self):
	# 	email = (self.cleaned_data.get('email'))
	# 	email_base, provider = email.split("@")
	# 	domain, extension = provider.split(".")
	# 	# if not domain == "bit":
	# 		# raise forms.ValidationError("Please use a valid bit email address")
	# 	if not extension == "edu":
	# 		raise forms.ValidationError("Please use a valid .EDU email address")
	# 	return email