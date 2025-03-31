from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from tasks.models import Task
from datetime import timedelta

class Command(BaseCommand):
    help = 'Send email reminders for tasks with due dates approaching'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        upcoming_tasks = Task.objects.filter(due_date__lte=today + timedelta(days=1), completed=False)
        
        for task in upcoming_tasks:
            send_mail(
                subject=f'Reminder: Task "{task.title}" is due tomorrow',
                message=f'This is a reminder that the task "{task.title}" is due tomorrow.',
                from_email='noreply@taskmanager.com',
                recipient_list=[task.user.email]
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully sent email reminders'))
