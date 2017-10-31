# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from managers.custom_managers import (
                                        StatusManager, 
                                        StatusDeletedModel, 
                                        DateTimeHandlerModel
                                    )

DELETED = 1
NOT_DELETED = 0


DELETED_STATUS = (
    (NOT_DELETED, "Not Deleted"),
    (DELETED, "Deleted"),
    )


class Posts(StatusDeletedModel, DateTimeHandlerModel, StatusManager):
    title = models.CharField(max_length=48)
    description = models.CharField(max_length=45)
    image = models.ImageField(upload_to="img/%Y/%m/%d", null=True)
    deleted = models.IntegerField(choices=DELETED_STATUS, default=NOT_DELETED)

    class Meta:
        db_table = 'posts'

    def __str__(self, *args, **kwargs):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        if self.updated_at is not None:
            self.updated_at = timezone.now()
        super(Posts, self).save(*args, **kwargs)


class Comments(StatusDeletedModel, DateTimeHandlerModel, StatusManager):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                db_column='user_id')
    post_id = models.ForeignKey('Posts', on_delete=models.CASCADE,
                                db_column='post_id')
    comment = models.CharField(max_length=200)
    deleted = models.IntegerField(choices=DELETED_STATUS, default=NOT_DELETED,
                                  db_column='deleted')

    class Meta:
        db_table = 'comments'

    def __str__(self, *args, **kwargs):
        return '{}'.format(self.comment)

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        if self.updated_at is not None:
            self.updated_at = timezone.now()
        super(Comments, self).save(*args, **kwargs)


class Likes(DateTimeHandlerModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                db_column='user_id')
    post_id = models.ForeignKey('Posts', on_delete=models.CASCADE,
                                db_column='post_id')
    reaction = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'likes'

    def __str__(self, *args, **kwargs):
        return '{}'.format(reaction)

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()
        if self.updated_at is not None:
            self.updated_at = timezone.now()
        super(Likes, self).save(*args, **kwargs)


class Alarams(DateTimeHandlerModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                db_column='user_id')
    post_id = models.ForeignKey('Posts', on_delete=models.CASCADE,
                                db_column='post_id')

    class Meta:
        db_table = 'alarams'

    def __str__(self, *args, **kwargs):
        return 'user {}, alaram enable on post {}'.format(user_id, post_id)

    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = timezone.now()
        if self.updated_at is not None:
            self.updated_at = timezone.now
        super(Save, self).save(*args, **kwargs)
