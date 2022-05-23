# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mux_python.configuration import Configuration


class CreateSpaceRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'SpaceType',
        'passthrough': 'str',
        'broadcasts': 'list[CreateBroadcastRequest]'
    }

    attribute_map = {
        'type': 'type',
        'passthrough': 'passthrough',
        'broadcasts': 'broadcasts'
    }

    def __init__(self, type=None, passthrough=None, broadcasts=None, local_vars_configuration=None):  # noqa: E501
        """CreateSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._passthrough = None
        self._broadcasts = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if passthrough is not None:
            self.passthrough = passthrough
        if broadcasts is not None:
            self.broadcasts = broadcasts

    @property
    def type(self):
        """Gets the type of this CreateSpaceRequest.  # noqa: E501


        :return: The type of this CreateSpaceRequest.  # noqa: E501
        :rtype: SpaceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateSpaceRequest.


        :param type: The type of this CreateSpaceRequest.  # noqa: E501
        :type type: SpaceType
        """

        self._type = type

    @property
    def passthrough(self):
        """Gets the passthrough of this CreateSpaceRequest.  # noqa: E501

        Arbitrary user-supplied metadata that will be included in the space details and related webhooks. Max: 255 characters.  # noqa: E501

        :return: The passthrough of this CreateSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this CreateSpaceRequest.

        Arbitrary user-supplied metadata that will be included in the space details and related webhooks. Max: 255 characters.  # noqa: E501

        :param passthrough: The passthrough of this CreateSpaceRequest.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

    @property
    def broadcasts(self):
        """Gets the broadcasts of this CreateSpaceRequest.  # noqa: E501

        An array of broadcast destinations you want to stream the space to. **Note:** By default only a single broadcast destination can be specified. Contact Mux support if you need more.  # noqa: E501

        :return: The broadcasts of this CreateSpaceRequest.  # noqa: E501
        :rtype: list[CreateBroadcastRequest]
        """
        return self._broadcasts

    @broadcasts.setter
    def broadcasts(self, broadcasts):
        """Sets the broadcasts of this CreateSpaceRequest.

        An array of broadcast destinations you want to stream the space to. **Note:** By default only a single broadcast destination can be specified. Contact Mux support if you need more.  # noqa: E501

        :param broadcasts: The broadcasts of this CreateSpaceRequest.  # noqa: E501
        :type broadcasts: list[CreateBroadcastRequest]
        """

        self._broadcasts = broadcasts

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
