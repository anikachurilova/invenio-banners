# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2023 CERN.
#
# Invenio-Banners is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Configuration variables."""

from flask_babelex import lazy_gettext as _

from invenio_banners.utils import style_category

BANNERS_CATEGORIES = [
    ("info", "Info"),
    ("warning", "Warning"),
    ("other", "Other"),
]
"""Categories to define different types of messages. List of (id, label)."""

BANNERS_CATEGORIES_TO_STYLE = style_category
"""Function to transform the banner category to a specific Semantic-UI class."""

BANNERS_SEARCH = {
    "facets": [],
    "sort": [
        "message",
        "url_path",
        "category",
        "active",
        "start_datetime",
        "end_datetime",
        "created",
        "updated",
    ],
}
"""Banner search configuration (i.e list of banners)"""

BANNERS_FACETS = {}

BANNERS_SORT_OPTIONS = {
    "message": dict(
        title=_("Message"),
        fields=["message"],
    ),
    "url_path": dict(
        title=_("URL path"),
        fields=["url_path"],
    ),
    "category": dict(
        title=_("Category"),
        fields=["category"],
    ),
    "active": dict(
        title=_("Active"),
        fields=["active"],
    ),
    "start_datetime": dict(
        title=_("Start DateTime"),
        fields=["start_datetime"],
    ),
    "end_datetime": dict(
        title=_("End DateTime"),
        fields=["end_datetime"],
    ),
    "created": dict(
        title=_("Created"),
        fields=["created"],
    ),
    "updated": dict(
        title=_("Updated"),
        fields=["updated"],
    ),
}
"""Definitions of available Banners sort options. """
