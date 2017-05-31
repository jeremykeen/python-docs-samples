# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import os

import manager


# TODO: Pull from environment
DEVICE_ID = 'test-device' # TODO: unique?
PROJECT_ID = '' # TODO: Use environment variable
REGISTRY_ID = 'test-registry-{}'.format(int(time.time()))
TOPIC_ID = 'device-events'

PUBSUB_TOPIC = 'projects/{}/topics/{}'.format(PROJECT_ID, TOPIC_ID)

API_KEY = '' # TODO: Encrypt / use access token
SERVICE_ACCOUNT_JSON = '' # TODO: Use environment variable

CLOUD_REGION = 'us-central1'

# TODO: begin - create pubsub topic
# TODO: end - destroy pubsub topic

def test_create(capsys):
    manager.open_registry(
            SERVICE_ACCOUNT_JSON, API_KEY, PROJECT_ID, CLOUD_REGION,
            PUBSUB_TOPIC, REGISTRY_ID)

    manager.list_devices(
            SERVICE_ACCOUNT_JSON, API_KEY, PROJECT_ID, CLOUD_REGION,
            REGISTRY_ID)

    out, _ = capsys.readouterr()

    # Check that create / list worked
    assert 'Created registry' in out
    assert 'eventNotificationConfig' in out

    # Clean up
    manager.delete_registry(
            SERVICE_ACCOUNT_JSON, API_KEY, PROJECT_ID, CLOUD_REGION,
            REGISTRY_ID)

# TODO: Make these tests
"""
    # Lookup or create the registry.
    print 'Creating registry', registry_id, 'in project', args.project_id
    device_registry = DeviceRegistry(
            args.project_id, registry_id, args.cloud_region,
            args.service_account_json, args.api_key, args.pubsub_topic)

    # List devices for the (empty) registry
    print('Current devices in the registry:')
    for device in device_registry.list_devices():
        print device

    # Create an RS256 authenticated device. Note that for security, it is very
    # important that you use unique public/private key pairs for each device
    # (do not reuse a key pair for multiple devices). This way if a private key
    # is compromised, only a single device will be affected.
    rs256_device_id = 'rs256-device'
    print('Creating RS256 authenticated device', rs256_device_id)
    device_registry.create_device_with_rs256(
            rs256_device_id, args.rsa_certificate_file)

    # Create an ES256 authenticated device. To demonstrate updating a device,
    # we will create the device with no authentication, and then update it to
    # use ES256 for authentication. Note that while one can create a device
    # without authentication, the MQTT client will not be able to connect to
    # it.
    es256_device_id = 'es256-device'
    print('Creating device without authentication', es256_device_id)
    device_registry.create_device_with_no_auth(es256_device_id)

    # Now list devices again
    print('Current devices in the registry:')
    for device in device_registry.list_devices():
        print(device)

    # Patch the device with authentication
    print('Updating device', es256_device_id, 'to use ES256 authentication.')
    device_registry.patch_es256_for_auth(
            es256_device_id, args.ec_public_key_file)

    # Now list devices again
    print('Current devices in the registry:')
    for device in device_registry.list_devices():
        print(device)

    # Delete the ES256 device
    print('Deleting device', es256_device_id)
    device_registry.delete_device(es256_device_id)

    # List devices - will only show the RS256 device.
    print('Current devices in the registry:')
    for device in device_registry.list_devices():
        print(device)

    # Try to delete the registry. This will fail however, since the registry is
    # not empty.
    print('Trying to delete non-empty registry')
    try:
        device_registry.delete()
    except HttpError as e:
        # This will say that the registry is not empty.
        print(e)

    # Delete the RSA devices from the registry
    print('Deleting device', rs256_device_id)
    device_registry.delete_device(rs256_device_id)

    # Now actually delete registry
    print('Deleting registry')
    device_registry.delete()

    print 'Completed successfully. Goodbye!'
"""
