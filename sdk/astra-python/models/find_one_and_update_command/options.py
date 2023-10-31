from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Options(Parsable):
    """
    Options for `findOneAndUpdate` command.
    """
    # Specifies which document to perform the projection on. If `before` the projection is performed on the document before the update is applied, if `after` the document projection is from the document after the update.
    return_document: Optional[str] = "before"
    # When `true`, if no documents match the `filter` clause the command will create a new _empty_ document and apply the `update` clause and all equality filters to the empty document.
    upsert: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Options:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Options
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Options()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "returnDocument": lambda n : setattr(self, 'return_document', n.get_str_value()),
            "upsert": lambda n : setattr(self, 'upsert', n.get_bool_value()),
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
        writer.write_str_value("returnDocument", self.return_document)
        writer.write_bool_value("upsert", self.upsert)
    

