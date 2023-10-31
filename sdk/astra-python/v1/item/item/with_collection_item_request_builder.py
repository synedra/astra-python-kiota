from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.command_result import CommandResult
    from ....models.count_documents_commands import CountDocumentsCommands
    from ....models.delete_many_command import DeleteManyCommand
    from ....models.delete_one_command import DeleteOneCommand
    from ....models.find_command import FindCommand
    from ....models.find_one_and_delete_command import FindOneAndDeleteCommand
    from ....models.find_one_and_replace_command.find_one_and_replace_command import FindOneAndReplaceCommand
    from ....models.find_one_and_update_command.find_one_and_update_command import FindOneAndUpdateCommand
    from ....models.find_one_command import FindOneCommand
    from ....models.insert_many_command.insert_many_command import InsertManyCommand
    from ....models.insert_one_command import InsertOneCommand
    from ....models.update_many_command.update_many_command import UpdateManyCommand
    from ....models.update_one_command.update_one_command import UpdateOneCommand

class WithCollectionItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/{namespace}/{collection}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WithCollectionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/{namespace}/{collection}", path_parameters)
    
    async def post(self,body: Optional[Union[Union[Union[Union[Union[Union[Union[Union[Union[Union[Union[CountDocumentsCommands, DeleteManyCommand], DeleteOneCommand], FindCommand], FindOneAndDeleteCommand], FindOneAndReplaceCommand], FindOneAndUpdateCommand], FindOneCommand], InsertManyCommand], InsertOneCommand], UpdateManyCommand], UpdateOneCommand]] = None, request_configuration: Optional[WithCollectionItemRequestBuilderPostRequestConfiguration] = None) -> Optional[CommandResult]:
        """
        Executes a single command against a collection.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CommandResult]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.command_result import CommandResult

        return await self.request_adapter.send_async(request_info, CommandResult, None)
    
    def to_post_request_information(self,body: Optional[Union[Union[Union[Union[Union[Union[Union[Union[Union[Union[Union[CountDocumentsCommands, DeleteManyCommand], DeleteOneCommand], FindCommand], FindOneAndDeleteCommand], FindOneAndReplaceCommand], FindOneAndUpdateCommand], FindOneCommand], InsertManyCommand], InsertOneCommand], UpdateManyCommand], UpdateOneCommand]] = None, request_configuration: Optional[WithCollectionItemRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Executes a single command against a collection.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_scalar(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> WithCollectionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCollectionItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return WithCollectionItemRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WithCollectionItemRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

