from peewee import *
from data.entity import psql_db


class Peer(Model):
    """Peer database entity model"""
    vk_user_id = IntegerField(primary_key=True)
    group_number = IntegerField()

    class Meta:
        database = psql_db


class SavedMassagesInText(Model):
    peer_id = IntegerField()
    hashtag = CharField(100)
    message_id = IntegerField()
    author_id = IntegerField()
    text = TextField()

    class Meta:
        database = psql_db
        primary_key = CompositeKey('peer_id', 'hashtag')


class Attachments(Model):
    peer_id = IntegerField()
    hashtag = CharField(100)
    attachment = CharField(255)

    class Meta:
        database = psql_db


Peer.create_table(safe=True)
SavedMassagesInText.create_table(safe=True)
# Attachments.create_table(safe=True)