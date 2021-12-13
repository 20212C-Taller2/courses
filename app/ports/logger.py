import logging.config

from app.dependencies import get_settings

logging.config.fileConfig('app/conf/logging.conf', disable_existing_loggers=False)
logging.basicConfig(
    level=get_settings().LOG_LEVEL
)

logger = logging.getLogger(__name__)
