""" Handler for Send email functionality:
without SMTP configures, it prints to the console
"""

from django.core.mail import send_mail
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from contacts.models import Contact


@receiver(post_delete, sender=Contact)
def send_new_contact_notification_email(sender, instance, **kwargs):

    # if a contact is removed, compose and send the email

    name = instance.name
    email = instance.email

    subject = f'NAME: {name}, Email: {email}'
    message = 'The Contact has been deleted!\n'
    message += 'NAME: ' + name + '\n' + 'EMAIL: ' \
              + email
    message += '--' * 30

    send_mail(
        subject,
        message,
        'your_email@example.com',
        ['recipeint1@xample.com', 'recipent2@xample.com '],
        fail_silently=False,
    )