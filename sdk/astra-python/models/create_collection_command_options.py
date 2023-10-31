from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_collection_command_options_vector import CreateCollectionCommand_options_vector
    from .create_collection_command_options_vectorize import CreateCollectionCommand_options_vectorize

@dataclass
class CreateCollectionCommand_options(Parsable):
    """
    Configuration for the collection
    """
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateCollectionCommand_options:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateCollectionCommand_options
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CreateCollectionCommand_options()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .create_collection_command_options_vector import CreateCollectionCommand_options_vector
        from .create_collection_command_options_vectorize import CreateCollectionCommand_options_vectorize

        from .create_collection_command_options_vector import CreateCollectionCommand_options_vector
        from .create_collection_command_options_vectorize import CreateCollectionCommand_options_vectorize

        fields: Dict[str, Callable[[Any], None]] = {
            "vector": lambda n : setattr(self, 'vector', n.get_object_value(CreateCollectionCommand_options_vector)),
            "vectorize": lambda n : setattr(self, 'vectorize', n.get_object_value(CreateCollectionCommand_options_vectorize)),
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
        writer.write_object_value("vector", self.vector)
        writer.write_object_value("vectorize", self.vectorize)
    

