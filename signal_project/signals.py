from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Students
# from django.contrib.auth.models import User
import os
from django.conf import settings


User = settings.AUTH_USER_MODEL





# instance on nemoneyi hast ke sakhte shode jadid ya kari rosh anjam shode
@receiver(post_save, sender=Students)
def create_student(sender, instance, created, **kwargs):
    if created:
        instance.students_code = "0000"
        instance.save()
        os.mkdir(f"students/{instance.name} {instance.family}")
    

@receiver(post_delete, sender=Students)
def delete_student(sender, instance, **kwargs):
    print("deleted")



@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, *args, **kwargs):
    print(args, kwargs)


# post_save.connect(user_created_handler, sender=User)


# Second way instead of decorator
# post_save.connect(create_student, sender=Students)


