"""
celery.py
"""
from celery import Celery
from controller.settings import settings, tasks

celery = Celery(include=tasks)

# Time
celery.conf.timezone = settings.timezone
celery.conf.enable_utc = settings.utc

# Broker & Backend
celery.conf.broker_url = settings.rediss
celery.conf.result_backend = settings.rediss

# Censored
celery.conf.humanize(with_defaults=False, censored=settings.censored)
celery.conf.table(with_defaults=False, censored=settings.censored)

# Priorities
celery.conf.broker_transport_options = {
    "priority_steps": list(range(settings.priority_levels)),
    "sep": ":",
    "queue_order_strategy": "priority",
}

if __name__ == "__main__":
    celery.start()
