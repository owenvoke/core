"""Support for Streamlabs Water Monitor Usage."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfVolume
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import StreamlabsCoordinator
from .const import DOMAIN
from .coordinator import StreamlabsData


@dataclass(frozen=True, kw_only=True)
class StreamlabsWaterSensorEntityDescription(SensorEntityDescription):
    """Streamlabs sensor entity description."""

    value_fn: Callable[[StreamlabsData], StateType]


SENSORS: tuple[StreamlabsWaterSensorEntityDescription, ...] = (
    StreamlabsWaterSensorEntityDescription(
        key="daily_usage",
        translation_key="daily_usage",
        native_unit_of_measurement=UnitOfVolume.GALLONS,
        device_class=SensorDeviceClass.WATER,
        value_fn=lambda data: data.daily_usage,
    ),
    StreamlabsWaterSensorEntityDescription(
        key="monthly_usage",
        translation_key="monthly_usage",
        native_unit_of_measurement=UnitOfVolume.GALLONS,
        device_class=SensorDeviceClass.WATER,
        value_fn=lambda data: data.monthly_usage,
    ),
    StreamlabsWaterSensorEntityDescription(
        key="yearly_usage",
        translation_key="yearly_usage",
        native_unit_of_measurement=UnitOfVolume.GALLONS,
        device_class=SensorDeviceClass.WATER,
        value_fn=lambda data: data.yearly_usage,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Streamlabs water sensor from a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        StreamLabsSensor(coordinator, location_id, entity_description)
        for location_id in coordinator.data
        for entity_description in SENSORS
    )


class StreamLabsSensor(CoordinatorEntity[StreamlabsCoordinator], SensorEntity):
    """Monitors the daily water usage."""

    _attr_has_entity_name = True

    entity_description: StreamlabsWaterSensorEntityDescription

    def __init__(
        self,
        coordinator: StreamlabsCoordinator,
        location_id: str,
        entity_description: StreamlabsWaterSensorEntityDescription,
    ) -> None:
        """Initialize the daily water usage device."""
        super().__init__(coordinator)
        self._location_id = location_id
        self._attr_unique_id = f"{location_id}-{entity_description.key}"
        self.entity_description = entity_description
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, location_id)}, name=self.location_data.name
        )

    @property
    def location_data(self) -> StreamlabsData:
        """Returns the data object."""
        return self.coordinator.data[self._location_id]

    @property
    def native_value(self) -> StateType:
        """Return the current daily usage."""
        return self.entity_description.value_fn(self.location_data)
