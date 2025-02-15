# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contrib/envoy/extensions/filters/network/rocketmq_proxy/v3/route.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.config.route.v3 import route_components_pb2 as envoy_dot_config_dot_route_dot_v3_dot_route__components__pb2
from envoy.type.matcher.v3 import string_pb2 as envoy_dot_type_dot_matcher_dot_v3_dot_string__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFcontrib/envoy/extensions/filters/network/rocketmq_proxy/v3/route.proto\x12\x32\x65nvoy.extensions.filters.network.rocketmq_proxy.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a,envoy/config/route/v3/route_components.proto\x1a\"envoy/type/matcher/v3/string.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"m\n\x12RouteConfiguration\x12\x0c\n\x04name\x18\x01 \x01(\t\x12I\n\x06routes\x18\x02 \x03(\x0b\x32\x39.envoy.extensions.filters.network.rocketmq_proxy.v3.Route\"\xba\x01\n\x05Route\x12W\n\x05match\x18\x01 \x01(\x0b\x32>.envoy.extensions.filters.network.rocketmq_proxy.v3.RouteMatchB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12X\n\x05route\x18\x02 \x01(\x0b\x32?.envoy.extensions.filters.network.rocketmq_proxy.v3.RouteActionB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"\x82\x01\n\nRouteMatch\x12=\n\x05topic\x18\x01 \x01(\x0b\x32$.envoy.type.matcher.v3.StringMatcherB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x35\n\x07headers\x18\x02 \x03(\x0b\x32$.envoy.config.route.v3.HeaderMatcher\"_\n\x0bRouteAction\x12\x18\n\x07\x63luster\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x36\n\x0emetadata_match\x18\x02 \x01(\x0b\x32\x1e.envoy.config.core.v3.MetadataB\xcc\x01\n@io.envoyproxy.envoy.extensions.filters.network.rocketmq_proxy.v3B\nRouteProtoP\x01Zrgithub.com/envoyproxy/go-control-plane/contrib/envoy/extensions/filters/network/rocketmq_proxy/v3;rocketmq_proxyv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'contrib.envoy.extensions.filters.network.rocketmq_proxy.v3.route_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n@io.envoyproxy.envoy.extensions.filters.network.rocketmq_proxy.v3B\nRouteProtoP\001Zrgithub.com/envoyproxy/go-control-plane/contrib/envoy/extensions/filters/network/rocketmq_proxy/v3;rocketmq_proxyv3\272\200\310\321\006\002\020\002'
  _ROUTE.fields_by_name['match']._options = None
  _ROUTE.fields_by_name['match']._serialized_options = b'\372B\005\212\001\002\020\001'
  _ROUTE.fields_by_name['route']._options = None
  _ROUTE.fields_by_name['route']._serialized_options = b'\372B\005\212\001\002\020\001'
  _ROUTEMATCH.fields_by_name['topic']._options = None
  _ROUTEMATCH.fields_by_name['topic']._serialized_options = b'\372B\005\212\001\002\020\001'
  _ROUTEACTION.fields_by_name['cluster']._options = None
  _ROUTEACTION.fields_by_name['cluster']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_ROUTECONFIGURATION']._serialized_start=297
  _globals['_ROUTECONFIGURATION']._serialized_end=406
  _globals['_ROUTE']._serialized_start=409
  _globals['_ROUTE']._serialized_end=595
  _globals['_ROUTEMATCH']._serialized_start=598
  _globals['_ROUTEMATCH']._serialized_end=728
  _globals['_ROUTEACTION']._serialized_start=730
  _globals['_ROUTEACTION']._serialized_end=825
# @@protoc_insertion_point(module_scope)
