from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from playground.tasks import notify_customers
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
import requests


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


# def say_hello(request):
#     notify_customers.delay("Hiiii")
#     return render(request, "hello.html", {"name": "Mosh"})

# caching
# def say_hello(request):
#     key = "httpbin_result"
#     if cache.get(key) is None:
#         response = requests.get("https://httpbin.org/delay/2")
#         data = response.json()
#         cache.set(key, data)
#     return render(request, "hello.html", {"name": cache.get(key)})


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get("https://httpbin.org/delay/2")
        data = response.json()
        return render(request, "hello.html", {"name": data})


# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get("https://httpbin.org/delay/2")
#     data = response.json()
#     return render(request, "hello.html", {"name": data})
