from celery import shared_task
from PIL import Image
import os
from django.conf import settings
from recipe_management.models import Recipe
from celery import shared_task
from django.core.mail import send_mail
import datetime

@shared_task
def compress_image_task(recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    image_path = os.path.join(settings.MEDIA_ROOT, recipe.image.name)

    with Image.open(image_path) as img:
        img = img.convert('RGB')
        img.save(image_path, 'JPEG', optimize=True, quality=60)

@shared_task
def send_daily_email():
    today = datetime.datetime.today().weekday()
    if today < 5:
        send_mail(
            subject="Daily Recipe Digest",
            message="Here's your daily recipe update!",
            from_email="kajalcodecraft@example.com",
            recipient_list=["itscuriousone@example.com"],
        )
