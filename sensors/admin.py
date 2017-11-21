# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MicroSensor,MacroSensor,Plant

admin.site.register(Plant)
admin.site.register(MacroSensor)
admin.site.register(MicroSensor)

