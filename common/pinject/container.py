import pinject
from pinject.object_graph import ObjectGraph

from common.pinject.sql_alchemy_session_service_binding_spec import SQLAlchemyBindingSpec


class Container:
    __container = None

    def __init__(self, config=None):
        if not config:
            raise Exception("Must be initialized with a valid config")
        binding_specs = [SQLAlchemyBindingSpec(dict(config))]

        Container.__container = pinject.new_object_graph(binding_specs=binding_specs, only_use_explicit_bindings=True)

    @staticmethod
    def get_object_graph() -> ObjectGraph:
        if not Container.__container:
            raise Exception("Container was not Initialized")

        return Container.__container
