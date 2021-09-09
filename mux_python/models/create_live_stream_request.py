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


class CreateLiveStreamRequest(object):
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
        'playback_policy': 'list[PlaybackPolicy]',
        'new_asset_settings': 'CreateAssetRequest',
        'reconnect_window': 'float',
        'passthrough': 'str',
        'audio_only': 'bool',
        'reduced_latency': 'bool',
        'low_latency': 'bool',
        'test': 'bool',
        'simulcast_targets': 'list[CreateSimulcastTargetRequest]'
    }

    attribute_map = {
        'playback_policy': 'playback_policy',
        'new_asset_settings': 'new_asset_settings',
        'reconnect_window': 'reconnect_window',
        'passthrough': 'passthrough',
        'audio_only': 'audio_only',
        'reduced_latency': 'reduced_latency',
        'low_latency': 'low_latency',
        'test': 'test',
        'simulcast_targets': 'simulcast_targets'
    }

    def __init__(self, playback_policy=None, new_asset_settings=None, reconnect_window=None, passthrough=None, audio_only=None, reduced_latency=None, low_latency=None, test=None, simulcast_targets=None, local_vars_configuration=None):  # noqa: E501
        """CreateLiveStreamRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._playback_policy = None
        self._new_asset_settings = None
        self._reconnect_window = None
        self._passthrough = None
        self._audio_only = None
        self._reduced_latency = None
        self._low_latency = None
        self._test = None
        self._simulcast_targets = None
        self.discriminator = None

        if playback_policy is not None:
            self.playback_policy = playback_policy
        if new_asset_settings is not None:
            self.new_asset_settings = new_asset_settings
        if reconnect_window is not None:
            self.reconnect_window = reconnect_window
        if passthrough is not None:
            self.passthrough = passthrough
        if audio_only is not None:
            self.audio_only = audio_only
        if reduced_latency is not None:
            self.reduced_latency = reduced_latency
        if low_latency is not None:
            self.low_latency = low_latency
        if test is not None:
            self.test = test
        if simulcast_targets is not None:
            self.simulcast_targets = simulcast_targets

    @property
    def playback_policy(self):
        """Gets the playback_policy of this CreateLiveStreamRequest.  # noqa: E501


        :return: The playback_policy of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: list[PlaybackPolicy]
        """
        return self._playback_policy

    @playback_policy.setter
    def playback_policy(self, playback_policy):
        """Sets the playback_policy of this CreateLiveStreamRequest.


        :param playback_policy: The playback_policy of this CreateLiveStreamRequest.  # noqa: E501
        :type playback_policy: list[PlaybackPolicy]
        """

        self._playback_policy = playback_policy

    @property
    def new_asset_settings(self):
        """Gets the new_asset_settings of this CreateLiveStreamRequest.  # noqa: E501


        :return: The new_asset_settings of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: CreateAssetRequest
        """
        return self._new_asset_settings

    @new_asset_settings.setter
    def new_asset_settings(self, new_asset_settings):
        """Sets the new_asset_settings of this CreateLiveStreamRequest.


        :param new_asset_settings: The new_asset_settings of this CreateLiveStreamRequest.  # noqa: E501
        :type new_asset_settings: CreateAssetRequest
        """

        self._new_asset_settings = new_asset_settings

    @property
    def reconnect_window(self):
        """Gets the reconnect_window of this CreateLiveStreamRequest.  # noqa: E501

        When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset. Defaults to 60 seconds on the API if not specified.  # noqa: E501

        :return: The reconnect_window of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: float
        """
        return self._reconnect_window

    @reconnect_window.setter
    def reconnect_window(self, reconnect_window):
        """Sets the reconnect_window of this CreateLiveStreamRequest.

        When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset. Defaults to 60 seconds on the API if not specified.  # noqa: E501

        :param reconnect_window: The reconnect_window of this CreateLiveStreamRequest.  # noqa: E501
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
    def passthrough(self):
        """Gets the passthrough of this CreateLiveStreamRequest.  # noqa: E501


        :return: The passthrough of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this CreateLiveStreamRequest.


        :param passthrough: The passthrough of this CreateLiveStreamRequest.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

    @property
    def audio_only(self):
        """Gets the audio_only of this CreateLiveStreamRequest.  # noqa: E501

        Force the live stream to only process the audio track when the value is set to true. Mux drops the video track if broadcasted.  # noqa: E501

        :return: The audio_only of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._audio_only

    @audio_only.setter
    def audio_only(self, audio_only):
        """Sets the audio_only of this CreateLiveStreamRequest.

        Force the live stream to only process the audio track when the value is set to true. Mux drops the video track if broadcasted.  # noqa: E501

        :param audio_only: The audio_only of this CreateLiveStreamRequest.  # noqa: E501
        :type audio_only: bool
        """

        self._audio_only = audio_only

    @property
    def reduced_latency(self):
        """Gets the reduced_latency of this CreateLiveStreamRequest.  # noqa: E501

        Latency is the time from when the streamer does something in real life to when you see it happen in the player. Set this if you want lower latency for your live stream. Note: Reconnect windows are incompatible with Reduced Latency and will always be set to zero (0) seconds. Read more here: https://mux.com/blog/reduced-latency-for-mux-live-streaming-now-available/  # noqa: E501

        :return: The reduced_latency of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reduced_latency

    @reduced_latency.setter
    def reduced_latency(self, reduced_latency):
        """Sets the reduced_latency of this CreateLiveStreamRequest.

        Latency is the time from when the streamer does something in real life to when you see it happen in the player. Set this if you want lower latency for your live stream. Note: Reconnect windows are incompatible with Reduced Latency and will always be set to zero (0) seconds. Read more here: https://mux.com/blog/reduced-latency-for-mux-live-streaming-now-available/  # noqa: E501

        :param reduced_latency: The reduced_latency of this CreateLiveStreamRequest.  # noqa: E501
        :type reduced_latency: bool
        """

        self._reduced_latency = reduced_latency

    @property
    def low_latency(self):
        """Gets the low_latency of this CreateLiveStreamRequest.  # noqa: E501

        Latency is the time from when the streamer does something in real life to when you see it happen in the player. Setting this option will enable compatibility with the LL-HLS specification for low-latency streaming. This typically has lower latency than Reduced Latency streams, and cannot be combined with Reduced Latency. Note: Reconnect windows are incompatible with Low Latency and will always be set to zero (0) seconds.  # noqa: E501

        :return: The low_latency of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._low_latency

    @low_latency.setter
    def low_latency(self, low_latency):
        """Sets the low_latency of this CreateLiveStreamRequest.

        Latency is the time from when the streamer does something in real life to when you see it happen in the player. Setting this option will enable compatibility with the LL-HLS specification for low-latency streaming. This typically has lower latency than Reduced Latency streams, and cannot be combined with Reduced Latency. Note: Reconnect windows are incompatible with Low Latency and will always be set to zero (0) seconds.  # noqa: E501

        :param low_latency: The low_latency of this CreateLiveStreamRequest.  # noqa: E501
        :type low_latency: bool
        """

        self._low_latency = low_latency

    @property
    def test(self):
        """Gets the test of this CreateLiveStreamRequest.  # noqa: E501

        Marks the live stream as a test live stream when the value is set to true. A test live stream can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test live streams created. Test live streams are watermarked with the Mux logo and limited to 5 minutes. The test live stream is disabled after the stream is active for 5 mins and the recorded asset also deleted after 24 hours.  # noqa: E501

        :return: The test of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this CreateLiveStreamRequest.

        Marks the live stream as a test live stream when the value is set to true. A test live stream can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test live streams created. Test live streams are watermarked with the Mux logo and limited to 5 minutes. The test live stream is disabled after the stream is active for 5 mins and the recorded asset also deleted after 24 hours.  # noqa: E501

        :param test: The test of this CreateLiveStreamRequest.  # noqa: E501
        :type test: bool
        """

        self._test = test

    @property
    def simulcast_targets(self):
        """Gets the simulcast_targets of this CreateLiveStreamRequest.  # noqa: E501


        :return: The simulcast_targets of this CreateLiveStreamRequest.  # noqa: E501
        :rtype: list[CreateSimulcastTargetRequest]
        """
        return self._simulcast_targets

    @simulcast_targets.setter
    def simulcast_targets(self, simulcast_targets):
        """Sets the simulcast_targets of this CreateLiveStreamRequest.


        :param simulcast_targets: The simulcast_targets of this CreateLiveStreamRequest.  # noqa: E501
        :type simulcast_targets: list[CreateSimulcastTargetRequest]
        """

        self._simulcast_targets = simulcast_targets

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
        if not isinstance(other, CreateLiveStreamRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLiveStreamRequest):
            return True

        return self.to_dict() != other.to_dict()
