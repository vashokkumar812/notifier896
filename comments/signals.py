from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import comment,post

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

import channels 

@receiver(post_save, sender=comment)
def scooter_post_update(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        print(instance.of.id)
        user_list = list(User.objects.filter(comment__pk__in=comment.objects.filter(of_id=post.objects.get(comment__pk=instance.id)).values_list('id',flat=True)).distinct().values_list('id',flat=True))
        print(user_list)
        for user_id in user_list:
            async_to_sync(channel_layer.group_send)(
            "not_" + str(user_id) , {"type": "comment.added", "by": instance.by.id}
            )