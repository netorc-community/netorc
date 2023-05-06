"""
logger.py
"""
import logging
from settings import settings

logger = logging.getLogger(__name__)

logger.setLevel(settings.log_level)

console = logging.StreamHandler()

file = logging.handlers.RotatingFileHandler(
    filename="logs/netorc.log", mode="w", maxBytes=10000000, backupCount=5
)

syslog = logging.handlers.SysLogHandler(
    address=(settings.syslog_server, settings.syslog_port)
)

formatter = logging.Formatter(settings.log_format)

console.setFormatter(formatter)
logger.addHandler(console)

file.setFormatter(formatter)
logger.addHandler(file)

syslog.setFormatter(formatter)
logger.addHandler(syslog)
