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


class MonitoringBreakdownValue(object):
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
        'value': 'str',
        'negative_impact': 'int',
        'metric_value': 'float',
        'display_value': 'str',
        'concurrent_viewers': 'int'
    }

    attribute_map = {
        'value': 'value',
        'negative_impact': 'negative_impact',
        'metric_value': 'metric_value',
        'display_value': 'display_value',
        'concurrent_viewers': 'concurrent_viewers'
    }

    def __init__(self, value=None, negative_impact=None, metric_value=None, display_value=None, concurrent_viewers=None, local_vars_configuration=None):  # noqa: E501
        """MonitoringBreakdownValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._negative_impact = None
        self._metric_value = None
        self._display_value = None
        self._concurrent_viewers = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if negative_impact is not None:
            self.negative_impact = negative_impact
        if metric_value is not None:
            self.metric_value = metric_value
        if display_value is not None:
            self.display_value = display_value
        if concurrent_viewers is not None:
            self.concurrent_viewers = concurrent_viewers

    @property
    def value(self):
        """Gets the value of this MonitoringBreakdownValue.  # noqa: E501


        :return: The value of this MonitoringBreakdownValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MonitoringBreakdownValue.


        :param value: The value of this MonitoringBreakdownValue.  # noqa: E501
        :type value: str
        """

        self._value = value

    @property
    def negative_impact(self):
        """Gets the negative_impact of this MonitoringBreakdownValue.  # noqa: E501


        :return: The negative_impact of this MonitoringBreakdownValue.  # noqa: E501
        :rtype: int
        """
        return self._negative_impact

    @negative_impact.setter
    def negative_impact(self, negative_impact):
        """Sets the negative_impact of this MonitoringBreakdownValue.


        :param negative_impact: The negative_impact of this MonitoringBreakdownValue.  # noqa: E501
        :type negative_impact: int
        """

        self._negative_impact = negative_impact

    @property
    def metric_value(self):
        """Gets the metric_value of this MonitoringBreakdownValue.  # noqa: E501


        :return: The metric_value of this MonitoringBreakdownValue.  # noqa: E501
        :rtype: float
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        """Sets the metric_value of this MonitoringBreakdownValue.


        :param metric_value: The metric_value of this MonitoringBreakdownValue.  # noqa: E501
        :type metric_value: float
        """

        self._metric_value = metric_value

    @property
    def display_value(self):
        """Gets the display_value of this MonitoringBreakdownValue.  # noqa: E501


        :return: The display_value of this MonitoringBreakdownValue.  # noqa: E501
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        """Sets the display_value of this MonitoringBreakdownValue.


        :param display_value: The display_value of this MonitoringBreakdownValue.  # noqa: E501
        :type display_value: str
        """

        self._display_value = display_value

    @property
    def concurrent_viewers(self):
        """Gets the concurrent_viewers of this MonitoringBreakdownValue.  # noqa: E501


        :return: The concurrent_viewers of this MonitoringBreakdownValue.  # noqa: E501
        :rtype: int
        """
        return self._concurrent_viewers

    @concurrent_viewers.setter
    def concurrent_viewers(self, concurrent_viewers):
        """Sets the concurrent_viewers of this MonitoringBreakdownValue.


        :param concurrent_viewers: The concurrent_viewers of this MonitoringBreakdownValue.  # noqa: E501
        :type concurrent_viewers: int
        """

        self._concurrent_viewers = concurrent_viewers

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
        if not isinstance(other, MonitoringBreakdownValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MonitoringBreakdownValue):
            return True

        return self.to_dict() != other.to_dict()
