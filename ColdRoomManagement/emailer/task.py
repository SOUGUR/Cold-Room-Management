# emailer/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from inventory.models import Material
from emailer.models import SentEmail
from django.contrib.auth.models import User

@shared_task
def send_materials_email_task():
    today = timezone.now().date()
    first_day_of_next_month = (today.replace(day=1) + timedelta(days=32)).replace(day=1)
    last_day_of_current_month = first_day_of_next_month - timedelta(days=1)
    send_date = last_day_of_current_month - timedelta(days=10)
    
    if today == send_date:
        materials = Material.objects.all()
        material_list = "\n".join([f"{m.product_id} - {m.name} - {m.quantity} - {m.expiry_date}" for m in materials])
        
        subject = 'List of Materials in Cold Room'
        message = f"Here is the list of materials in the cold room:\n\n{material_list}"
        recipients = User.objects.values_list('email', flat=True)  # Get all user emails
        recipients_list = list(filter(None, recipients))  # Filter out empty email addresses
            
        if recipients_list:
            send_mail(subject, message, 'sourabhgurav@gmail.com', recipients_list)
                
            SentEmail.objects.create(subject=subject, body=message, recipients=", ".join(recipients_list))
                
        