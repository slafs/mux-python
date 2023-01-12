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


class CreateAssetRequest(object):
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
        'input': 'list[InputSettings]',
        'playback_policy': 'list[PlaybackPolicy]',
        'per_title_encode': 'bool',
        'passthrough': 'str',
        'mp4_support': 'str',
        'normalize_audio': 'bool',
        'master_access': 'str',
        'test': 'bool'
    }

    attribute_map = {
        'input': 'input',
        'playback_policy': 'playback_policy',
        'per_title_encode': 'per_title_encode',
        'passthrough': 'passthrough',
        'mp4_support': 'mp4_support',
        'normalize_audio': 'normalize_audio',
        'master_access': 'master_access',
        'test': 'test'
    }

    def __init__(self, input=None, playback_policy=None, per_title_encode=None, passthrough=None, mp4_support=None, normalize_audio=False, master_access=None, test=None, local_vars_configuration=None):  # noqa: E501
        """CreateAssetRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._input = None
        self._playback_policy = None
        self._per_title_encode = None
        self._passthrough = None
        self._mp4_support = None
        self._normalize_audio = None
        self._master_access = None
        self._test = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if playback_policy is not None:
            self.playback_policy = playback_policy
        if per_title_encode is not None:
            self.per_title_encode = per_title_encode
        if passthrough is not None:
            self.passthrough = passthrough
        if mp4_support is not None:
            self.mp4_support = mp4_support
        if normalize_audio is not None:
            self.normalize_audio = normalize_audio
        if master_access is not None:
            self.master_access = master_access
        if test is not None:
            self.test = test

    @property
    def input(self):
        """Gets the input of this CreateAssetRequest.  # noqa: E501

        An array of objects that each describe an input file to be used to create the asset. As a shortcut, input can also be a string URL for a file when only one input file is used. See `input[].url` for requirements.  # noqa: E501

        :return: The input of this CreateAssetRequest.  # noqa: E501
        :rtype: list[InputSettings]
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateAssetRequest.

        An array of objects that each describe an input file to be used to create the asset. As a shortcut, input can also be a string URL for a file when only one input file is used. See `input[].url` for requirements.  # noqa: E501

        :param input: The input of this CreateAssetRequest.  # noqa: E501
        :type input: list[InputSettings]
        """

        self._input = input

    @property
    def playback_policy(self):
        """Gets the playback_policy of this CreateAssetRequest.  # noqa: E501

        An array of playback policy names that you want applied to this asset and available through `playback_ids`. Options include: `\"public\"` (anyone with the playback URL can stream the asset). And `\"signed\"` (an additional access token is required to play the asset). If no playback_policy is set, the asset will have no playback IDs and will therefore not be playable. For simplicity, a single string name can be used in place of the array in the case of only one playback policy.  # noqa: E501

        :return: The playback_policy of this CreateAssetRequest.  # noqa: E501
        :rtype: list[PlaybackPolicy]
        """
        return self._playback_policy

    @playback_policy.setter
    def playback_policy(self, playback_policy):
        """Sets the playback_policy of this CreateAssetRequest.

        An array of playback policy names that you want applied to this asset and available through `playback_ids`. Options include: `\"public\"` (anyone with the playback URL can stream the asset). And `\"signed\"` (an additional access token is required to play the asset). If no playback_policy is set, the asset will have no playback IDs and will therefore not be playable. For simplicity, a single string name can be used in place of the array in the case of only one playback policy.  # noqa: E501

        :param playback_policy: The playback_policy of this CreateAssetRequest.  # noqa: E501
        :type playback_policy: list[PlaybackPolicy]
        """

        self._playback_policy = playback_policy

    @property
    def per_title_encode(self):
        """Gets the per_title_encode of this CreateAssetRequest.  # noqa: E501


        :return: The per_title_encode of this CreateAssetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._per_title_encode

    @per_title_encode.setter
    def per_title_encode(self, per_title_encode):
        """Sets the per_title_encode of this CreateAssetRequest.


        :param per_title_encode: The per_title_encode of this CreateAssetRequest.  # noqa: E501
        :type per_title_encode: bool
        """

        self._per_title_encode = per_title_encode

    @property
    def passthrough(self):
        """Gets the passthrough of this CreateAssetRequest.  # noqa: E501

        Arbitrary user-supplied metadata that will be included in the asset details and related webhooks. Can be used to store your own ID for a video along with the asset. **Max: 255 characters**.  # noqa: E501

        :return: The passthrough of this CreateAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this CreateAssetRequest.

        Arbitrary user-supplied metadata that will be included in the asset details and related webhooks. Can be used to store your own ID for a video along with the asset. **Max: 255 characters**.  # noqa: E501

        :param passthrough: The passthrough of this CreateAssetRequest.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

    @property
    def mp4_support(self):
        """Gets the mp4_support of this CreateAssetRequest.  # noqa: E501

        Specify what level (if any) of support for mp4 playback. In most cases you should use our default HLS-based streaming playback ({playback_id}.m3u8) which can automatically adjust to viewers' connection speeds, but an mp4 can be useful for some legacy devices or downloading for offline playback. See the [Download your videos guide](/guides/video/download-your-videos) for more information.  # noqa: E501

        :return: The mp4_support of this CreateAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._mp4_support

    @mp4_support.setter
    def mp4_support(self, mp4_support):
        """Sets the mp4_support of this CreateAssetRequest.

        Specify what level (if any) of support for mp4 playback. In most cases you should use our default HLS-based streaming playback ({playback_id}.m3u8) which can automatically adjust to viewers' connection speeds, but an mp4 can be useful for some legacy devices or downloading for offline playback. See the [Download your videos guide](/guides/video/download-your-videos) for more information.  # noqa: E501

        :param mp4_support: The mp4_support of this CreateAssetRequest.  # noqa: E501
        :type mp4_support: str
        """
        allowed_values = ["none", "standard"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mp4_support not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mp4_support` ({0}), must be one of {1}"  # noqa: E501
                .format(mp4_support, allowed_values)
            )

        self._mp4_support = mp4_support

    @property
    def normalize_audio(self):
        """Gets the normalize_audio of this CreateAssetRequest.  # noqa: E501

        Normalize the audio track loudness level. This parameter is only applicable to on-demand (not live) assets.  # noqa: E501

        :return: The normalize_audio of this CreateAssetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._normalize_audio

    @normalize_audio.setter
    def normalize_audio(self, normalize_audio):
        """Sets the normalize_audio of this CreateAssetRequest.

        Normalize the audio track loudness level. This parameter is only applicable to on-demand (not live) assets.  # noqa: E501

        :param normalize_audio: The normalize_audio of this CreateAssetRequest.  # noqa: E501
        :type normalize_audio: bool
        """

        self._normalize_audio = normalize_audio

    @property
    def master_access(self):
        """Gets the master_access of this CreateAssetRequest.  # noqa: E501

        Specify what level (if any) of support for master access. Master access can be enabled temporarily for your asset to be downloaded. See the [Download your videos guide](/guides/video/download-your-videos) for more information.  # noqa: E501

        :return: The master_access of this CreateAssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._master_access

    @master_access.setter
    def master_access(self, master_access):
        """Sets the master_access of this CreateAssetRequest.

        Specify what level (if any) of support for master access. Master access can be enabled temporarily for your asset to be downloaded. See the [Download your videos guide](/guides/video/download-your-videos) for more information.  # noqa: E501

        :param master_access: The master_access of this CreateAssetRequest.  # noqa: E501
        :type master_access: str
        """
        allowed_values = ["none", "temporary"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and master_access not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `master_access` ({0}), must be one of {1}"  # noqa: E501
                .format(master_access, allowed_values)
            )

        self._master_access = master_access

    @property
    def test(self):
        """Gets the test of this CreateAssetRequest.  # noqa: E501

        Marks the asset as a test asset when the value is set to true. A Test asset can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test assets created. Test asset are watermarked with the Mux logo, limited to 10 seconds, deleted after 24 hrs.  # noqa: E501

        :return: The test of this CreateAssetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this CreateAssetRequest.

        Marks the asset as a test asset when the value is set to true. A Test asset can help evaluate the Mux Video APIs without incurring any cost. There is no limit on number of test assets created. Test asset are watermarked with the Mux logo, limited to 10 seconds, deleted after 24 hrs.  # noqa: E501

        :param test: The test of this CreateAssetRequest.  # noqa: E501
        :type test: bool
        """

        self._test = test

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
        if not isinstance(other, CreateAssetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAssetRequest):
            return True

        return self.to_dict() != other.to_dict()
