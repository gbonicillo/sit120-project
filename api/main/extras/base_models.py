from django.db import models

# Base Address Model


class AbstractAddress(models.Model):

    line_1 = models.CharField(max_length=200, null=False)
    line_2 = models.CharField(max_length=200)
    barangay = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    province = models.CharField(max_length=200, null=False)
    zip_code = models.CharField(max_length=4, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        full_address = self.line_1
        full_address += "" if self.line_2 is None else f", {self.line_2}"
        full_address += f", {self.barrangay}, {self.city}, {self.province} {self.zip_code}"
        return full_address
