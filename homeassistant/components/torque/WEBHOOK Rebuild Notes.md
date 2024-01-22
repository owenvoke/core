# Migration to Webhook in progress

To implement, we will need to register a webhook on the [__init__.py](./__init__.py) file
Sensor Data will either need to be piped from the init file, or we'll need a callback on the [sensor.py](./sensor.py) file.

Some other notes, torque's config use email, torque uploads an ID, I need to see if torque uploads a vehicle profile name. (In case a user has multiple vehicle profiles).
If torque does upload a vehicle profile name parameter, we may want to modify the base code to also consume this parameter for unique id generation.

- [X] Outline final code
- [ ] Outline migration plan
- [ ] Migrate code 😊

# Final Code Structure

1. We need to register a webhook with the `homeassistant.components.webhook.async_register` method.
2. Similar to the existing http based implementation, we'lll need a callback to parse the webhook data from a GET request, pulling the query parameters.
3. Once we pull the query parameters, we'll need to route the data to their platform data. (For now, only sensors, but could also be binary_sensor or device_tracker)
4. platform files need to take the data and store it correctly. (Already working for sensors, so we just need to move that code)

## Step 1, registering a webhook

To register a webhook with `homeassistant.components.webhook.async_register` we'll need the following parameters:

- hass (pretty easy to access)
- DOMAIN ('torque')
- webhook_id (torque? formatted string with torque email/id, we can also generate unique ids)
- handler (Maybe we can leverage existing get callback)
- * (no idea what this is)
- local_only (I'd believe true, must investigate)
- methods (get)

Since handling multiple domains should have a coordinator implementation, this will actually be implemented on the [sensor.py](./sensor.py) file.
This will remove our need for the next step, which was to pipe the platform data

## Step 2, callback

I plan to move the existing sensor callback into it's own function
This will require a DataUpdateCoordinator class... Which is something that should be implemented on the base branch. Let's combine this step with [Step 1](#step-1-registering-a-webhook)

## Step 3, pulling data into platforms

Let's see how exisitng integrations handle this.

## Step 4, platform files

Keep code as close to existing [sensor.py](./sensor.py) as possible.
