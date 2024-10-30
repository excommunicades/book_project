from django.db import models


class Books(models.Model):

    """Class create books model for db"""

    title = models.CharField(
                    max_length=30,
                    unique=True,
                    blank=False,
                    null=False,
                    )
    description = models.TextField()

    class Meta:
        
        verbose_name = "Book"
        verbose_name_plural = "Books"
