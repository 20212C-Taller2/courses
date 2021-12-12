import logging

from app.conf.config import settings

logging.basicConfig(
    level=settings.LOG_LEVEL
)

logger = logging.getLogger(__name__)
