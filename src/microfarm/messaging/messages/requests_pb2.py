# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages/requests.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17messages/requests.proto\"6\n\x13RegistrationRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\x0c\"\x1d\n\x0cTokenRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"6\n\x16RegistrationValidation\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"<\n\x1a\x43\x65rtificateCreationRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\"L\n\x1c\x43\x65rtificateRevocationRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06serial\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages.requests_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REGISTRATIONREQUEST']._serialized_start=27
  _globals['_REGISTRATIONREQUEST']._serialized_end=81
  _globals['_TOKENREQUEST']._serialized_start=83
  _globals['_TOKENREQUEST']._serialized_end=112
  _globals['_REGISTRATIONVALIDATION']._serialized_start=114
  _globals['_REGISTRATIONVALIDATION']._serialized_end=168
  _globals['_CERTIFICATECREATIONREQUEST']._serialized_start=170
  _globals['_CERTIFICATECREATIONREQUEST']._serialized_end=230
  _globals['_CERTIFICATEREVOCATIONREQUEST']._serialized_start=232
  _globals['_CERTIFICATEREVOCATIONREQUEST']._serialized_end=308
# @@protoc_insertion_point(module_scope)
