"""Test System Monitor sensor."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


async def test_sensor(
    hass: HomeAssistant, mock_added_config_entry: ConfigEntry
) -> None:
    """Test the sensor."""
    memory_sensor = hass.states.get("sensor.system_monitor_memory_free")
    assert memory_sensor is not None
    assert memory_sensor.state == "40.0"
