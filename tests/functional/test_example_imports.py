from module_resources.examples.json import logging_config as json_logging_config
from module_resources.examples.yaml import logging_config as yaml_logging_config

def test_json_and_yaml_are_identical_dicts():
    assert dict(json_logging_config) == dict(yaml_logging_config)
