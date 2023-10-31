from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Options1(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Options1:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Options1
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Options1()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "includeSimilarity": lambda n : setattr(self, 'include_similarity', n.get_bool_value()),
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "pagingState": lambda n : setattr(self, 'paging_state', n.get_str_value()),
            "skip": lambda n : setattr(self, 'skip', n.get_int_value()),
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
        writer.write_bool_value("includeSimilarity", self.include_similarity)
        writer.write_int_value("limit", self.limit)
        writer.write_str_value("pagingState", self.paging_state)
        writer.write_int_value("skip", self.skip)
    

