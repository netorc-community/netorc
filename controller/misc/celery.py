"""
celery.py
"""
from celery import Celery
from controller.settings import netorc, tasks

celery = Celery(include=tasks)

# Time
celery.conf.timezone = netorc.timezone
celery.conf.enable_utc = netorc.utc

# Broker & Backend
celery.conf.broker_url = netorc.rediss
celery.conf.result_backend = netorc.rediss

# Censored
celery.conf.humanize(with_defaults=False, censored=netorc.censored)
celery.conf.table(with_defaults=False, censored=netorc.censored)

# Priorities
celery.conf.broker_transport_options = {
    "priority_steps": list(range(netorc.priority_levels)),
    "sep": ":",
    "queue_order_strategy": "priority",
}

if __name__ == "__main__":
    celery.start()
