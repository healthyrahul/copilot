# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todolist.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todolist.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0etodolist.proto\"5\n\x05Thing\x12\r\n\x05\x66irst\x18\x01 \x01(\t\x12\x0e\n\x06second\x18\x02 \x01(\x08\x12\r\n\x05third\x18\x03 \x01(\x05\x62\x06proto3')
)




_THING = _descriptor.Descriptor(
  name='Thing',
  full_name='Thing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='Thing.first', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='Thing.second', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='third', full_name='Thing.third', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['Thing'] = _THING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Thing = _reflection.GeneratedProtocolMessageType('Thing', (_message.Message,), dict(
  DESCRIPTOR = _THING,
  __module__ = 'todolist_pb2'
  # @@protoc_insertion_point(class_scope:Thing)
  ))
_sym_db.RegisterMessage(Thing)


# @@protoc_insertion_point(module_scope)
