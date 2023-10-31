from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..filter_clause import FilterClause
    from ..update_clause import UpdateClause
    from .options import Options

@dataclass
class UpdateManyCommand(Parsable):
    """
    Command that finds documents from a collection and updates it with the values provided in the update clause.
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateManyCommand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateManyCommand
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UpdateManyCommand()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..filter_clause import FilterClause
        from ..update_clause import UpdateClause
        from .options import Options

        from ..filter_clause import FilterClause
        from ..update_clause import UpdateClause
        from .options import Options

        fields: Dict[str, Callable[[Any], None]] = {
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(FilterClause)),
            "options": lambda n : setattr(self, 'options', n.get_object_value(Options)),
            "update": lambda n : setattr(self, 'update', n.get_object_value(UpdateClause)),
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
        writer.write_object_value("filter", self.filter)
        writer.write_object_value("options", self.options)
        writer.write_object_value("update", self.update)
    

