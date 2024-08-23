# emailer/management/commands/send_materials_email.py
from django.core.management.base import BaseCommand
from emailer.task import send_materials_email_task

class Command(BaseCommand):
    help = 'Send an email with the list of materials 10 days before the end of the current month'

    def handle(self, *args, **kwargs):
        send_materials_email_task.apply()
