from django.db import models

# Create your models here.

class Trade(models.Model):
    id = models.IntField(pk=True)
    trader = fields.ForeignKeyField('models.Trader', 'trades')
    side = fields.IntEnumField(enum_type=TradeSide)
    tez_qty = fields.DecimalField(decimal_places=6, max_digits=16)
    token_qty = fields.DecimalField(decimal_places=18, max_digits=32)
    price = fields.DecimalField(decimal_places=6, max_digits=32)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()