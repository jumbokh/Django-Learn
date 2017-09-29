# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sign.models import Event, Guest

# Register your models here.
admin.site.register(Event)
admin.site.register(Guest)
