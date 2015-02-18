from django.db import models


class Livljpedso(models.Model):
    dbrjj = models.CharField(default='', max_length=89)
    pass


class Qpuji(models.Model):
    hpnkk = models.CharField(default='', max_length=51)
    pass


class Crzqih(models.Model):
    ttktcobp = models.CharField(default='', max_length=10)
    uanao = models.OneToOneField('joavhqi.Lfssmpr', null=True, related_name='+')
    nenil = models.ForeignKey('foijx.Qqktwujdfq', null=True, related_name='+')
    pass


class Ecgjvad(models.Model):
    dmlqug = models.CharField(default='', max_length=96)
    pass
