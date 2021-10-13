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


class AssetNonStandardInputReasons(object):
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
        'video_codec': 'str',
        'audio_codec': 'str',
        'video_gop_size': 'str',
        'video_frame_rate': 'str',
        'video_resolution': 'str',
        'video_bitrate': 'str',
        'pixel_aspect_ratio': 'str',
        'video_edit_list': 'str',
        'audio_edit_list': 'str',
        'unexpected_media_file_parameters': 'str'
    }

    attribute_map = {
        'video_codec': 'video_codec',
        'audio_codec': 'audio_codec',
        'video_gop_size': 'video_gop_size',
        'video_frame_rate': 'video_frame_rate',
        'video_resolution': 'video_resolution',
        'video_bitrate': 'video_bitrate',
        'pixel_aspect_ratio': 'pixel_aspect_ratio',
        'video_edit_list': 'video_edit_list',
        'audio_edit_list': 'audio_edit_list',
        'unexpected_media_file_parameters': 'unexpected_media_file_parameters'
    }

    def __init__(self, video_codec=None, audio_codec=None, video_gop_size=None, video_frame_rate=None, video_resolution=None, video_bitrate=None, pixel_aspect_ratio=None, video_edit_list=None, audio_edit_list=None, unexpected_media_file_parameters=None, local_vars_configuration=None):  # noqa: E501
        """AssetNonStandardInputReasons - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._video_codec = None
        self._audio_codec = None
        self._video_gop_size = None
        self._video_frame_rate = None
        self._video_resolution = None
        self._video_bitrate = None
        self._pixel_aspect_ratio = None
        self._video_edit_list = None
        self._audio_edit_list = None
        self._unexpected_media_file_parameters = None
        self.discriminator = None

        if video_codec is not None:
            self.video_codec = video_codec
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if video_gop_size is not None:
            self.video_gop_size = video_gop_size
        if video_frame_rate is not None:
            self.video_frame_rate = video_frame_rate
        if video_resolution is not None:
            self.video_resolution = video_resolution
        if video_bitrate is not None:
            self.video_bitrate = video_bitrate
        if pixel_aspect_ratio is not None:
            self.pixel_aspect_ratio = pixel_aspect_ratio
        if video_edit_list is not None:
            self.video_edit_list = video_edit_list
        if audio_edit_list is not None:
            self.audio_edit_list = audio_edit_list
        if unexpected_media_file_parameters is not None:
            self.unexpected_media_file_parameters = unexpected_media_file_parameters

    @property
    def video_codec(self):
        """Gets the video_codec of this AssetNonStandardInputReasons.  # noqa: E501

        The video codec used on the input file. For example, the input file encoded with `hevc` video codec is non-standard and the value of this parameter is `hevc`.  # noqa: E501

        :return: The video_codec of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this AssetNonStandardInputReasons.

        The video codec used on the input file. For example, the input file encoded with `hevc` video codec is non-standard and the value of this parameter is `hevc`.  # noqa: E501

        :param video_codec: The video_codec of this AssetNonStandardInputReasons.  # noqa: E501
        :type video_codec: str
        """

        self._video_codec = video_codec

    @property
    def audio_codec(self):
        """Gets the audio_codec of this AssetNonStandardInputReasons.  # noqa: E501

        The audio codec used on the input file. Non-AAC audio codecs are non-standard.  # noqa: E501

        :return: The audio_codec of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this AssetNonStandardInputReasons.

        The audio codec used on the input file. Non-AAC audio codecs are non-standard.  # noqa: E501

        :param audio_codec: The audio_codec of this AssetNonStandardInputReasons.  # noqa: E501
        :type audio_codec: str
        """

        self._audio_codec = audio_codec

    @property
    def video_gop_size(self):
        """Gets the video_gop_size of this AssetNonStandardInputReasons.  # noqa: E501

        The video key frame Interval (also called as Group of Picture or GOP) of the input file is `high`. This parameter is present when the gop is greater than 10 seconds.  # noqa: E501

        :return: The video_gop_size of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._video_gop_size

    @video_gop_size.setter
    def video_gop_size(self, video_gop_size):
        """Sets the video_gop_size of this AssetNonStandardInputReasons.

        The video key frame Interval (also called as Group of Picture or GOP) of the input file is `high`. This parameter is present when the gop is greater than 10 seconds.  # noqa: E501

        :param video_gop_size: The video_gop_size of this AssetNonStandardInputReasons.  # noqa: E501
        :type video_gop_size: str
        """
        allowed_values = ["high"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and video_gop_size not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `video_gop_size` ({0}), must be one of {1}"  # noqa: E501
                .format(video_gop_size, allowed_values)
            )

        self._video_gop_size = video_gop_size

    @property
    def video_frame_rate(self):
        """Gets the video_frame_rate of this AssetNonStandardInputReasons.  # noqa: E501

        The video frame rate of the input file. Video with average frames per second (fps) less than 10 or greater than 120 is non-standard. A `-1` frame rate value indicates Mux could not determine the frame rate of the video track.  # noqa: E501

        :return: The video_frame_rate of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._video_frame_rate

    @video_frame_rate.setter
    def video_frame_rate(self, video_frame_rate):
        """Sets the video_frame_rate of this AssetNonStandardInputReasons.

        The video frame rate of the input file. Video with average frames per second (fps) less than 10 or greater than 120 is non-standard. A `-1` frame rate value indicates Mux could not determine the frame rate of the video track.  # noqa: E501

        :param video_frame_rate: The video_frame_rate of this AssetNonStandardInputReasons.  # noqa: E501
        :type video_frame_rate: str
        """

        self._video_frame_rate = video_frame_rate

    @property
    def video_resolution(self):
        """Gets the video_resolution of this AssetNonStandardInputReasons.  # noqa: E501

        The video resolution of the input file. Video resolution higher than 2048 pixels on any one dimension (height or width) is considered non-standard, The resolution value is presented as `width` x `height` in pixels.  # noqa: E501

        :return: The video_resolution of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._video_resolution

    @video_resolution.setter
    def video_resolution(self, video_resolution):
        """Sets the video_resolution of this AssetNonStandardInputReasons.

        The video resolution of the input file. Video resolution higher than 2048 pixels on any one dimension (height or width) is considered non-standard, The resolution value is presented as `width` x `height` in pixels.  # noqa: E501

        :param video_resolution: The video_resolution of this AssetNonStandardInputReasons.  # noqa: E501
        :type video_resolution: str
        """

        self._video_resolution = video_resolution

    @property
    def video_bitrate(self):
        """Gets the video_bitrate of this AssetNonStandardInputReasons.  # noqa: E501

        The video bitrate of the input file is `high`. This parameter is present when the average bitrate of any key frame interval (also known as Group of Pictures or GOP) is higher than what's considered standard which typically is 16 Mbps.  # noqa: E501

        :return: The video_bitrate of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._video_bitrate

    @video_bitrate.setter
    def video_bitrate(self, video_bitrate):
        """Sets the video_bitrate of this AssetNonStandardInputReasons.

        The video bitrate of the input file is `high`. This parameter is present when the average bitrate of any key frame interval (also known as Group of Pictures or GOP) is higher than what's considered standard which typically is 16 Mbps.  # noqa: E501

        :param video_bitrate: The video_bitrate of this AssetNonStandardInputReasons.  # noqa: E501
        :type video_bitrate: str
        """
        allowed_values = ["high"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and video_bitrate not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `video_bitrate` ({0}), must be one of {1}"  # noqa: E501
                .format(video_bitrate, allowed_values)
            )

        self._video_bitrate = video_bitrate

    @property
    def pixel_aspect_ratio(self):
        """Gets the pixel_aspect_ratio of this AssetNonStandardInputReasons.  # noqa: E501

        The video pixel aspect ratio of the input file.  # noqa: E501

        :return: The pixel_aspect_ratio of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._pixel_aspect_ratio

    @pixel_aspect_ratio.setter
    def pixel_aspect_ratio(self, pixel_aspect_ratio):
        """Sets the pixel_aspect_ratio of this AssetNonStandardInputReasons.

        The video pixel aspect ratio of the input file.  # noqa: E501

        :param pixel_aspect_ratio: The pixel_aspect_ratio of this AssetNonStandardInputReasons.  # noqa: E501
        :type pixel_aspect_ratio: str
        """

        self._pixel_aspect_ratio = pixel_aspect_ratio

    @property
    def video_edit_list(self):
        """Gets the video_edit_list of this AssetNonStandardInputReasons.  # noqa: E501

        Video Edit List reason indicates that the input file's video track contains a complex Edit Decision List.  # noqa: E501

        :return: The video_edit_list of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._video_edit_list

    @video_edit_list.setter
    def video_edit_list(self, video_edit_list):
        """Sets the video_edit_list of this AssetNonStandardInputReasons.

        Video Edit List reason indicates that the input file's video track contains a complex Edit Decision List.  # noqa: E501

        :param video_edit_list: The video_edit_list of this AssetNonStandardInputReasons.  # noqa: E501
        :type video_edit_list: str
        """
        allowed_values = ["non-standard"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and video_edit_list not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `video_edit_list` ({0}), must be one of {1}"  # noqa: E501
                .format(video_edit_list, allowed_values)
            )

        self._video_edit_list = video_edit_list

    @property
    def audio_edit_list(self):
        """Gets the audio_edit_list of this AssetNonStandardInputReasons.  # noqa: E501

        Audio Edit List reason indicates that the input file's audio track contains a complex Edit Decision List.  # noqa: E501

        :return: The audio_edit_list of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._audio_edit_list

    @audio_edit_list.setter
    def audio_edit_list(self, audio_edit_list):
        """Sets the audio_edit_list of this AssetNonStandardInputReasons.

        Audio Edit List reason indicates that the input file's audio track contains a complex Edit Decision List.  # noqa: E501

        :param audio_edit_list: The audio_edit_list of this AssetNonStandardInputReasons.  # noqa: E501
        :type audio_edit_list: str
        """
        allowed_values = ["non-standard"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and audio_edit_list not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `audio_edit_list` ({0}), must be one of {1}"  # noqa: E501
                .format(audio_edit_list, allowed_values)
            )

        self._audio_edit_list = audio_edit_list

    @property
    def unexpected_media_file_parameters(self):
        """Gets the unexpected_media_file_parameters of this AssetNonStandardInputReasons.  # noqa: E501

        A catch-all reason when the input file in created with non-standard encoding parameters.  # noqa: E501

        :return: The unexpected_media_file_parameters of this AssetNonStandardInputReasons.  # noqa: E501
        :rtype: str
        """
        return self._unexpected_media_file_parameters

    @unexpected_media_file_parameters.setter
    def unexpected_media_file_parameters(self, unexpected_media_file_parameters):
        """Sets the unexpected_media_file_parameters of this AssetNonStandardInputReasons.

        A catch-all reason when the input file in created with non-standard encoding parameters.  # noqa: E501

        :param unexpected_media_file_parameters: The unexpected_media_file_parameters of this AssetNonStandardInputReasons.  # noqa: E501
        :type unexpected_media_file_parameters: str
        """
        allowed_values = ["non-standard"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unexpected_media_file_parameters not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unexpected_media_file_parameters` ({0}), must be one of {1}"  # noqa: E501
                .format(unexpected_media_file_parameters, allowed_values)
            )

        self._unexpected_media_file_parameters = unexpected_media_file_parameters

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
        if not isinstance(other, AssetNonStandardInputReasons):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetNonStandardInputReasons):
            return True

        return self.to_dict() != other.to_dict()
