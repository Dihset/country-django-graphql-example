from graphene import relay


class CustomNode(relay.Node):
    class Meta:
        name = "Node"

    @staticmethod
    def to_global_id(type_: str, pk: str):
        return f"{type_}:{pk}"

    @classmethod
    def from_global_id(cls, global_id: str):
        return global_id.split(":")
