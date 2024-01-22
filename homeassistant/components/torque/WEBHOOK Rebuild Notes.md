# Migration to Webhook in progress

To implement, we will need to register a webhook on the [__init__.py](./__init__.py) file
Sensor Data will either need to be piped from the init file, or we'll need a callback on the [sensor.py](./sensor.py) file.

Some other notes, torque's config use email, torque uploads an ID, I need to see if torque uploads a vehicle profile name. (In case a user has multiple vehicle profiles).
If torque does upload a vehicle profile name parameter, we may want to modify the base code to also consume this parameter for unique id generation.

- [ ] Outline final code
- [ ] Outline migration plan
- [ ] Migrate code 😊