from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .update_clause_update_operation_defs import UpdateClause_updateOperationDefs

@dataclass
class UpdateClause(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateClause:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateClause
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdateClause()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .update_clause_update_operation_defs import UpdateClause_updateOperationDefs

        from .update_clause_update_operation_defs import UpdateClause_updateOperationDefs

        fields: Dict[str, Callable[[Any], None]] = {
            "updateOperationDefs": lambda n : setattr(self, 'update_operation_defs', n.get_object_value(UpdateClause_updateOperationDefs)),
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
        writer.write_object_value("updateOperationDefs", self.update_operation_defs)
    

