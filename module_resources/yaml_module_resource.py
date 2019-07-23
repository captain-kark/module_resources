import yaml

from .module_resources import ModuleResource

LOADER = yaml.SafeLoader

MODULE_DESCRIPTION = "YAML configuration file"
FILENAME_GLOB = "*.yaml"

def namedtuple_constructor(loader, node):
    mapping = loader.construct_mapping(node)
    yield ModuleResource.mapping_to_namedtuple(mapping, loader.spec, 'yaml')


yaml.add_constructor('tag:yaml.org,2002:map', namedtuple_constructor, Loader=LOADER)

class YamlModuleResource(ModuleResource):
    def __init__(self, name, path, description=MODULE_DESCRIPTION, glob=FILENAME_GLOB):
        super().__init__(name, path, description, glob)

    def create_module(self, spec):
        yaml_filepath = self.import_request_to_filepath(spec)
        yaml.SafeLoader.spec = spec
        module_object = yaml.safe_load(yaml_filepath.read_text())
        yaml.SafeLoader.spec = None
        return module_object
