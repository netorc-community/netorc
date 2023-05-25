"""
logger.py
"""
import logging.handlers

from settings import settings

logger = logging.getLogger(__name__)

logger.setLevel(settings.log_level)
formatter = logging.Formatter(settings.log_format)

if settings.log_console is True:
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

if settings.log_file is True:
    file = logging.handlers.RotatingFileHandler(
        filename="logs/netorc.log", mode="w", maxBytes=10000000, backupCount=5
    )
    file.setFormatter(formatter)
    logger.addHandler(file)

if settings.log_syslog is True:
    syslog = logging.handlers.SysLogHandler(
        address=(settings.syslog_server, settings.syslog_port)
    )
    syslog.setFormatter(formatter)
    logger.addHandler(syslog)
