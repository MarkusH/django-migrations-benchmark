from django.db import models


class Livljpedso(models.Model):
    dbrjj = models.CharField(default='', max_length=89)
    pass


class Qpuji(models.Model):
    dgyoob = models.CharField(default='', max_length=155)
    pass


class Ecgjvad(models.Model):
    mkqcu = models.IntegerField(default=0)
    pass


class Ckree(models.Model):
    yqfsn = models.OneToOneField('glcmkwkzv.Fbytmhf', null=True, related_name='+')
    pass
