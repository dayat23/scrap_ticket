from django.db import models


# Create your models here.
class SiteScraping(models.Model):
    SITE_CHOICES = (
        ('1', 'www.traveloka.com'),
        ('2', 'www.tiket.com'),
    )

    PERIODICITY_CHOICES = (
        ('O', 'ONCE'),
        ('D', 'DAILY'),
        ('W', 'WEEKLY'),
        ('M', 'MONTHLY')
    )

    scraping_site = models.CharField(max_length=50, choices=SITE_CHOICES, db_index=True)
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOICES, default='D')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.scraping_site
