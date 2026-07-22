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


class ConfigLoader:
    """
    Load the application configuration from a JSON file.
    """

    def load(self):
        """
        Read the configuration file and return its contents.

        Returns
        -------
        dict
            Dictionary containing all configuration values
            defined in config.json.
        """

        with open("src/config/config.json", "r") as file:
            config = json.load(file)

        return config