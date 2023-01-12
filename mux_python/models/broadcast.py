# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from mux_python.configuration import Configuration


class Broadcast(object):
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
        'id': 'str',
        'passthrough': 'str',
        'live_stream_id': 'str',
        'status': 'BroadcastStatus',
        'layout': 'BroadcastLayout',
        'background': 'str',
        'resolution': 'BroadcastResolution'
    }

    attribute_map = {
        'id': 'id',
        'passthrough': 'passthrough',
        'live_stream_id': 'live_stream_id',
        'status': 'status',
        'layout': 'layout',
        'background': 'background',
        'resolution': 'resolution'
    }

    def __init__(self, id=None, passthrough=None, live_stream_id=None, status=None, layout=None, background=None, resolution=None, local_vars_configuration=None):  # noqa: E501
        """Broadcast - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._passthrough = None
        self._live_stream_id = None
        self._status = None
        self._layout = None
        self._background = None
        self._resolution = None
        self.discriminator = None

        self.id = id
        if passthrough is not None:
            self.passthrough = passthrough
        self.live_stream_id = live_stream_id
        self.status = status
        self.layout = layout
        if background is not None:
            self.background = background
        self.resolution = resolution

    @property
    def id(self):
        """Gets the id of this Broadcast.  # noqa: E501

        Unique identifier for the broadcast. Max 255 characters.  # noqa: E501

        :return: The id of this Broadcast.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Broadcast.

        Unique identifier for the broadcast. Max 255 characters.  # noqa: E501

        :param id: The id of this Broadcast.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def passthrough(self):
        """Gets the passthrough of this Broadcast.  # noqa: E501

        Arbitrary user-supplied metadata that will be included in the broadcast details and related webhooks. Max: 255 characters.  # noqa: E501

        :return: The passthrough of this Broadcast.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this Broadcast.

        Arbitrary user-supplied metadata that will be included in the broadcast details and related webhooks. Max: 255 characters.  # noqa: E501

        :param passthrough: The passthrough of this Broadcast.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

    @property
    def live_stream_id(self):
        """Gets the live_stream_id of this Broadcast.  # noqa: E501

        The ID of the live stream that the broadcast will be sent to.  # noqa: E501

        :return: The live_stream_id of this Broadcast.  # noqa: E501
        :rtype: str
        """
        return self._live_stream_id

    @live_stream_id.setter
    def live_stream_id(self, live_stream_id):
        """Sets the live_stream_id of this Broadcast.

        The ID of the live stream that the broadcast will be sent to.  # noqa: E501

        :param live_stream_id: The live_stream_id of this Broadcast.  # noqa: E501
        :type live_stream_id: str
        """
        if self.local_vars_configuration.client_side_validation and live_stream_id is None:  # noqa: E501
            raise ValueError("Invalid value for `live_stream_id`, must not be `None`")  # noqa: E501

        self._live_stream_id = live_stream_id

    @property
    def status(self):
        """Gets the status of this Broadcast.  # noqa: E501


        :return: The status of this Broadcast.  # noqa: E501
        :rtype: BroadcastStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Broadcast.


        :param status: The status of this Broadcast.  # noqa: E501
        :type status: BroadcastStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def layout(self):
        """Gets the layout of this Broadcast.  # noqa: E501


        :return: The layout of this Broadcast.  # noqa: E501
        :rtype: BroadcastLayout
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this Broadcast.


        :param layout: The layout of this Broadcast.  # noqa: E501
        :type layout: BroadcastLayout
        """
        if self.local_vars_configuration.client_side_validation and layout is None:  # noqa: E501
            raise ValueError("Invalid value for `layout`, must not be `None`")  # noqa: E501

        self._layout = layout

    @property
    def background(self):
        """Gets the background of this Broadcast.  # noqa: E501

        URL of an image to display as the background of the broadcast. Its dimensions should match the provided resolution.  # noqa: E501

        :return: The background of this Broadcast.  # noqa: E501
        :rtype: str
        """
        return self._background

    @background.setter
    def background(self, background):
        """Sets the background of this Broadcast.

        URL of an image to display as the background of the broadcast. Its dimensions should match the provided resolution.  # noqa: E501

        :param background: The background of this Broadcast.  # noqa: E501
        :type background: str
        """

        self._background = background

    @property
    def resolution(self):
        """Gets the resolution of this Broadcast.  # noqa: E501


        :return: The resolution of this Broadcast.  # noqa: E501
        :rtype: BroadcastResolution
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this Broadcast.


        :param resolution: The resolution of this Broadcast.  # noqa: E501
        :type resolution: BroadcastResolution
        """
        if self.local_vars_configuration.client_side_validation and resolution is None:  # noqa: E501
            raise ValueError("Invalid value for `resolution`, must not be `None`")  # noqa: E501

        self._resolution = resolution

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
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
        if not isinstance(other, Broadcast):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Broadcast):
            return True

        return self.to_dict() != other.to_dict()
