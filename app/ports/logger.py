import logging.config

from app.conf.config import settings

logging.config.fileConfig('app/conf/logging.conf', disable_existing_loggers=False)
logging.basicConfig(
    level=settings.LOG_LEVEL
)

logger = logging.getLogger(__name__)
