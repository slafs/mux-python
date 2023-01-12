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


class ExportDate(object):
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
        'export_date': 'date',
        'files': 'list[ExportFile]'
    }

    attribute_map = {
        'export_date': 'export_date',
        'files': 'files'
    }

    def __init__(self, export_date=None, files=None, local_vars_configuration=None):  # noqa: E501
        """ExportDate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._export_date = None
        self._files = None
        self.discriminator = None

        if export_date is not None:
            self.export_date = export_date
        if files is not None:
            self.files = files

    @property
    def export_date(self):
        """Gets the export_date of this ExportDate.  # noqa: E501


        :return: The export_date of this ExportDate.  # noqa: E501
        :rtype: date
        """
        return self._export_date

    @export_date.setter
    def export_date(self, export_date):
        """Sets the export_date of this ExportDate.


        :param export_date: The export_date of this ExportDate.  # noqa: E501
        :type export_date: date
        """

        self._export_date = export_date

    @property
    def files(self):
        """Gets the files of this ExportDate.  # noqa: E501


        :return: The files of this ExportDate.  # noqa: E501
        :rtype: list[ExportFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ExportDate.


        :param files: The files of this ExportDate.  # noqa: E501
        :type files: list[ExportFile]
        """

        self._files = files

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
        if not isinstance(other, ExportDate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportDate):
            return True

        return self.to_dict() != other.to_dict()
