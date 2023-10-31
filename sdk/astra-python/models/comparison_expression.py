from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .comparison_expression_filter_operations import ComparisonExpression_filterOperations

@dataclass
class ComparisonExpression(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ComparisonExpression:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComparisonExpression
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ComparisonExpression()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .comparison_expression_filter_operations import ComparisonExpression_filterOperations

        from .comparison_expression_filter_operations import ComparisonExpression_filterOperations

        fields: Dict[str, Callable[[Any], None]] = {
            "filterOperations": lambda n : setattr(self, 'filter_operations', n.get_collection_of_object_values(ComparisonExpression_filterOperations)),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
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
        writer.write_collection_of_object_values("filterOperations", self.filter_operations)
        writer.write_str_value("path", self.path)
    

