from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..filter_clause import FilterClause
    from ..json_node import JsonNode
    from ..object_node import ObjectNode
    from ..sort_clause import SortClause
    from .options import Options

@dataclass
class FindOneAndReplaceCommand(Parsable):
    """
    Command that finds a single JSON document from a collection and replaces it with the replacement document.
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FindOneAndReplaceCommand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FindOneAndReplaceCommand
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FindOneAndReplaceCommand()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..filter_clause import FilterClause
        from ..json_node import JsonNode
        from ..object_node import ObjectNode
        from ..sort_clause import SortClause
        from .options import Options

        from ..filter_clause import FilterClause
        from ..json_node import JsonNode
        from ..object_node import ObjectNode
        from ..sort_clause import SortClause
        from .options import Options

        fields: Dict[str, Callable[[Any], None]] = {
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(FilterClause)),
            "options": lambda n : setattr(self, 'options', n.get_object_value(Options)),
            "projection": lambda n : setattr(self, 'projection', n.get_object_value(JsonNode)),
            "replacement": lambda n : setattr(self, 'replacement', n.get_object_value(ObjectNode)),
            "sort": lambda n : setattr(self, 'sort', n.get_object_value(SortClause)),
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
        writer.write_object_value("projection", self.projection)
        writer.write_object_value("replacement", self.replacement)
        writer.write_object_value("sort", self.sort)
    

