"""
NetORC configuration file.

We have kept connection and secret prameters used by modules in this file.
This is not best practice, we recommend using a .env or a secret manager, see: <link>

"""
import os

# Default API Key Header
API_KEY_HEADER = "netorc-x-token"

# List of Allowed API Keys
API_KEYS = []

# We do NOT recommended to change this setting.
REDIS = "redis://redis:6379"

# Ensure this is the correct timezone.
TIMEZONE = "Europe/London"

UTC = True

# Censors celery configuration, passwords, api keys.
# We do NOT recommended to change this setting.
CENSORED = True

# Tasks can be queued with a priority.
# This is best effort and does not guarantee a faster execution.
# We do NOT recommended to change this setting.
PRIORITY_LEVELS = 10  # 0-9

# The default log level is set to info.
# To change this value, see: https://docs.python.org/3/library/logging.html#logging-levels
LOG_LEVEL = 20

# The default log handlers are console, file and syslog.
LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"

# Syslog messages are sent using UDP, for TCP, see <link>.
# LOG_USER facility.
SYSLOG_SERVER = "localhost"
SYSLOG_PORT = 514

# Default task directory.
TASK_DIR = "controller/worker/tasks/"

TASKS = [
    (TASK_DIR + x).replace("/", ".").strip(".py")
    for x in os.listdir(TASK_DIR)
    if not x.startswith("__") and x.endswith(".py")
]
