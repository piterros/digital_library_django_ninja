from django.db import models


class DigitalLibraryModel(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    finish_date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True


class Games(DigitalLibraryModel):
    platform = models.CharField(max_length=50, blank=False, null=False)
    purchase_date = models.DateField(blank=True, null=True)


class Books(DigitalLibraryModel):
    author = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=50, blank=False, null=False)
    purchase_date = models.DateField(blank=True, null=True)


class Videos(DigitalLibraryModel):
    type = models.CharField(max_length=50, blank=False, null=False)
