from asyncio.log import logger
from celery import shared_task
from time import sleep
from .email import send_review_email
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def send_review_email_task(name, email, review):
    logger.info('i don finish work')
    return send_review_email(name, email, review)


@shared_task
def sleepy(duration):
    sleep(duration)
    return 'I am done'


