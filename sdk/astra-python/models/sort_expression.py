from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SortExpression(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SortExpression:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SortExpression
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SortExpression()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ascending": lambda n : setattr(self, 'ascending', n.get_bool_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "vector": lambda n : setattr(self, 'vector', n.get_collection_of_primitive_values(float)),
            "vectorize": lambda n : setattr(self, 'vectorize', n.get_str_value()),
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
        writer.write_bool_value("ascending", self.ascending)
        writer.write_str_value("path", self.path)
        writer.write_collection_of_primitive_values("vector", self.vector)
        writer.write_str_value("vectorize", self.vectorize)
    

