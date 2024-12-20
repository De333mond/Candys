from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.models import Product, Customer


@receiver(post_save, sender=Product)
def send_product_on_sale_email(sender, instance: Product, created, **kwargs):
    if not created and instance.adv_state == 'sale':
        customers = Customer.objects.filter(get_email=True)

        send_mail(
            'Welcome!',
            f'The {instance.title} now on sale!',
            'no-reply@example.com',
            [customer.user.email for customer in customers]
        )
