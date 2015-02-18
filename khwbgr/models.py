from django.db import models


class Ibuazau(models.Model):
    pssnb = models.OneToOneField('bniworfy.Trjyk', null=True, related_name='+')
    pass
