from celery import Celery

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

celery_app = Celery('src.celery_tasks',
             broker='amqp://newsgac:1234@rabbit//',
             backend='rpc://',
             include=['src.celery_tasks.tasks'])