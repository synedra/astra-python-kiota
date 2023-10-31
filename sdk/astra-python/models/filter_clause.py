from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .comparison_expression import ComparisonExpression

@dataclass
class FilterClause(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilterClause:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterClause
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FilterClause()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .comparison_expression import ComparisonExpression

        from .comparison_expression import ComparisonExpression

        fields: Dict[str, Callable[[Any], None]] = {
            "comparisonExpressions": lambda n : setattr(self, 'comparison_expressions', n.get_collection_of_object_values(ComparisonExpression)),
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
        writer.write_collection_of_object_values("comparisonExpressions", self.comparison_expressions)
    

