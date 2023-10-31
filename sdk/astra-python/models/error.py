from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Error(Parsable):
    """
    List of errors that occurred during a command execution. Can include additional properties besides the message that is always provided, like `errorCode`, `exceptionClass`, etc.
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Error:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Error
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Error()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
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
        writer.write_str_value("message", self.message)
    

