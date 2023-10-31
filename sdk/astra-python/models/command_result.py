from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .command_result_status import CommandResult_status
    from .error import Error
    from .multi_response_data import MultiResponseData
    from .single_response_data import SingleResponseData

@dataclass
class CommandResult(Parsable):
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommandResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommandResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CommandResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .command_result_status import CommandResult_status
        from .error import Error
        from .multi_response_data import MultiResponseData
        from .single_response_data import SingleResponseData

        from .command_result_status import CommandResult_status
        from .error import Error
        from .multi_response_data import MultiResponseData
        from .single_response_data import SingleResponseData

        fields: Dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(MultiResponseData)),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(Error)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(CommandResult_status)),
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
        writer.write_object_value("data", self.data)
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_object_value("status", self.status)
    

