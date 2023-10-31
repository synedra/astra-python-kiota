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
    from ..models.command_result import CommandResult
    from ..models.create_embedding_service_command import CreateEmbeddingServiceCommand
    from ..models.create_namespace_command.create_namespace_command import CreateNamespaceCommand
    from .item.with_namespace_item_request_builder import WithNamespaceItemRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1", path_parameters)
    
    def by_namespace(self,namespace: str) -> WithNamespaceItemRequestBuilder:
        """
        Gets an item from the AstraDBSDK.v1.item collection
        param namespace: The namespace where the collection is located.
        Returns: WithNamespaceItemRequestBuilder
        """
        if not namespace:
            raise TypeError("namespace cannot be null.")
        from .item.with_namespace_item_request_builder import WithNamespaceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["namespace"] = namespace
        return WithNamespaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: Optional[Union[CreateEmbeddingServiceCommand, CreateNamespaceCommand]] = None, request_configuration: Optional[V1RequestBuilderPostRequestConfiguration] = None) -> Optional[CommandResult]:
        """
        Executes a single general command.
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
        from ..models.command_result import CommandResult

        return await self.request_adapter.send_async(request_info, CommandResult, None)
    
    def to_post_request_information(self,body: Optional[Union[CreateEmbeddingServiceCommand, CreateNamespaceCommand]] = None, request_configuration: Optional[V1RequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Executes a single general command.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> V1RequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: V1RequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return V1RequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class V1RequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

