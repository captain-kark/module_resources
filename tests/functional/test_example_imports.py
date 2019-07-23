def test_json_and_yaml_are_identical_dicts():
    from module_resources.examples.json import logging_config as json_logging_config
    from module_resources.examples.yaml import logging_config as yaml_logging_config

    assert dict(json_logging_config) == dict(yaml_logging_config)


def test_top_level_properties_are_importable():
    from module_resources.examples.json.logging_config import formatters as json_logging_formatters
    from module_resources.examples.yaml.logging_config import formatters as yaml_logging_formatters

    assert dict(json_logging_formatters) == dict(yaml_logging_formatters)
