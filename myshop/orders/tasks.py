from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from celery import shared_task
from django.core.mail.message import EmailMultiAlternatives


@shared_task
def order_created(order_id):
    """
    Задание по отправке уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order N. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order. Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'basingerfelix17@gmail.com',
                          [order.email])
    return mail_sent
