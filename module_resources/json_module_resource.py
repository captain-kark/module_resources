import json

from .module_resources import ModuleResource

MODULE_DESCRIPTION = "JSON file as a python namedtuple object"
FILENAME_GLOB = '*.json'

class NamedtupleDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        self.spec = kwargs.pop('spec')
        super().__init__(object_hook=self._object_hook, *args, **kwargs)

    def _object_hook(self, json_dict):
        return ModuleResource.mapping_to_namedtuple(json_dict, self.spec, 'json')


class JsonModuleResource(ModuleResource):
    def __init__(self, name, path, description=MODULE_DESCRIPTION, glob=FILENAME_GLOB):
        super().__init__(name, path, description, glob)

    def create_module(self, spec):
        json_filepath = self.import_request_to_filepath(spec)
        json_data = json_filepath.read_text()
        return json.loads(json_data, cls=NamedtupleDecoder, spec=spec)
