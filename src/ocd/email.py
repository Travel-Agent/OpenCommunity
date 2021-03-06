from django.core.mail import get_connection
from django.core.mail.message import EmailMultiAlternatives


def send_mails(from_email, emails, subject, message, html_message=None,
               fail_silently=False, connection=None):

    connection = connection or get_connection(fail_silently=fail_silently)

    alts = [(html_message, 'text/html')] if html_message else None

    messages = [EmailMultiAlternatives(subject, message, from_email, [email],
                                       alternatives=alts,
                connection=connection) for email in emails]
    return connection.send_messages(messages)

