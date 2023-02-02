# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 CERN.
#
# Invenio-Banners is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio administration banners view module."""
from datetime import datetime

from flask_babelex import lazy_gettext as _
from invenio_administration.views.base import (
    AdminResourceCreateView,
    AdminResourceDetailView,
    AdminResourceEditView,
    AdminResourceListView,
)


class BannerListView(AdminResourceListView):
    """Search admin view."""

    api_endpoint = "/banners"
    name = "banners"
    resource_config = "banners_resource"
    search_request_headers = {"Accept": "application/json"}
    title = "Banners"
    menu_label = "Banners"
    category = "Banners"
    pid_path = "id"
    icon = "newspaper"
    template = "invenio_banners/administration/banner_search.html"

    display_search = True
    display_delete = True
    display_create = True
    display_edit = True

    item_field_list = {
        "message": {"text": _("Message"), "order": 1},
        "url_path": {"text": _("URL path"), "order": 2},
        "category": {"text": _("Category"), "order": 3},
        "start_datetime": {"text": _("Start DateTime"), "order": 4},
        "end_datetime": {"text": _("End DateTime"), "order": 5},
        "created": {"text": _("Created"), "order": 6},
        "active": {"text": _("Active"), "order": 7},
    }

    create_view_name = "banner_create"

    search_config_name = "BANNERS_SEARCH"
    search_facets_config_name = "BANNERS_FACETS"
    search_sort_config_name = "BANNERS_SORT_OPTIONS"


class BannerEditView(AdminResourceEditView):
    """Configuration for Banner edit view."""

    name = "banner_edit"
    url = "/banners/<pid_value>/edit"
    resource_config = "banners_resource"
    pid_path = "id"
    api_endpoint = "/banners"
    title = "Edit Banner"

    list_view_name = "banners"

    form_fields = {
        "category": {
            "order": 1,
            "text": _("Category"),
            "description": _("Banner category."),
            "options": [
                {"title_l10n": "Info", "id": "info"},
                {"title_l10n": "Warning", "id": "warning"},
                {"title_l10n": "Other", "id": "other"},
            ],
        },
        "message": {
            "order": 2,
            "text": _("Message"),
            "description": _("Message to be displayed on the banner."),
        },
        "url_path": {
            "order": 3,
            "text": _("URL path"),
            "description": _(
                "Enter the URL path (including the first /) to define in "
                "which part of the site the message will be active. For "
                "example, if you enter `/records`, any URL starting with "
                "`/records` will return an active banner (/records, "
                "/records/1234, etc...). Empty value will make the banner "
                "active for any URL."
            ),
        },
        "active": {
            "order": 4,
            "text": _("Active"),
            "description": _("Set to true to display a banner, false - to disable."),
            "trueLabel": "True",
            "falseLabel": "False",
        },
        "start_datetime": {
            "order": 5,
            "text": _("Start DateTime"),
            "description": _(
                "DateTime input format: yyyy-mm-dd hh:mm:ss."
                "Set to current or future date/time to delay the banner."
            ),
            "placeholder": _("YYYY-MM-DD hh:mm:ss"),
        },
        "end_datetime": {
            "order": 6,
            "text": _("End DateTime"),
            "description": _(
                "DateTime input format: yyyy-mm-dd hh:mm:ss. Date/time "
                "to make the banner inactive. Empty value will make "
                "the banner active until manually disabled via the active flag."
            ),
            "placeholder": _("YYYY-MM-DD hh:mm:ss"),
        },
        "created": {"order": 7},
        "updated": {"order": 8},
    }


class BannerCreateView(AdminResourceCreateView):
    """Configuration for Banner create view."""

    name = "banner_create"
    url = "/banners/create"
    resource_config = "banners_resource"
    pid_path = "id"
    api_endpoint = "/banners/new"
    title = "Create Banner"

    list_view_name = "banners"

    form_fields = {
        "category": {
            "order": 1,
            "text": _("Category"),
            "description": _("Banner category."),
            "options": [
                {"title_l10n": "Info", "id": "info"},
                {"title_l10n": "Warning", "id": "warning"},
                {"title_l10n": "Other", "id": "other"},
            ],
            "placeholder": "Info",
        },
        "url_path": {
            "order": 2,
            "text": _("URL path"),
            "description": _(
                "Enter the URL path (including the first /) to define in "
                "which part of the site the message will be active. For "
                "example, if you enter `/records`, any URL starting with "
                "`/records` will return an active banner (/records, "
                "/records/1234, etc...). Empty value will make the banner "
                "active for any URL."
            ),
        },
        "message": {
            "order": 3,
            "text": _("Message"),
            "description": _("Message to be displayed on the banner."),
        },
        "active": {
            "order": 4,
            "text": _("Active"),
            "description": _("Set to true to display a banner, false - to disable."),
            "trueLabel": "True",
            "falseLabel": "False",
        },
        "start_datetime": {
            "order": 5,
            "text": _("Start DateTime"),
            "description": _(
                "DateTime input format: yyyy-mm-dd hh:mm:ss."
                "Set to current or future date/time to delay the banner."
            ),
            "placeholder": _("YYYY-MM-DD hh:mm:ss"),
            "defaultValue": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        },
        "end_datetime": {
            "order": 6,
            "text": _("End DateTime"),
            "description": _(
                "DateTime input format: yyyy-mm-dd hh:mm:ss. Date/time "
                "to make the banner inactive. Empty value will make "
                "the banner active until manually disabled via the active flag."
            ),
            "placeholder": _("YYYY-MM-DD hh:mm:ss"),
        },
    }


class BannerDetailView(AdminResourceDetailView):
    """Admin banner detail view."""

    url = "/banners/<pid_value>"
    api_endpoint = "/banners"
    name = "banner-details"
    resource_config = "banners_resource"
    title = "Banner Details"

    template = "invenio_banners/administration/banner_details.html"

    display_delete = True
    display_edit = True

    list_view_name = "banners"
    pid_path = "id"
    request_headers = {"Accept": "application/json"}

    item_field_list = {
        "message": {"text": _("Message"), "order": 1},
        "url_path": {"text": _("URL path"), "order": 2},
        "category": {"text": _("Category"), "order": 3},
        "start_datetime": {"text": _("Start DateTime"), "order": 4},
        "end_datetime": {"text": _("End DateTime"), "order": 5},
        "active": {"text": _("Active"), "order": 6},
        "created": {"text": _("Created"), "order": 7},
        "updated": {"text": _("Updated"), "order": 8},
    }
