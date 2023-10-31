from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_node_factory import JsonNodeFactory
    from .json_node_type import JsonNodeType
    from .object_node__children import ObjectNode__children

@dataclass
class ObjectNode(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ObjectNode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObjectNode
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ObjectNode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .json_node_factory import JsonNodeFactory
        from .json_node_type import JsonNodeType
        from .object_node__children import ObjectNode__children

        from .json_node_factory import JsonNodeFactory
        from .json_node_type import JsonNodeType
        from .object_node__children import ObjectNode__children

        fields: Dict[str, Callable[[Any], None]] = {
            "_children": lambda n : setattr(self, '_children', n.get_object_value(ObjectNode__children)),
            "_nodeFactory": lambda n : setattr(self, '_node_factory', n.get_object_value(JsonNodeFactory)),
            "array": lambda n : setattr(self, 'array', n.get_bool_value()),
            "bigDecimal": lambda n : setattr(self, 'big_decimal', n.get_bool_value()),
            "bigInteger": lambda n : setattr(self, 'big_integer', n.get_bool_value()),
            "binary": lambda n : setattr(self, 'binary', n.get_bool_value()),
            "boolean": lambda n : setattr(self, 'boolean', n.get_bool_value()),
            "containerNode": lambda n : setattr(self, 'container_node', n.get_bool_value()),
            "double": lambda n : setattr(self, 'double', n.get_bool_value()),
            "empty": lambda n : setattr(self, 'empty', n.get_bool_value()),
            "float": lambda n : setattr(self, 'float', n.get_bool_value()),
            "floatingPointNumber": lambda n : setattr(self, 'floating_point_number', n.get_bool_value()),
            "int": lambda n : setattr(self, 'int', n.get_bool_value()),
            "integralNumber": lambda n : setattr(self, 'integral_number', n.get_bool_value()),
            "long": lambda n : setattr(self, 'long', n.get_bool_value()),
            "missingNode": lambda n : setattr(self, 'missing_node', n.get_bool_value()),
            "nodeType": lambda n : setattr(self, 'node_type', n.get_enum_value(JsonNodeType)),
            "null": lambda n : setattr(self, 'null', n.get_bool_value()),
            "number": lambda n : setattr(self, 'number', n.get_bool_value()),
            "object": lambda n : setattr(self, 'object', n.get_bool_value()),
            "pojo": lambda n : setattr(self, 'pojo', n.get_bool_value()),
            "short": lambda n : setattr(self, 'short', n.get_bool_value()),
            "textual": lambda n : setattr(self, 'textual', n.get_bool_value()),
            "valueNode": lambda n : setattr(self, 'value_node', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("_children", self._children)
        writer.write_object_value("_nodeFactory", self._node_factory)
        writer.write_bool_value("array", self.array)
        writer.write_bool_value("bigDecimal", self.big_decimal)
        writer.write_bool_value("bigInteger", self.big_integer)
        writer.write_bool_value("binary", self.binary)
        writer.write_bool_value("boolean", self.boolean)
        writer.write_bool_value("containerNode", self.container_node)
        writer.write_bool_value("double", self.double)
        writer.write_bool_value("empty", self.empty)
        writer.write_bool_value("float", self.float)
        writer.write_bool_value("floatingPointNumber", self.floating_point_number)
        writer.write_bool_value("int", self.int)
        writer.write_bool_value("integralNumber", self.integral_number)
        writer.write_bool_value("long", self.long)
        writer.write_bool_value("missingNode", self.missing_node)
        writer.write_enum_value("nodeType", self.node_type)
        writer.write_bool_value("null", self.null)
        writer.write_bool_value("number", self.number)
        writer.write_bool_value("object", self.object)
        writer.write_bool_value("pojo", self.pojo)
        writer.write_bool_value("short", self.short)
        writer.write_bool_value("textual", self.textual)
        writer.write_bool_value("valueNode", self.value_node)
    

