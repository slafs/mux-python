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


class AssetStaticRenditionsFiles(object):
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
        'name': 'str',
        'ext': 'str',
        'height': 'int',
        'width': 'int',
        'bitrate': 'int',
        'filesize': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ext': 'ext',
        'height': 'height',
        'width': 'width',
        'bitrate': 'bitrate',
        'filesize': 'filesize'
    }

    def __init__(self, name=None, ext=None, height=None, width=None, bitrate=None, filesize=None, local_vars_configuration=None):  # noqa: E501
        """AssetStaticRenditionsFiles - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._ext = None
        self._height = None
        self._width = None
        self._bitrate = None
        self._filesize = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ext is not None:
            self.ext = ext
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if bitrate is not None:
            self.bitrate = bitrate
        if filesize is not None:
            self.filesize = filesize

    @property
    def name(self):
        """Gets the name of this AssetStaticRenditionsFiles.  # noqa: E501


        :return: The name of this AssetStaticRenditionsFiles.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetStaticRenditionsFiles.


        :param name: The name of this AssetStaticRenditionsFiles.  # noqa: E501
        :type name: str
        """
        allowed_values = ["low.mp4", "medium.mp4", "high.mp4", "audio.m4a"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def ext(self):
        """Gets the ext of this AssetStaticRenditionsFiles.  # noqa: E501

        Extension of the static rendition file  # noqa: E501

        :return: The ext of this AssetStaticRenditionsFiles.  # noqa: E501
        :rtype: str
        """
        return self._ext

    @ext.setter
    def ext(self, ext):
        """Sets the ext of this AssetStaticRenditionsFiles.

        Extension of the static rendition file  # noqa: E501

        :param ext: The ext of this AssetStaticRenditionsFiles.  # noqa: E501
        :type ext: str
        """
        allowed_values = ["mp4", "m4a"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and ext not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `ext` ({0}), must be one of {1}"  # noqa: E501
                .format(ext, allowed_values)
            )

        self._ext = ext

    @property
    def height(self):
        """Gets the height of this AssetStaticRenditionsFiles.  # noqa: E501

        The height of the static rendition's file in pixels  # noqa: E501

        :return: The height of this AssetStaticRenditionsFiles.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this AssetStaticRenditionsFiles.

        The height of the static rendition's file in pixels  # noqa: E501

        :param height: The height of this AssetStaticRenditionsFiles.  # noqa: E501
        :type height: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this AssetStaticRenditionsFiles.  # noqa: E501

        The width of the static rendition's file in pixels  # noqa: E501

        :return: The width of this AssetStaticRenditionsFiles.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this AssetStaticRenditionsFiles.

        The width of the static rendition's file in pixels  # noqa: E501

        :param width: The width of this AssetStaticRenditionsFiles.  # noqa: E501
        :type width: int
        """

        self._width = width

    @property
    def bitrate(self):
        """Gets the bitrate of this AssetStaticRenditionsFiles.  # noqa: E501

        The bitrate in bits per second  # noqa: E501

        :return: The bitrate of this AssetStaticRenditionsFiles.  # noqa: E501
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AssetStaticRenditionsFiles.

        The bitrate in bits per second  # noqa: E501

        :param bitrate: The bitrate of this AssetStaticRenditionsFiles.  # noqa: E501
        :type bitrate: int
        """

        self._bitrate = bitrate

    @property
    def filesize(self):
        """Gets the filesize of this AssetStaticRenditionsFiles.  # noqa: E501

        The file size in bytes  # noqa: E501

        :return: The filesize of this AssetStaticRenditionsFiles.  # noqa: E501
        :rtype: str
        """
        return self._filesize

    @filesize.setter
    def filesize(self, filesize):
        """Sets the filesize of this AssetStaticRenditionsFiles.

        The file size in bytes  # noqa: E501

        :param filesize: The filesize of this AssetStaticRenditionsFiles.  # noqa: E501
        :type filesize: str
        """

        self._filesize = filesize

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
        if not isinstance(other, AssetStaticRenditionsFiles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetStaticRenditionsFiles):
            return True

        return self.to_dict() != other.to_dict()
