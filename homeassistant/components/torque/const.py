"""Constants for the Torque integration."""
import logging
from typing import Final

DOMAIN: Final = "torque"

API_PATH = "/api/torque"

ISSUE_PLACEHOLDER = {"url": "/config/integrations/dashboard/add?domain=torque"}

LOGGER = logging.getLogger(__package__)

SENSOR_EMAIL_FIELD = "eml"
SENSOR_NAME_KEY = r"userFullName(\w+)"
SENSOR_UNIT_KEY = r"userUnit(\w+)"
SENSOR_VALUE_KEY = r"k(\w+)"
