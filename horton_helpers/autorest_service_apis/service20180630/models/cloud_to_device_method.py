# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudToDeviceMethod(Model):
    """Parameters to execute a direct method on the device.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param method_name: Method to run
    :type method_name: str
    :ivar payload: Payload
    :vartype payload: object
    :param response_timeout_in_seconds:
    :type response_timeout_in_seconds: int
    :param connect_timeout_in_seconds:
    :type connect_timeout_in_seconds: int
    """

    _validation = {
        'payload': {'readonly': True},
    }

    _attribute_map = {
        'method_name': {'key': 'methodName', 'type': 'str'},
        'payload': {'key': 'payload', 'type': 'object'},
        'response_timeout_in_seconds': {'key': 'responseTimeoutInSeconds', 'type': 'int'},
        'connect_timeout_in_seconds': {'key': 'connectTimeoutInSeconds', 'type': 'int'},
    }

    def __init__(self, method_name=None, response_timeout_in_seconds=None, connect_timeout_in_seconds=None):
        super(CloudToDeviceMethod, self).__init__()
        self.method_name = method_name
        self.payload = None
        self.response_timeout_in_seconds = response_timeout_in_seconds
        self.connect_timeout_in_seconds = connect_timeout_in_seconds
