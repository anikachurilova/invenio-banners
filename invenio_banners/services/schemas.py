# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2023 CERN.
#
# Invenio-Banners is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Banners schema."""

from invenio_records_resources.services.records.schema import BaseRecordSchema
from marshmallow import fields


class BannerSchema(BaseRecordSchema):
    """Schema for banners."""

    message = fields.String(required=True)
    url_path = fields.String(allow_none=True)
    category = fields.String(required=True)
    start_datetime = fields.DateTime(required=True)
    end_datetime = fields.DateTime(allow_none=True)
    active = fields.Boolean(required=True)
    created = fields.DateTime(dump_only=True)
    updated = fields.DateTime(dump_only=True)
