from celery.decorators import task
from celery.utils.log import get_task_logger
from .email import send_review_email

from celery import shared_task
from time import sleep

logger = get_task_logger(__name__)




@shared_task
def sleepy(id):
    sleep(1)
    print("id of the image= ")
    return id
