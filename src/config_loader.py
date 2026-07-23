"""
config_loader.py

Configuration Loader

This module is responsible for loading the project configuration
from a JSON file.

The configuration file keeps project settings outside the source
code, making the application easier to configure without modifying
Python files.
"""

import json
from logger import logger

class ConfigLoader:
    """
    Load the application configuration from a JSON file.
    """

    def load(self):
        """
            Load the application configuration.

            Returns
            -------
            dict
                Parsed JSON configuration.
        """
        try:
            with open("src/config/config.json", "r") as file:
                config = json.load(file)
                logger.info("Configuration loaded.")
                return config
            
        except FileNotFoundError:
            logger.exception("Configuration file not found.")