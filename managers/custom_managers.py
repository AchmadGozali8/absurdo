# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

DELETED = 1
NOT_DELETED = 0


class StatusManager(models.Manager):
    # custom models queryset

    def get_queryset(self):
        return super(StatusManager, self).get_queryset().\
            filter(deleted=NOT_DELETED)


class StatusDeletedModel(models.Model):
    # change default Manager name
    # default (objects) to (status)
    # Before: data.objects.all() -> for query all data on DB
    # After: data.status.all() -> for query all data on DB but,
    # filter by status, like class above
    # it's why we use StatusManager class as value in variable below
    status = StatusManager()
    # below, we will keep default manager, so if sometimes we don't want use
    # custom manager, we can still using default
    objects = models.Manager()

    class Meta:
        # Abstract base classes are useful when you want to put some common
        # information into a number of other models
        abstract = True


class DateTimeHandlerModel(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
