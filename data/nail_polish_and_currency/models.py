from django.db import models


class Types_nail_polish(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return f'{self.name}'


class Variant_nail_polish(models.Model):

    types = models.ForeignKey(Types_nail_polish, on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=150, blank=False)
    expiration_date = models.DateField()


    def __str__(self):
        return f'{self.name} {self.expiration_date}'
