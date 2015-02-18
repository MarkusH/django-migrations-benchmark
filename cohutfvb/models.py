from django.db import models


class Livljpedso(models.Model):
    dbrjj = models.CharField(default='', max_length=89)
    pass


class Qpuji(models.Model):
    dgyoob = models.CharField(default='', max_length=155)
    pass


class Ecgjvad(models.Model):
    xoyasniyf = models.OneToOneField('kakry.Xgsseizbpr', null=True, related_name='+')
    pass
