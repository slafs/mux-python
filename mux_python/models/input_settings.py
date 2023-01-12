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


class InputSettings(object):
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
        'url': 'str',
        'overlay_settings': 'InputSettingsOverlaySettings',
        'start_time': 'float',
        'end_time': 'float',
        'type': 'str',
        'text_type': 'str',
        'language_code': 'str',
        'name': 'str',
        'closed_captions': 'bool',
        'passthrough': 'str'
    }

    attribute_map = {
        'url': 'url',
        'overlay_settings': 'overlay_settings',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'type': 'type',
        'text_type': 'text_type',
        'language_code': 'language_code',
        'name': 'name',
        'closed_captions': 'closed_captions',
        'passthrough': 'passthrough'
    }

    def __init__(self, url=None, overlay_settings=None, start_time=None, end_time=None, type=None, text_type=None, language_code=None, name=None, closed_captions=None, passthrough=None, local_vars_configuration=None):  # noqa: E501
        """InputSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._overlay_settings = None
        self._start_time = None
        self._end_time = None
        self._type = None
        self._text_type = None
        self._language_code = None
        self._name = None
        self._closed_captions = None
        self._passthrough = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if overlay_settings is not None:
            self.overlay_settings = overlay_settings
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if type is not None:
            self.type = type
        if text_type is not None:
            self.text_type = text_type
        if language_code is not None:
            self.language_code = language_code
        if name is not None:
            self.name = name
        if closed_captions is not None:
            self.closed_captions = closed_captions
        if passthrough is not None:
            self.passthrough = passthrough

    @property
    def url(self):
        """Gets the url of this InputSettings.  # noqa: E501

        The URL of the file that Mux should download and use. * For subtitles text tracks, the URL is the location of subtitle/captions file. Mux supports [SubRip Text (SRT)](https://en.wikipedia.org/wiki/SubRip) and [Web Video Text Tracks](https://www.w3.org/TR/webvtt1/) format for ingesting Subtitles and Closed Captions. * For Watermarking or Overlay, the URL is the location of the watermark image. * When creating clips from existing Mux assets, the URL is defined with `mux://assets/{asset_id}` template where `asset_id` is the Asset Identifier for creating the clip from.   # noqa: E501

        :return: The url of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InputSettings.

        The URL of the file that Mux should download and use. * For subtitles text tracks, the URL is the location of subtitle/captions file. Mux supports [SubRip Text (SRT)](https://en.wikipedia.org/wiki/SubRip) and [Web Video Text Tracks](https://www.w3.org/TR/webvtt1/) format for ingesting Subtitles and Closed Captions. * For Watermarking or Overlay, the URL is the location of the watermark image. * When creating clips from existing Mux assets, the URL is defined with `mux://assets/{asset_id}` template where `asset_id` is the Asset Identifier for creating the clip from.   # noqa: E501

        :param url: The url of this InputSettings.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def overlay_settings(self):
        """Gets the overlay_settings of this InputSettings.  # noqa: E501


        :return: The overlay_settings of this InputSettings.  # noqa: E501
        :rtype: InputSettingsOverlaySettings
        """
        return self._overlay_settings

    @overlay_settings.setter
    def overlay_settings(self, overlay_settings):
        """Sets the overlay_settings of this InputSettings.


        :param overlay_settings: The overlay_settings of this InputSettings.  # noqa: E501
        :type overlay_settings: InputSettingsOverlaySettings
        """

        self._overlay_settings = overlay_settings

    @property
    def start_time(self):
        """Gets the start_time of this InputSettings.  # noqa: E501

        The time offset in seconds from the beginning of the video indicating the clip's starting marker. The default value is 0 when not included. This parameter is only applicable for creating clips when `input.url` has `mux://assets/{asset_id}` format.  # noqa: E501

        :return: The start_time of this InputSettings.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InputSettings.

        The time offset in seconds from the beginning of the video indicating the clip's starting marker. The default value is 0 when not included. This parameter is only applicable for creating clips when `input.url` has `mux://assets/{asset_id}` format.  # noqa: E501

        :param start_time: The start_time of this InputSettings.  # noqa: E501
        :type start_time: float
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InputSettings.  # noqa: E501

        The time offset in seconds from the beginning of the video, indicating the clip's ending marker. The default value is the duration of the video when not included. This parameter is only applicable for creating clips when `input.url` has `mux://assets/{asset_id}` format.  # noqa: E501

        :return: The end_time of this InputSettings.  # noqa: E501
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InputSettings.

        The time offset in seconds from the beginning of the video, indicating the clip's ending marker. The default value is the duration of the video when not included. This parameter is only applicable for creating clips when `input.url` has `mux://assets/{asset_id}` format.  # noqa: E501

        :param end_time: The end_time of this InputSettings.  # noqa: E501
        :type end_time: float
        """

        self._end_time = end_time

    @property
    def type(self):
        """Gets the type of this InputSettings.  # noqa: E501

        This parameter is required for `text` type tracks.  # noqa: E501

        :return: The type of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InputSettings.

        This parameter is required for `text` type tracks.  # noqa: E501

        :param type: The type of this InputSettings.  # noqa: E501
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
    def text_type(self):
        """Gets the text_type of this InputSettings.  # noqa: E501

        Type of text track. This parameter only supports subtitles value. For more information on Subtitles / Closed Captions, [see this blog post](https://mux.com/blog/subtitles-captions-webvtt-hls-and-those-magic-flags/). This parameter is required for `text` type tracks.  # noqa: E501

        :return: The text_type of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._text_type

    @text_type.setter
    def text_type(self, text_type):
        """Sets the text_type of this InputSettings.

        Type of text track. This parameter only supports subtitles value. For more information on Subtitles / Closed Captions, [see this blog post](https://mux.com/blog/subtitles-captions-webvtt-hls-and-those-magic-flags/). This parameter is required for `text` type tracks.  # noqa: E501

        :param text_type: The text_type of this InputSettings.  # noqa: E501
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
    def language_code(self):
        """Gets the language_code of this InputSettings.  # noqa: E501

        The language code value must be a valid [BCP 47](https://tools.ietf.org/html/bcp47) specification compliant value. For example, en for English or en-US for the US version of English. This parameter is required for text type and subtitles text type track.  # noqa: E501

        :return: The language_code of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this InputSettings.

        The language code value must be a valid [BCP 47](https://tools.ietf.org/html/bcp47) specification compliant value. For example, en for English or en-US for the US version of English. This parameter is required for text type and subtitles text type track.  # noqa: E501

        :param language_code: The language_code of this InputSettings.  # noqa: E501
        :type language_code: str
        """

        self._language_code = language_code

    @property
    def name(self):
        """Gets the name of this InputSettings.  # noqa: E501

        The name of the track containing a human-readable description. This value must be unique across all text type and subtitles `text` type tracks. The hls manifest will associate a subtitle text track with this value. For example, the value should be \"English\" for subtitles text track with language_code as en. This optional parameter should be used only for `text` type and subtitles `text` type tracks. If this parameter is not included, Mux will auto-populate based on the `input[].language_code` value.  # noqa: E501

        :return: The name of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputSettings.

        The name of the track containing a human-readable description. This value must be unique across all text type and subtitles `text` type tracks. The hls manifest will associate a subtitle text track with this value. For example, the value should be \"English\" for subtitles text track with language_code as en. This optional parameter should be used only for `text` type and subtitles `text` type tracks. If this parameter is not included, Mux will auto-populate based on the `input[].language_code` value.  # noqa: E501

        :param name: The name of this InputSettings.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def closed_captions(self):
        """Gets the closed_captions of this InputSettings.  # noqa: E501

        Indicates the track provides Subtitles for the Deaf or Hard-of-hearing (SDH). This optional parameter should be used for `text` type and subtitles `text` type tracks.  # noqa: E501

        :return: The closed_captions of this InputSettings.  # noqa: E501
        :rtype: bool
        """
        return self._closed_captions

    @closed_captions.setter
    def closed_captions(self, closed_captions):
        """Sets the closed_captions of this InputSettings.

        Indicates the track provides Subtitles for the Deaf or Hard-of-hearing (SDH). This optional parameter should be used for `text` type and subtitles `text` type tracks.  # noqa: E501

        :param closed_captions: The closed_captions of this InputSettings.  # noqa: E501
        :type closed_captions: bool
        """

        self._closed_captions = closed_captions

    @property
    def passthrough(self):
        """Gets the passthrough of this InputSettings.  # noqa: E501

        This optional parameter should be used for `text` type and subtitles `text` type tracks.  # noqa: E501

        :return: The passthrough of this InputSettings.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this InputSettings.

        This optional parameter should be used for `text` type and subtitles `text` type tracks.  # noqa: E501

        :param passthrough: The passthrough of this InputSettings.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

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
        if not isinstance(other, InputSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputSettings):
            return True

        return self.to_dict() != other.to_dict()
