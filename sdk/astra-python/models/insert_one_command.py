from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .insert_one_command_document import InsertOneCommand_document
    from .json_node import JsonNode

@dataclass
class InsertOneCommand(Parsable):
    """
    Command that inserts a single JSON document to a collection.
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InsertOneCommand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InsertOneCommand
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InsertOneCommand()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .insert_one_command_document import InsertOneCommand_document
        from .json_node import JsonNode

        from .insert_one_command_document import InsertOneCommand_document
        from .json_node import JsonNode

        fields: Dict[str, Callable[[Any], None]] = {
            "document": lambda n : setattr(self, 'document', n.get_object_value(InsertOneCommand_document)),
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
        writer.write_object_value("document", self.document)
        writer.write_object_value("options", self.options)
    

