# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AppPlatformManagementClientConfiguration
from .operations import (
    ApiPortalCustomDomainsOperations,
    ApiPortalsOperations,
    ApplicationAcceleratorsOperations,
    ApplicationLiveViewsOperations,
    AppsOperations,
    BindingsOperations,
    BuildServiceAgentPoolOperations,
    BuildServiceBuilderOperations,
    BuildServiceOperations,
    BuildpackBindingOperations,
    CertificatesOperations,
    ConfigServersOperations,
    ConfigurationServicesOperations,
    CustomDomainsOperations,
    CustomizedAcceleratorsOperations,
    DeploymentsOperations,
    DevToolPortalsOperations,
    GatewayCustomDomainsOperations,
    GatewayRouteConfigsOperations,
    GatewaysOperations,
    MonitoringSettingsOperations,
    Operations,
    PredefinedAcceleratorsOperations,
    RuntimeVersionsOperations,
    ServiceRegistriesOperations,
    ServicesOperations,
    SkusOperations,
    StoragesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class AppPlatformManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """REST API for Azure Spring Apps.

    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.appplatform.v2023_01_01_preview.operations.ServicesOperations
    :ivar config_servers: ConfigServersOperations operations
    :vartype config_servers:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.ConfigServersOperations
    :ivar configuration_services: ConfigurationServicesOperations operations
    :vartype configuration_services:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.ConfigurationServicesOperations
    :ivar service_registries: ServiceRegistriesOperations operations
    :vartype service_registries:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.ServiceRegistriesOperations
    :ivar application_live_views: ApplicationLiveViewsOperations operations
    :vartype application_live_views:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.ApplicationLiveViewsOperations
    :ivar dev_tool_portals: DevToolPortalsOperations operations
    :vartype dev_tool_portals:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.DevToolPortalsOperations
    :ivar build_service: BuildServiceOperations operations
    :vartype build_service:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.BuildServiceOperations
    :ivar buildpack_binding: BuildpackBindingOperations operations
    :vartype buildpack_binding:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.BuildpackBindingOperations
    :ivar build_service_builder: BuildServiceBuilderOperations operations
    :vartype build_service_builder:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.BuildServiceBuilderOperations
    :ivar build_service_agent_pool: BuildServiceAgentPoolOperations operations
    :vartype build_service_agent_pool:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.BuildServiceAgentPoolOperations
    :ivar monitoring_settings: MonitoringSettingsOperations operations
    :vartype monitoring_settings:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.MonitoringSettingsOperations
    :ivar apps: AppsOperations operations
    :vartype apps: azure.mgmt.appplatform.v2023_01_01_preview.operations.AppsOperations
    :ivar bindings: BindingsOperations operations
    :vartype bindings: azure.mgmt.appplatform.v2023_01_01_preview.operations.BindingsOperations
    :ivar storages: StoragesOperations operations
    :vartype storages: azure.mgmt.appplatform.v2023_01_01_preview.operations.StoragesOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.CertificatesOperations
    :ivar custom_domains: CustomDomainsOperations operations
    :vartype custom_domains:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.CustomDomainsOperations
    :ivar deployments: DeploymentsOperations operations
    :vartype deployments:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.DeploymentsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.appplatform.v2023_01_01_preview.operations.Operations
    :ivar runtime_versions: RuntimeVersionsOperations operations
    :vartype runtime_versions:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.RuntimeVersionsOperations
    :ivar skus: SkusOperations operations
    :vartype skus: azure.mgmt.appplatform.v2023_01_01_preview.operations.SkusOperations
    :ivar gateways: GatewaysOperations operations
    :vartype gateways: azure.mgmt.appplatform.v2023_01_01_preview.operations.GatewaysOperations
    :ivar gateway_route_configs: GatewayRouteConfigsOperations operations
    :vartype gateway_route_configs:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.GatewayRouteConfigsOperations
    :ivar gateway_custom_domains: GatewayCustomDomainsOperations operations
    :vartype gateway_custom_domains:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.GatewayCustomDomainsOperations
    :ivar api_portals: ApiPortalsOperations operations
    :vartype api_portals:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.ApiPortalsOperations
    :ivar api_portal_custom_domains: ApiPortalCustomDomainsOperations operations
    :vartype api_portal_custom_domains:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.ApiPortalCustomDomainsOperations
    :ivar application_accelerators: ApplicationAcceleratorsOperations operations
    :vartype application_accelerators:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.ApplicationAcceleratorsOperations
    :ivar customized_accelerators: CustomizedAcceleratorsOperations operations
    :vartype customized_accelerators:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.CustomizedAcceleratorsOperations
    :ivar predefined_accelerators: PredefinedAcceleratorsOperations operations
    :vartype predefined_accelerators:
     azure.mgmt.appplatform.v2023_01_01_preview.operations.PredefinedAcceleratorsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-01-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AppPlatformManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.services = ServicesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.config_servers = ConfigServersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.configuration_services = ConfigurationServicesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.service_registries = ServiceRegistriesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.application_live_views = ApplicationLiveViewsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.dev_tool_portals = DevToolPortalsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.build_service = BuildServiceOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.buildpack_binding = BuildpackBindingOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.build_service_builder = BuildServiceBuilderOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.build_service_agent_pool = BuildServiceAgentPoolOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.monitoring_settings = MonitoringSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.apps = AppsOperations(self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview")
        self.bindings = BindingsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.storages = StoragesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.certificates = CertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.custom_domains = CustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.deployments = DeploymentsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.runtime_versions = RuntimeVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.skus = SkusOperations(self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview")
        self.gateways = GatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.gateway_route_configs = GatewayRouteConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.gateway_custom_domains = GatewayCustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.api_portals = ApiPortalsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.api_portal_custom_domains = ApiPortalCustomDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.application_accelerators = ApplicationAcceleratorsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.customized_accelerators = CustomizedAcceleratorsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )
        self.predefined_accelerators = PredefinedAcceleratorsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-01-01-preview"
        )

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "AppPlatformManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
