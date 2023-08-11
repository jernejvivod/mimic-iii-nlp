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


class ClinicalTextConfig(object):
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
        'foreign_key_path': 'list[str]',
        'text_property_name': 'str',
        'clinical_text_entity_id_property_name': 'str',
        'clinical_text_date_time_properties_names': 'list[str]',
        'root_entity_datetime_property_for_cutoff': 'str',
        'root_entities_spec': 'RootEntitiesSpec',
        'clinical_text_extraction_duration_spec': 'ClinicalTextExtractionDurationSpec'
    }

    attribute_map = {
        'foreign_key_path': 'foreignKeyPath',
        'text_property_name': 'textPropertyName',
        'clinical_text_entity_id_property_name': 'clinicalTextEntityIdPropertyName',
        'clinical_text_date_time_properties_names': 'clinicalTextDateTimePropertiesNames',
        'root_entity_datetime_property_for_cutoff': 'rootEntityDatetimePropertyForCutoff',
        'root_entities_spec': 'rootEntitiesSpec',
        'clinical_text_extraction_duration_spec': 'clinicalTextExtractionDurationSpec'
    }

    def __init__(self, foreign_key_path=None, text_property_name=None, clinical_text_entity_id_property_name=None, clinical_text_date_time_properties_names=None, root_entity_datetime_property_for_cutoff=None, root_entities_spec=None, clinical_text_extraction_duration_spec=None, local_vars_configuration=None):  # noqa: E501
        """ClinicalTextConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._foreign_key_path = None
        self._text_property_name = None
        self._clinical_text_entity_id_property_name = None
        self._clinical_text_date_time_properties_names = None
        self._root_entity_datetime_property_for_cutoff = None
        self._root_entities_spec = None
        self._clinical_text_extraction_duration_spec = None
        self.discriminator = None

        self.foreign_key_path = foreign_key_path
        self.text_property_name = text_property_name
        if clinical_text_entity_id_property_name is not None:
            self.clinical_text_entity_id_property_name = clinical_text_entity_id_property_name
        if clinical_text_date_time_properties_names is not None:
            self.clinical_text_date_time_properties_names = clinical_text_date_time_properties_names
        if root_entity_datetime_property_for_cutoff is not None:
            self.root_entity_datetime_property_for_cutoff = root_entity_datetime_property_for_cutoff
        self.root_entities_spec = root_entities_spec
        if clinical_text_extraction_duration_spec is not None:
            self.clinical_text_extraction_duration_spec = clinical_text_extraction_duration_spec

    @property
    def foreign_key_path(self):
        """Gets the foreign_key_path of this ClinicalTextConfig.  # noqa: E501


        :return: The foreign_key_path of this ClinicalTextConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._foreign_key_path

    @foreign_key_path.setter
    def foreign_key_path(self, foreign_key_path):
        """Sets the foreign_key_path of this ClinicalTextConfig.


        :param foreign_key_path: The foreign_key_path of this ClinicalTextConfig.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and foreign_key_path is None:  # noqa: E501
            raise ValueError("Invalid value for `foreign_key_path`, must not be `None`")  # noqa: E501

        self._foreign_key_path = foreign_key_path

    @property
    def text_property_name(self):
        """Gets the text_property_name of this ClinicalTextConfig.  # noqa: E501


        :return: The text_property_name of this ClinicalTextConfig.  # noqa: E501
        :rtype: str
        """
        return self._text_property_name

    @text_property_name.setter
    def text_property_name(self, text_property_name):
        """Sets the text_property_name of this ClinicalTextConfig.


        :param text_property_name: The text_property_name of this ClinicalTextConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text_property_name is None:  # noqa: E501
            raise ValueError("Invalid value for `text_property_name`, must not be `None`")  # noqa: E501

        self._text_property_name = text_property_name

    @property
    def clinical_text_entity_id_property_name(self):
        """Gets the clinical_text_entity_id_property_name of this ClinicalTextConfig.  # noqa: E501


        :return: The clinical_text_entity_id_property_name of this ClinicalTextConfig.  # noqa: E501
        :rtype: str
        """
        return self._clinical_text_entity_id_property_name

    @clinical_text_entity_id_property_name.setter
    def clinical_text_entity_id_property_name(self, clinical_text_entity_id_property_name):
        """Sets the clinical_text_entity_id_property_name of this ClinicalTextConfig.


        :param clinical_text_entity_id_property_name: The clinical_text_entity_id_property_name of this ClinicalTextConfig.  # noqa: E501
        :type: str
        """

        self._clinical_text_entity_id_property_name = clinical_text_entity_id_property_name

    @property
    def clinical_text_date_time_properties_names(self):
        """Gets the clinical_text_date_time_properties_names of this ClinicalTextConfig.  # noqa: E501


        :return: The clinical_text_date_time_properties_names of this ClinicalTextConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._clinical_text_date_time_properties_names

    @clinical_text_date_time_properties_names.setter
    def clinical_text_date_time_properties_names(self, clinical_text_date_time_properties_names):
        """Sets the clinical_text_date_time_properties_names of this ClinicalTextConfig.


        :param clinical_text_date_time_properties_names: The clinical_text_date_time_properties_names of this ClinicalTextConfig.  # noqa: E501
        :type: list[str]
        """

        self._clinical_text_date_time_properties_names = clinical_text_date_time_properties_names

    @property
    def root_entity_datetime_property_for_cutoff(self):
        """Gets the root_entity_datetime_property_for_cutoff of this ClinicalTextConfig.  # noqa: E501


        :return: The root_entity_datetime_property_for_cutoff of this ClinicalTextConfig.  # noqa: E501
        :rtype: str
        """
        return self._root_entity_datetime_property_for_cutoff

    @root_entity_datetime_property_for_cutoff.setter
    def root_entity_datetime_property_for_cutoff(self, root_entity_datetime_property_for_cutoff):
        """Sets the root_entity_datetime_property_for_cutoff of this ClinicalTextConfig.


        :param root_entity_datetime_property_for_cutoff: The root_entity_datetime_property_for_cutoff of this ClinicalTextConfig.  # noqa: E501
        :type: str
        """

        self._root_entity_datetime_property_for_cutoff = root_entity_datetime_property_for_cutoff

    @property
    def root_entities_spec(self):
        """Gets the root_entities_spec of this ClinicalTextConfig.  # noqa: E501


        :return: The root_entities_spec of this ClinicalTextConfig.  # noqa: E501
        :rtype: RootEntitiesSpec
        """
        return self._root_entities_spec

    @root_entities_spec.setter
    def root_entities_spec(self, root_entities_spec):
        """Sets the root_entities_spec of this ClinicalTextConfig.


        :param root_entities_spec: The root_entities_spec of this ClinicalTextConfig.  # noqa: E501
        :type: RootEntitiesSpec
        """
        if self.local_vars_configuration.client_side_validation and root_entities_spec is None:  # noqa: E501
            raise ValueError("Invalid value for `root_entities_spec`, must not be `None`")  # noqa: E501

        self._root_entities_spec = root_entities_spec

    @property
    def clinical_text_extraction_duration_spec(self):
        """Gets the clinical_text_extraction_duration_spec of this ClinicalTextConfig.  # noqa: E501


        :return: The clinical_text_extraction_duration_spec of this ClinicalTextConfig.  # noqa: E501
        :rtype: ClinicalTextExtractionDurationSpec
        """
        return self._clinical_text_extraction_duration_spec

    @clinical_text_extraction_duration_spec.setter
    def clinical_text_extraction_duration_spec(self, clinical_text_extraction_duration_spec):
        """Sets the clinical_text_extraction_duration_spec of this ClinicalTextConfig.


        :param clinical_text_extraction_duration_spec: The clinical_text_extraction_duration_spec of this ClinicalTextConfig.  # noqa: E501
        :type: ClinicalTextExtractionDurationSpec
        """

        self._clinical_text_extraction_duration_spec = clinical_text_extraction_duration_spec

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
        if not isinstance(other, ClinicalTextConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClinicalTextConfig):
            return True

        return self.to_dict() != other.to_dict()