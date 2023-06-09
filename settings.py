"""
NetORC configuration file.

We have kept the default connection and secret parameters used by modules in this file.
This is not best practice, we recommend overriding these using a .env or a secret manager, see: <link>

"""
import os

from pydantic import BaseSettings, RedisDsn, DirectoryPath, PostgresDsn


class Settings(BaseSettings):
    """NetORC settings management"""

    # Header key used for authentication.
    api_key_header = "netorc-x-token"

    # We recommend changing the postgres db credentials.
    database: PostgresDsn = "postgresql://netorc:netorc123@netorc-postgres:5432/netorc"

    # We recommend changing the redis credentials.
    redis: RedisDsn = "redis://netorc-redis:6379"  # TODO: redis or rediss

    # Check this is the correct timezone.
    timezone: str = "Europe/London"
    utc: bool = True

    # Censors celery configuration, passwords, api keys.
    # We do NOT recommend to change this setting.
    censored: bool = True

    # Tasks can be queued with a priority.
    # This is "best effort" and does not guarantee a faster execution.
    # We do NOT recommend to change this setting.
    priority_levels: int = 10  # 0-9

    # Log outputs
    log_console: bool = True
    log_file: bool = True
    log_syslog: bool = True

    # The default log level is set to info.
    # To change this value, see: https://docs.python.org/3/library/logging.html#logging-levels
    log_level: int = 20
    log_format: str = "%(asctime)s %(levelname)s: %(message)s"

    # Syslog messages are sent using UDP, for TCP, see <link>.
    # LOG_USER facility.
    syslog_server: str = "localhost"
    syslog_port: int = 514

    # Default task directory.
    task_dir: DirectoryPath = "worker/tasks"

    class Config:
        """Modify the behaviour of settings management"""

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

tasks = [
    (str(settings.task_dir) + "/" + x).replace("/", ".").strip(".py")
    for x in os.listdir(str(settings.task_dir))
    if not x.startswith("__") and x.endswith(".py")
]
