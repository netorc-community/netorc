"""
logger.py
"""
import logging
from controller.settings import netorc

logger = logging.getLogger(__name__)

logger.setLevel(netorc.log_level)

console = logging.StreamHandler()

file = logging.handlers.RotatingFileHandler(
    filename="logs/netorc.log", mode="w", maxBytes=10000000, backupCount=5
)

syslog = logging.handlers.SysLogHandler(
    address=(netorc.syslog_server, netorc.syslog_port)
)

formatter = logging.Formatter(netorc.log_format)

console.setFormatter(formatter)
logger.addHandler(console)

file.setFormatter(formatter)
logger.addHandler(file)

syslog.setFormatter(formatter)
logger.addHandler(syslog)
