# coding: utf-8

"""
    EHR Explorer Processor API

    API for the EHR Explorer Processor microservice  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: vivod.jernej@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from generated_client.configuration import Configuration


class TargetExtractionSpec(object):
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
        'target_type': 'str',
        'ids': 'list[int]',
        'age_lim': 'int',
        'max_days_interval_positive': 'int',
        'max_days_death_after_last_positive': 'int'
    }

    attribute_map = {
        'target_type': 'targetType',
        'ids': 'ids',
        'age_lim': 'ageLim',
        'max_days_interval_positive': 'maxDaysIntervalPositive',
        'max_days_death_after_last_positive': 'maxDaysDeathAfterLastPositive'
    }

    def __init__(self, target_type=None, ids=None, age_lim=None, max_days_interval_positive=30, max_days_death_after_last_positive=30, local_vars_configuration=None):  # noqa: E501
        """TargetExtractionSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_type = None
        self._ids = None
        self._age_lim = None
        self._max_days_interval_positive = None
        self._max_days_death_after_last_positive = None
        self.discriminator = None

        self.target_type = target_type
        if ids is not None:
            self.ids = ids
        if age_lim is not None:
            self.age_lim = age_lim
        if max_days_interval_positive is not None:
            self.max_days_interval_positive = max_days_interval_positive
        if max_days_death_after_last_positive is not None:
            self.max_days_death_after_last_positive = max_days_death_after_last_positive

    @property
    def target_type(self):
        """Gets the target_type of this TargetExtractionSpec.  # noqa: E501


        :return: The target_type of this TargetExtractionSpec.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this TargetExtractionSpec.


        :param target_type: The target_type of this TargetExtractionSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_type is None:  # noqa: E501
            raise ValueError("Invalid value for `target_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PATIENT_DIED_DURING_ADMISSION", "HOSPITAL_READMISSION_HAPPENED", "ICU_STAY_READMISSION_HAPPENED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and target_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `target_type` ({0}), must be one of {1}"  # noqa: E501
                .format(target_type, allowed_values)
            )

        self._target_type = target_type

    @property
    def ids(self):
        """Gets the ids of this TargetExtractionSpec.  # noqa: E501


        :return: The ids of this TargetExtractionSpec.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this TargetExtractionSpec.


        :param ids: The ids of this TargetExtractionSpec.  # noqa: E501
        :type: list[int]
        """

        self._ids = ids

    @property
    def age_lim(self):
        """Gets the age_lim of this TargetExtractionSpec.  # noqa: E501


        :return: The age_lim of this TargetExtractionSpec.  # noqa: E501
        :rtype: int
        """
        return self._age_lim

    @age_lim.setter
    def age_lim(self, age_lim):
        """Sets the age_lim of this TargetExtractionSpec.


        :param age_lim: The age_lim of this TargetExtractionSpec.  # noqa: E501
        :type: int
        """

        self._age_lim = age_lim

    @property
    def max_days_interval_positive(self):
        """Gets the max_days_interval_positive of this TargetExtractionSpec.  # noqa: E501


        :return: The max_days_interval_positive of this TargetExtractionSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_days_interval_positive

    @max_days_interval_positive.setter
    def max_days_interval_positive(self, max_days_interval_positive):
        """Sets the max_days_interval_positive of this TargetExtractionSpec.


        :param max_days_interval_positive: The max_days_interval_positive of this TargetExtractionSpec.  # noqa: E501
        :type: int
        """

        self._max_days_interval_positive = max_days_interval_positive

    @property
    def max_days_death_after_last_positive(self):
        """Gets the max_days_death_after_last_positive of this TargetExtractionSpec.  # noqa: E501


        :return: The max_days_death_after_last_positive of this TargetExtractionSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_days_death_after_last_positive

    @max_days_death_after_last_positive.setter
    def max_days_death_after_last_positive(self, max_days_death_after_last_positive):
        """Sets the max_days_death_after_last_positive of this TargetExtractionSpec.


        :param max_days_death_after_last_positive: The max_days_death_after_last_positive of this TargetExtractionSpec.  # noqa: E501
        :type: int
        """

        self._max_days_death_after_last_positive = max_days_death_after_last_positive

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TargetExtractionSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetExtractionSpec):
            return True

        return self.to_dict() != other.to_dict()