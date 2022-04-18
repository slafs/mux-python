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


class UpdateLiveStreamRequest(object):
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
        'passthrough': 'str',
        'latency_mode': 'str',
        'reconnect_window': 'float',
        'max_continuous_duration': 'int'
    }

    attribute_map = {
        'passthrough': 'passthrough',
        'latency_mode': 'latency_mode',
        'reconnect_window': 'reconnect_window',
        'max_continuous_duration': 'max_continuous_duration'
    }

    def __init__(self, passthrough=None, latency_mode=None, reconnect_window=None, max_continuous_duration=43200, local_vars_configuration=None):  # noqa: E501
        """UpdateLiveStreamRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._passthrough = None
        self._latency_mode = None
        self._reconnect_window = None
        self._max_continuous_duration = None
        self.discriminator = None

        if passthrough is not None:
            self.passthrough = passthrough
        if latency_mode is not None:
            self.latency_mode = latency_mode
        if reconnect_window is not None:
            self.reconnect_window = reconnect_window
        if max_continuous_duration is not None:
            self.max_continuous_duration = max_continuous_duration

    @property
    def passthrough(self):
        """Gets the passthrough of this UpdateLiveStreamRequest.  # noqa: E501

        Arbitrary user-supplied metadata set for the live stream. Max 255 characters. In order to clear this value, the field should be included with an empty-string value.  # noqa: E501

        :return: The passthrough of this UpdateLiveStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this UpdateLiveStreamRequest.

        Arbitrary user-supplied metadata set for the live stream. Max 255 characters. In order to clear this value, the field should be included with an empty-string value.  # noqa: E501

        :param passthrough: The passthrough of this UpdateLiveStreamRequest.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

    @property
    def latency_mode(self):
        """Gets the latency_mode of this UpdateLiveStreamRequest.  # noqa: E501

        Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this as an alternative to setting low latency or reduced latency flags. The Low Latency value is a beta feature. Note: Reconnect windows are incompatible with Reduced Latency and Low Latency and will always be set to zero (0) seconds. Read more here: https://mux.com/blog/introducing-low-latency-live-streaming/  # noqa: E501

        :return: The latency_mode of this UpdateLiveStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._latency_mode

    @latency_mode.setter
    def latency_mode(self, latency_mode):
        """Sets the latency_mode of this UpdateLiveStreamRequest.

        Latency is the time from when the streamer transmits a frame of video to when you see it in the player. Set this as an alternative to setting low latency or reduced latency flags. The Low Latency value is a beta feature. Note: Reconnect windows are incompatible with Reduced Latency and Low Latency and will always be set to zero (0) seconds. Read more here: https://mux.com/blog/introducing-low-latency-live-streaming/  # noqa: E501

        :param latency_mode: The latency_mode of this UpdateLiveStreamRequest.  # noqa: E501
        :type latency_mode: str
        """
        allowed_values = ["low", "reduced", "standard"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and latency_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `latency_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(latency_mode, allowed_values)
            )

        self._latency_mode = latency_mode

    @property
    def reconnect_window(self):
        """Gets the reconnect_window of this UpdateLiveStreamRequest.  # noqa: E501

        When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset.  # noqa: E501

        :return: The reconnect_window of this UpdateLiveStreamRequest.  # noqa: E501
        :rtype: float
        """
        return self._reconnect_window

    @reconnect_window.setter
    def reconnect_window(self, reconnect_window):
        """Sets the reconnect_window of this UpdateLiveStreamRequest.

        When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset.  # noqa: E501

        :param reconnect_window: The reconnect_window of this UpdateLiveStreamRequest.  # noqa: E501
        :type reconnect_window: float
        """
        if (self.local_vars_configuration.client_side_validation and
                reconnect_window is not None and reconnect_window > 300):  # noqa: E501
            raise ValueError("Invalid value for `reconnect_window`, must be a value less than or equal to `300`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reconnect_window is not None and reconnect_window < 0.1):  # noqa: E501
            raise ValueError("Invalid value for `reconnect_window`, must be a value greater than or equal to `0.1`")  # noqa: E501

        self._reconnect_window = reconnect_window

    @property
    def max_continuous_duration(self):
        """Gets the max_continuous_duration of this UpdateLiveStreamRequest.  # noqa: E501

        The time in seconds a live stream may be continuously active before being disconnected. Defaults to 12 hours.  # noqa: E501

        :return: The max_continuous_duration of this UpdateLiveStreamRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_continuous_duration

    @max_continuous_duration.setter
    def max_continuous_duration(self, max_continuous_duration):
        """Sets the max_continuous_duration of this UpdateLiveStreamRequest.

        The time in seconds a live stream may be continuously active before being disconnected. Defaults to 12 hours.  # noqa: E501

        :param max_continuous_duration: The max_continuous_duration of this UpdateLiveStreamRequest.  # noqa: E501
        :type max_continuous_duration: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_continuous_duration is not None and max_continuous_duration > 43200):  # noqa: E501
            raise ValueError("Invalid value for `max_continuous_duration`, must be a value less than or equal to `43200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_continuous_duration is not None and max_continuous_duration < 60):  # noqa: E501
            raise ValueError("Invalid value for `max_continuous_duration`, must be a value greater than or equal to `60`")  # noqa: E501

        self._max_continuous_duration = max_continuous_duration

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
        if not isinstance(other, UpdateLiveStreamRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateLiveStreamRequest):
            return True

        return self.to_dict() != other.to_dict()
