from django.db import models
from gsheets import mixins
from uuid import uuid4


class Data(mixins.SheetPullableMixin, models.Model):
    spreadsheet_id = '13UcX2Wf021V3RW_E4AkzSv2jvHhe0YorK0-H5ckhzso'
    model_id_field = 'guid'
    guid = models.CharField(primary_key=True, max_length=255, default=uuid4)
    order = models.CharField(max_length=20, default='')
    price = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    date = models.DateField()
    price_rub = models.DecimalField(max_digits=10, decimal_places=1, default=0)



