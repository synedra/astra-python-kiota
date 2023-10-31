from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_node import JsonNode

@dataclass
class CreateEmbeddingServiceCommand(Parsable):
    """
    Command that create embedding service configuration.
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateEmbeddingServiceCommand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateEmbeddingServiceCommand
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CreateEmbeddingServiceCommand()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .json_node import JsonNode

        from .json_node import JsonNode

        fields: Dict[str, Callable[[Any], None]] = {
            "apiKey": lambda n : setattr(self, 'api_key', n.get_str_value()),
            "apiProvider": lambda n : setattr(self, 'api_provider', n.get_str_value()),
            "baseUrl": lambda n : setattr(self, 'base_url', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "options": lambda n : setattr(self, 'options', n.get_object_value(JsonNode)),
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
        writer.write_str_value("apiKey", self.api_key)
        writer.write_str_value("apiProvider", self.api_provider)
        writer.write_str_value("baseUrl", self.base_url)
        writer.write_str_value("name", self.name)
        writer.write_object_value("options", self.options)
    

