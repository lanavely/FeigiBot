from peewee import *
from data.entity import psql_db


class Peer(Model):
    """Peer database entity model"""
    vk_user_id = IntegerField(primary_key=True)
    group_number = IntegerField()

    class Meta:
        database = psql_db


Peer.create_table(safe=True)
