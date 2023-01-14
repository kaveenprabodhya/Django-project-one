from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage

from playground.tasks import notify_customers


# def say_hello(request):
#     try:
#         # send_mail("subject", "message", "info@kbuy.com", ["bob@kbuy.com"])
#         # mail_admins("subject", "message", html_message="message")

#         # attach a file
#         # message = EmailMessage("subject", "message", "from@kbuy.com", ["john@bob.com"])
#         # message.attach_file("playground/static/images/dog.jpg")
#         # message.send()

#         # template
#         message = BaseEmailMessage(
#             template_name="emails/hello.html", context={"name": "Kaveen"}
#         )
#         message.send(["john@kbuy.com"])
#     except BadHeaderError:
#         pass
#     return render(request, "hello.html", {"name": "Mosh"})


def say_hello(request):
    notify_customers.delay("Hiiii")
    return render(request, "hello.html", {"name": "Mosh"})
