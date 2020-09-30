from django.db import models

# Base Address Model


class AbstractAddress(models.Model):

    line_1 = models.CharField(max_length=200)
    line_2 = models.CharField(max_length=200, default="", blank=True)
    barangay = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=4)

    class Meta:
        abstract = True

    def __str__(self):
        full_address = self.line_1
        full_address += f", {self.line_2}" if len(self.line_2) > 0 else ""
        full_address += f", {self.barangay}, {self.city}, {self.province} {self.zip_code}"
        return full_address
