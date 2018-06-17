from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def registered(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the Picky-Bucket clan!'

    sender = 'pickybuckets@gmail.com'


    text_content = render_to_string('email/subscribemail.txt',{"name": name})
    html_content = render_to_string('email/subscribemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()