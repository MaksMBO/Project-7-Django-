from django.core.mail import send_mail
from django.template.loader import render_to_string

from flowerStore.settings import EMAIL_HOST_USER


def subscribe_user(email: str) -> None:
    """
    Надсилає електронний лист для підписки користувача на розсилку.
    """
    html_message = render_to_string('emails/subscribe_email.html')
    send_async_email(email, html_message)

def send_async_email(email: str, html_message: str) -> None:
    """
    Надсилає електронний лист.
    """ 
    send_mail(
        'Lystva',
        '',
        EMAIL_HOST_USER,
        [email],
        html_message=html_message,
        fail_silently=False
    )