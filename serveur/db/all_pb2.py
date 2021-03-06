# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: all.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='all.proto',
  package='',
  serialized_pb='\n\tall.proto\"\xbf\x02\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05\x61\x64min\x18\x02 \x01(\x08\x12\x18\n\x04info\x18\x03 \x01(\x0b\x32\n.User.Info\x12\x19\n\x11verification_code\x18\x04 \x01(\t\x12\x1a\n\x12has_verified_email\x18\x05 \x01(\x08\x12\x1a\n\x12stripe_customer_id\x18\x06 \x01(\t\x12\x1f\n\x17timestamp_creation_secs\x18\x07 \x01(\x03\x12(\n timestamp_last_modification_secs\x18\x08 \x01(\x04\x1a\x64\n\x04Info\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t\">\n\x07Product\x12\x12\n\nproduct_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tprice_usd\x18\x03 \x01(\x02\"\x84\x01\n\x04Sale\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12#\n\x08products\x18\x03 \x03(\x0b\x32\x11.Sale.ProductSale\x1a\x33\n\x0bProductSale\x12\x12\n\nproduct_id\x18\x01 \x01(\x03\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"A\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x10\n\x08remember\x18\x03 \x01(\x08\"J\n\x13RegistrationRequest\x12\x1d\n\tuser_info\x18\x01 \x01(\x0b\x32\n.User.Info\x12\x14\n\x0cstripe_token\x18\x02 \x01(\t')




_USER_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='User.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='User.Info.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='User.Info.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='User.Info.first_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='User.Info.last_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='User.Info.phone_number', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=233,
  serialized_end=333,
)

_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='User.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='admin', full_name='User.admin', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='User.info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verification_code', full_name='User.verification_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_verified_email', full_name='User.has_verified_email', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stripe_customer_id', full_name='User.stripe_customer_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_creation_secs', full_name='User.timestamp_creation_secs', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_last_modification_secs', full_name='User.timestamp_last_modification_secs', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_USER_INFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=14,
  serialized_end=333,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='Product.product_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Product.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_usd', full_name='Product.price_usd', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=335,
  serialized_end=397,
)


_SALE_PRODUCTSALE = _descriptor.Descriptor(
  name='ProductSale',
  full_name='Sale.ProductSale',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product_id', full_name='Sale.ProductSale.product_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='Sale.ProductSale.quantity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=481,
  serialized_end=532,
)

_SALE = _descriptor.Descriptor(
  name='Sale',
  full_name='Sale',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='Sale.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Sale.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='products', full_name='Sale.products', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SALE_PRODUCTSALE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=400,
  serialized_end=532,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='LoginRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remember', full_name='LoginRequest.remember', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=534,
  serialized_end=599,
)


_REGISTRATIONREQUEST = _descriptor.Descriptor(
  name='RegistrationRequest',
  full_name='RegistrationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='RegistrationRequest.user_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stripe_token', full_name='RegistrationRequest.stripe_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=601,
  serialized_end=675,
)

_USER_INFO.containing_type = _USER;
_USER.fields_by_name['info'].message_type = _USER_INFO
_SALE_PRODUCTSALE.containing_type = _SALE;
_SALE.fields_by_name['products'].message_type = _SALE_PRODUCTSALE
_REGISTRATIONREQUEST.fields_by_name['user_info'].message_type = _USER_INFO
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Sale'] = _SALE
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['RegistrationRequest'] = _REGISTRATIONREQUEST

class User(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Info(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _USER_INFO

    # @@protoc_insertion_point(class_scope:User.Info)
  DESCRIPTOR = _USER

  # @@protoc_insertion_point(class_scope:User)

class Product(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PRODUCT

  # @@protoc_insertion_point(class_scope:Product)

class Sale(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class ProductSale(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _SALE_PRODUCTSALE

    # @@protoc_insertion_point(class_scope:Sale.ProductSale)
  DESCRIPTOR = _SALE

  # @@protoc_insertion_point(class_scope:Sale)

class LoginRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINREQUEST

  # @@protoc_insertion_point(class_scope:LoginRequest)

class RegistrationRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTRATIONREQUEST

  # @@protoc_insertion_point(class_scope:RegistrationRequest)


# @@protoc_insertion_point(module_scope)
