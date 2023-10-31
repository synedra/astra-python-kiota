from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class JsonNodeFactory(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> JsonNodeFactory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JsonNodeFactory
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return JsonNodeFactory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "_cfgBigDecimalExact": lambda n : setattr(self, '_cfg_big_decimal_exact', n.get_bool_value()),
            "maxElementIndexForInsert": lambda n : setattr(self, 'max_element_index_for_insert', n.get_int_value()),
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
        writer.write_bool_value("_cfgBigDecimalExact", self._cfg_big_decimal_exact)
        writer.write_int_value("maxElementIndexForInsert", self.max_element_index_for_insert)
    

