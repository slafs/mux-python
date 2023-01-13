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


class Track(object):
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
        'type': 'str',
        'duration': 'float',
        'max_width': 'int',
        'max_height': 'int',
        'max_frame_rate': 'float',
        'max_channels': 'int',
        'max_channel_layout': 'str',
        'text_type': 'str',
        'text_source': 'str',
        'language_code': 'str',
        'name': 'str',
        'closed_captions': 'bool',
        'passthrough': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'duration': 'duration',
        'max_width': 'max_width',
        'max_height': 'max_height',
        'max_frame_rate': 'max_frame_rate',
        'max_channels': 'max_channels',
        'max_channel_layout': 'max_channel_layout',
        'text_type': 'text_type',
        'text_source': 'text_source',
        'language_code': 'language_code',
        'name': 'name',
        'closed_captions': 'closed_captions',
        'passthrough': 'passthrough',
        'status': 'status'
    }

    def __init__(self, id=None, type=None, duration=None, max_width=None, max_height=None, max_frame_rate=None, max_channels=None, max_channel_layout=None, text_type=None, text_source=None, language_code=None, name=None, closed_captions=None, passthrough=None, status=None, local_vars_configuration=None):  # noqa: E501
        """Track - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._duration = None
        self._max_width = None
        self._max_height = None
        self._max_frame_rate = None
        self._max_channels = None
        self._max_channel_layout = None
        self._text_type = None
        self._text_source = None
        self._language_code = None
        self._name = None
        self._closed_captions = None
        self._passthrough = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if duration is not None:
            self.duration = duration
        if max_width is not None:
            self.max_width = max_width
        if max_height is not None:
            self.max_height = max_height
        if max_frame_rate is not None:
            self.max_frame_rate = max_frame_rate
        if max_channels is not None:
            self.max_channels = max_channels
        if max_channel_layout is not None:
            self.max_channel_layout = max_channel_layout
        if text_type is not None:
            self.text_type = text_type
        if text_source is not None:
            self.text_source = text_source
        if language_code is not None:
            self.language_code = language_code
        if name is not None:
            self.name = name
        if closed_captions is not None:
            self.closed_captions = closed_captions
        if passthrough is not None:
            self.passthrough = passthrough
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this Track.  # noqa: E501

        Unique identifier for the Track  # noqa: E501

        :return: The id of this Track.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Track.

        Unique identifier for the Track  # noqa: E501

        :param id: The id of this Track.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Track.  # noqa: E501

        The type of track  # noqa: E501

        :return: The type of this Track.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Track.

        The type of track  # noqa: E501

        :param type: The type of this Track.  # noqa: E501
        :type type: str
        """
        allowed_values = ["video", "audio", "text"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def duration(self):
        """Gets the duration of this Track.  # noqa: E501

        The duration in seconds of the track media. This parameter is not set for `text` type tracks. This field is optional and may not be set. The top level `duration` field of an asset will always be set.  # noqa: E501

        :return: The duration of this Track.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Track.

        The duration in seconds of the track media. This parameter is not set for `text` type tracks. This field is optional and may not be set. The top level `duration` field of an asset will always be set.  # noqa: E501

        :param duration: The duration of this Track.  # noqa: E501
        :type duration: float
        """

        self._duration = duration

    @property
    def max_width(self):
        """Gets the max_width of this Track.  # noqa: E501

        The maximum width in pixels available for the track. Only set for the `video` type track.  # noqa: E501

        :return: The max_width of this Track.  # noqa: E501
        :rtype: int
        """
        return self._max_width

    @max_width.setter
    def max_width(self, max_width):
        """Sets the max_width of this Track.

        The maximum width in pixels available for the track. Only set for the `video` type track.  # noqa: E501

        :param max_width: The max_width of this Track.  # noqa: E501
        :type max_width: int
        """

        self._max_width = max_width

    @property
    def max_height(self):
        """Gets the max_height of this Track.  # noqa: E501

        The maximum height in pixels available for the track. Only set for the `video` type track.  # noqa: E501

        :return: The max_height of this Track.  # noqa: E501
        :rtype: int
        """
        return self._max_height

    @max_height.setter
    def max_height(self, max_height):
        """Sets the max_height of this Track.

        The maximum height in pixels available for the track. Only set for the `video` type track.  # noqa: E501

        :param max_height: The max_height of this Track.  # noqa: E501
        :type max_height: int
        """

        self._max_height = max_height

    @property
    def max_frame_rate(self):
        """Gets the max_frame_rate of this Track.  # noqa: E501

        The maximum frame rate available for the track. Only set for the `video` type track. This field may return `-1` if the frame rate of the input cannot be reliably determined.  # noqa: E501

        :return: The max_frame_rate of this Track.  # noqa: E501
        :rtype: float
        """
        return self._max_frame_rate

    @max_frame_rate.setter
    def max_frame_rate(self, max_frame_rate):
        """Sets the max_frame_rate of this Track.

        The maximum frame rate available for the track. Only set for the `video` type track. This field may return `-1` if the frame rate of the input cannot be reliably determined.  # noqa: E501

        :param max_frame_rate: The max_frame_rate of this Track.  # noqa: E501
        :type max_frame_rate: float
        """

        self._max_frame_rate = max_frame_rate

    @property
    def max_channels(self):
        """Gets the max_channels of this Track.  # noqa: E501

        The maximum number of audio channels the track supports. Only set for the `audio` type track.  # noqa: E501

        :return: The max_channels of this Track.  # noqa: E501
        :rtype: int
        """
        return self._max_channels

    @max_channels.setter
    def max_channels(self, max_channels):
        """Sets the max_channels of this Track.

        The maximum number of audio channels the track supports. Only set for the `audio` type track.  # noqa: E501

        :param max_channels: The max_channels of this Track.  # noqa: E501
        :type max_channels: int
        """

        self._max_channels = max_channels

    @property
    def max_channel_layout(self):
        """Gets the max_channel_layout of this Track.  # noqa: E501

        Only set for the `audio` type track.  # noqa: E501

        :return: The max_channel_layout of this Track.  # noqa: E501
        :rtype: str
        """
        return self._max_channel_layout

    @max_channel_layout.setter
    def max_channel_layout(self, max_channel_layout):
        """Sets the max_channel_layout of this Track.

        Only set for the `audio` type track.  # noqa: E501

        :param max_channel_layout: The max_channel_layout of this Track.  # noqa: E501
        :type max_channel_layout: str
        """

        self._max_channel_layout = max_channel_layout

    @property
    def text_type(self):
        """Gets the text_type of this Track.  # noqa: E501

        This parameter is only set for `text` type tracks.  # noqa: E501

        :return: The text_type of this Track.  # noqa: E501
        :rtype: str
        """
        return self._text_type

    @text_type.setter
    def text_type(self, text_type):
        """Sets the text_type of this Track.

        This parameter is only set for `text` type tracks.  # noqa: E501

        :param text_type: The text_type of this Track.  # noqa: E501
        :type text_type: str
        """
        allowed_values = ["subtitles"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and text_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `text_type` ({0}), must be one of {1}"  # noqa: E501
                .format(text_type, allowed_values)
            )

        self._text_type = text_type

    @property
    def text_source(self):
        """Gets the text_source of this Track.  # noqa: E501

        The source of the text contained in a Track of type `text`. Valid `text_source` values are listed below. * `uploaded`: Tracks uploaded to Mux as caption or subtitle files using the Create Asset Track API. * `embedded`: Tracks extracted from an embedded stream of CEA-608 closed captions. * `generated_live`: Tracks generated by automatic speech recognition on a live stream configured with `generated_subtitles`. If an Asset has both `generated_live` and `generated_live_final` tracks that are `ready`, then only the `generated_live_final` track will be included during playback. * `generated_live_final`: Tracks generated by automatic speech recognition on a live stream using `generated_subtitles`. The accuracy, timing, and formatting of these subtitles is improved compared to the corresponding `generated_live` tracks. However, `generated_live_final` tracks will not be available in `ready` status until the live stream ends. If an Asset has both `generated_live` and `generated_live_final` tracks that are `ready`, then only the `generated_live_final` track will be included during playback.   # noqa: E501

        :return: The text_source of this Track.  # noqa: E501
        :rtype: str
        """
        return self._text_source

    @text_source.setter
    def text_source(self, text_source):
        """Sets the text_source of this Track.

        The source of the text contained in a Track of type `text`. Valid `text_source` values are listed below. * `uploaded`: Tracks uploaded to Mux as caption or subtitle files using the Create Asset Track API. * `embedded`: Tracks extracted from an embedded stream of CEA-608 closed captions. * `generated_live`: Tracks generated by automatic speech recognition on a live stream configured with `generated_subtitles`. If an Asset has both `generated_live` and `generated_live_final` tracks that are `ready`, then only the `generated_live_final` track will be included during playback. * `generated_live_final`: Tracks generated by automatic speech recognition on a live stream using `generated_subtitles`. The accuracy, timing, and formatting of these subtitles is improved compared to the corresponding `generated_live` tracks. However, `generated_live_final` tracks will not be available in `ready` status until the live stream ends. If an Asset has both `generated_live` and `generated_live_final` tracks that are `ready`, then only the `generated_live_final` track will be included during playback.   # noqa: E501

        :param text_source: The text_source of this Track.  # noqa: E501
        :type text_source: str
        """
        allowed_values = ["uploaded", "embedded", "generated_live", "generated_live_final"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and text_source not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `text_source` ({0}), must be one of {1}"  # noqa: E501
                .format(text_source, allowed_values)
            )

        self._text_source = text_source

    @property
    def language_code(self):
        """Gets the language_code of this Track.  # noqa: E501

        The language code value represents [BCP 47](https://tools.ietf.org/html/bcp47) specification compliant value. For example, `en` for English or `en-US` for the US version of English. This parameter is only set for `text` type and `subtitles` text type tracks.  # noqa: E501

        :return: The language_code of this Track.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this Track.

        The language code value represents [BCP 47](https://tools.ietf.org/html/bcp47) specification compliant value. For example, `en` for English or `en-US` for the US version of English. This parameter is only set for `text` type and `subtitles` text type tracks.  # noqa: E501

        :param language_code: The language_code of this Track.  # noqa: E501
        :type language_code: str
        """

        self._language_code = language_code

    @property
    def name(self):
        """Gets the name of this Track.  # noqa: E501

        The name of the track containing a human-readable description. The hls manifest will associate a subtitle text track with this value. For example, the value is \"English\" for subtitles text track for the `language_code` value of `en-US`. This parameter is only set for `text` type and `subtitles` text type tracks.  # noqa: E501

        :return: The name of this Track.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Track.

        The name of the track containing a human-readable description. The hls manifest will associate a subtitle text track with this value. For example, the value is \"English\" for subtitles text track for the `language_code` value of `en-US`. This parameter is only set for `text` type and `subtitles` text type tracks.  # noqa: E501

        :param name: The name of this Track.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def closed_captions(self):
        """Gets the closed_captions of this Track.  # noqa: E501

        Indicates the track provides Subtitles for the Deaf or Hard-of-hearing (SDH). This parameter is only set for `text` type and `subtitles` text type tracks.  # noqa: E501

        :return: The closed_captions of this Track.  # noqa: E501
        :rtype: bool
        """
        return self._closed_captions

    @closed_captions.setter
    def closed_captions(self, closed_captions):
        """Sets the closed_captions of this Track.

        Indicates the track provides Subtitles for the Deaf or Hard-of-hearing (SDH). This parameter is only set for `text` type and `subtitles` text type tracks.  # noqa: E501

        :param closed_captions: The closed_captions of this Track.  # noqa: E501
        :type closed_captions: bool
        """

        self._closed_captions = closed_captions

    @property
    def passthrough(self):
        """Gets the passthrough of this Track.  # noqa: E501

        Arbitrary user-supplied metadata set for the track either when creating the asset or track. This parameter is only set for `text` type tracks. Max 255 characters.  # noqa: E501

        :return: The passthrough of this Track.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this Track.

        Arbitrary user-supplied metadata set for the track either when creating the asset or track. This parameter is only set for `text` type tracks. Max 255 characters.  # noqa: E501

        :param passthrough: The passthrough of this Track.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

    @property
    def status(self):
        """Gets the status of this Track.  # noqa: E501

        The status of the track. This parameter is only set for `text` type tracks.  # noqa: E501

        :return: The status of this Track.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Track.

        The status of the track. This parameter is only set for `text` type tracks.  # noqa: E501

        :param status: The status of this Track.  # noqa: E501
        :type status: str
        """
        allowed_values = ["preparing", "ready", "errored"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, Track):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Track):
            return True

        return self.to_dict() != other.to_dict()
