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


class UpdateAssetMasterAccessRequest(object):
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
        'master_access': 'str'
    }

    attribute_map = {
        'master_access': 'master_access'
    }

    def __init__(self, master_access=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAssetMasterAccessRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._master_access = None
        self.discriminator = None

        if master_access is not None:
            self.master_access = master_access

    @property
    def master_access(self):
        """Gets the master_access of this UpdateAssetMasterAccessRequest.  # noqa: E501

        Add or remove access to the master version of the video.  # noqa: E501

        :return: The master_access of this UpdateAssetMasterAccessRequest.  # noqa: E501
        :rtype: str
        """
        return self._master_access

    @master_access.setter
    def master_access(self, master_access):
        """Sets the master_access of this UpdateAssetMasterAccessRequest.

        Add or remove access to the master version of the video.  # noqa: E501

        :param master_access: The master_access of this UpdateAssetMasterAccessRequest.  # noqa: E501
        :type master_access: str
        """
        allowed_values = ["temporary", "none"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and master_access not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `master_access` ({0}), must be one of {1}"  # noqa: E501
                .format(master_access, allowed_values)
            )

        self._master_access = master_access

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
        if not isinstance(other, UpdateAssetMasterAccessRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAssetMasterAccessRequest):
            return True

        return self.to_dict() != other.to_dict()
