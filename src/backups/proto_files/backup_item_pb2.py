# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_files/backup_item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_files/backup_item.proto',
  package='backup_item',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dproto_files/backup_item.proto\x12\x0b\x62\x61\x63kup_item\"\x92\x07\n\nBackupItem\x12?\n\x0fpayment_session\x18\x01 \x01(\x0b\x32&.backup_item.BackupItem.PaymentSession\x12,\n\x05order\x18\x02 \x01(\x0b\x32\x1d.backup_item.BackupItem.Order\x12*\n\x04user\x18\x03 \x01(\x0b\x32\x1c.backup_item.BackupItem.User\x1a\xa7\x02\n\x0ePaymentSession\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x10\n\x08order_id\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x11\n\tuser_name\x18\x05 \x01(\t\x12\x14\n\x0cuser_surname\x18\x06 \x01(\t\x12\x1a\n\x12user_email_address\x18\x07 \x01(\t\x12\x19\n\x11user_phone_number\x18\x08 \x01(\t\x12\x16\n\x0e\x62\x61nk_card_mask\x18\t \x01(\t\x12\x14\n\x0corder_tariff\x18\n \x01(\t\x12\x14\n\x0corder_amount\x18\x0b \x01(\x05\x12\x16\n\x0eorder_currency\x18\x0c \x01(\t\x12\x1b\n\x13order_refund_amount\x18\r \x01(\x05\x1a\xde\x02\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x14\n\x0c\x62\x61nk_card_id\x18\x03 \x01(\t\x12\x1a\n\x12payment_session_id\x18\x04 \x01(\t\x12\x0e\n\x06tariff\x18\x05 \x01(\t\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x05\x12\x10\n\x08\x63urrency\x18\x07 \x01(\t\x12\x15\n\rrefund_amount\x18\x08 \x01(\x05\x12(\n meta_information_simple_number_1\x18\t \x01(\t\x12\x34\n,human_is_all_too_human_coding_for_free_minds\x18\n \x01(\t\x12(\n in_an_hour_of_unprecedented_heat\x18\x0b \x01(\t\x12\x1f\n\x17i_am_part_of_that_force\x18\x0c \x01(\t\x12\x12\n\ncreated_at\x18\r \x01(\t\x1a^\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\x12\x15\n\remail_address\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\tb\x06proto3')
)




_BACKUPITEM_PAYMENTSESSION = _descriptor.Descriptor(
  name='PaymentSession',
  full_name='backup_item.BackupItem.PaymentSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='backup_item.BackupItem.PaymentSession.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='backup_item.BackupItem.PaymentSession.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='backup_item.BackupItem.PaymentSession.order_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='backup_item.BackupItem.PaymentSession.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='backup_item.BackupItem.PaymentSession.user_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_surname', full_name='backup_item.BackupItem.PaymentSession.user_surname', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_email_address', full_name='backup_item.BackupItem.PaymentSession.user_email_address', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_phone_number', full_name='backup_item.BackupItem.PaymentSession.user_phone_number', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank_card_mask', full_name='backup_item.BackupItem.PaymentSession.bank_card_mask', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_tariff', full_name='backup_item.BackupItem.PaymentSession.order_tariff', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_amount', full_name='backup_item.BackupItem.PaymentSession.order_amount', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_currency', full_name='backup_item.BackupItem.PaymentSession.order_currency', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_refund_amount', full_name='backup_item.BackupItem.PaymentSession.order_refund_amount', index=12,
      number=13, type=5, cpp_type=1, label=1,
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
  serialized_start=217,
  serialized_end=512,
)

_BACKUPITEM_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='backup_item.BackupItem.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='backup_item.BackupItem.Order.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='backup_item.BackupItem.Order.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank_card_id', full_name='backup_item.BackupItem.Order.bank_card_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_session_id', full_name='backup_item.BackupItem.Order.payment_session_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tariff', full_name='backup_item.BackupItem.Order.tariff', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='backup_item.BackupItem.Order.amount', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='backup_item.BackupItem.Order.currency', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refund_amount', full_name='backup_item.BackupItem.Order.refund_amount', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta_information_simple_number_1', full_name='backup_item.BackupItem.Order.meta_information_simple_number_1', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='human_is_all_too_human_coding_for_free_minds', full_name='backup_item.BackupItem.Order.human_is_all_too_human_coding_for_free_minds', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in_an_hour_of_unprecedented_heat', full_name='backup_item.BackupItem.Order.in_an_hour_of_unprecedented_heat', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i_am_part_of_that_force', full_name='backup_item.BackupItem.Order.i_am_part_of_that_force', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='backup_item.BackupItem.Order.created_at', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=515,
  serialized_end=865,
)

_BACKUPITEM_USER = _descriptor.Descriptor(
  name='User',
  full_name='backup_item.BackupItem.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='backup_item.BackupItem.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='backup_item.BackupItem.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='surname', full_name='backup_item.BackupItem.User.surname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email_address', full_name='backup_item.BackupItem.User.email_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='backup_item.BackupItem.User.phone_number', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=867,
  serialized_end=961,
)

_BACKUPITEM = _descriptor.Descriptor(
  name='BackupItem',
  full_name='backup_item.BackupItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payment_session', full_name='backup_item.BackupItem.payment_session', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='backup_item.BackupItem.order', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='backup_item.BackupItem.user', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BACKUPITEM_PAYMENTSESSION, _BACKUPITEM_ORDER, _BACKUPITEM_USER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=961,
)

_BACKUPITEM_PAYMENTSESSION.containing_type = _BACKUPITEM
_BACKUPITEM_ORDER.containing_type = _BACKUPITEM
_BACKUPITEM_USER.containing_type = _BACKUPITEM
_BACKUPITEM.fields_by_name['payment_session'].message_type = _BACKUPITEM_PAYMENTSESSION
_BACKUPITEM.fields_by_name['order'].message_type = _BACKUPITEM_ORDER
_BACKUPITEM.fields_by_name['user'].message_type = _BACKUPITEM_USER
DESCRIPTOR.message_types_by_name['BackupItem'] = _BACKUPITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BackupItem = _reflection.GeneratedProtocolMessageType('BackupItem', (_message.Message,), dict(

  PaymentSession = _reflection.GeneratedProtocolMessageType('PaymentSession', (_message.Message,), dict(
    DESCRIPTOR = _BACKUPITEM_PAYMENTSESSION,
    __module__ = 'proto_files.backup_item_pb2'
    # @@protoc_insertion_point(class_scope:backup_item.BackupItem.PaymentSession)
    ))
  ,

  Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
    DESCRIPTOR = _BACKUPITEM_ORDER,
    __module__ = 'proto_files.backup_item_pb2'
    # @@protoc_insertion_point(class_scope:backup_item.BackupItem.Order)
    ))
  ,

  User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
    DESCRIPTOR = _BACKUPITEM_USER,
    __module__ = 'proto_files.backup_item_pb2'
    # @@protoc_insertion_point(class_scope:backup_item.BackupItem.User)
    ))
  ,
  DESCRIPTOR = _BACKUPITEM,
  __module__ = 'proto_files.backup_item_pb2'
  # @@protoc_insertion_point(class_scope:backup_item.BackupItem)
  ))
_sym_db.RegisterMessage(BackupItem)
_sym_db.RegisterMessage(BackupItem.PaymentSession)
_sym_db.RegisterMessage(BackupItem.Order)
_sym_db.RegisterMessage(BackupItem.User)


# @@protoc_insertion_point(module_scope)
