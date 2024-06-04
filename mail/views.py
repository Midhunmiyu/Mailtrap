from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail import send_mail


class IndexView(TemplateView):
    template_name = 'index.html'


class SendEmailView(View):
    def post(self, request, *args, **kwargs):
        
        name = request.POST['name']
        email = request.POST['email']

        subject = 'New Form Submission'
        message_body = f'Name: {name}\nEmail: {email}'  # Use \n for newlines in email body
        from_email = email
        to_email = 'midhunrajagopal1@gmail.com'

        try:
            send_mail(subject, message_body, from_email, [to_email])
            messages.info(request, "Your Request Shared Successfully")
            return redirect('/')  # Redirect on success

        except Exception as e:
            # Handle exceptions here (e.g., logging error, displaying user-friendly message)
            messages.error(request, f"Error sending email: {str(e)}")
            return render(request, 'index.html')

