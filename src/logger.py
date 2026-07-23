import logging

"""
Application logging configuration.

This module creates and configures the project's shared logger.
"""

logging.basicConfig(
    filename="logger.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)