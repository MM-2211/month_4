from django.db import models

class LitnetBooksModel(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class RezkaFilmsModel(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title
