from django.db import models


class Sehvi(models.Model):
    wspsk = models.OneToOneField('foijx.Wrafoshzom', null=True, related_name='+')
    pass


class Kmwzcb(models.Model):
    zahlcf = models.IntegerField(default=0)
    pass
