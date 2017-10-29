#-------------------------------------------------------------------------------
# Name:        models.py
# Purpose:     subclass django.db.models.DateTimeFields to make them auto-update
# Usage:       class ModelName(models.Model):
#                  date_created = AutoNewDateTimeField(blank=True)
#                  date_updated = AutoDateTimeField(blank=True)
#
# Author:      James Marlowe
#
# Created:     10/25/2013
# Copyright:   (c) James Marlowe
# Licence:     MIT
#-------------------------------------------------------------------------------

from django.db.models import DateTimeField
from datetime import datetime
from django.conf import settings
from django.utils import timezone


class AutoDateTimeField(DateTimeField):
    def pre_save(self, model_instance, add):
        if settings.USE_TZ:
            now = timezone.now()
        else:
            now = datetime.now()
        setattr(model_instance, self.attname, now)
        return now


class AutoNewDateTimeField(DateTimeField):
    def pre_save(self, model_instance, add):
        if not add:
            return getattr(model_instance, self.attname)
        if settings.USE_TZ:
            now = timezone.now()
        else:
            now = datetime.now()
        setattr(model_instance, self.attname, now)
        return now
