from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Meet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=40)


class EventResult(models.Model):
    meet_id = models.ForeignKey(Meet, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    results_context = models.TextField(null=True, blank=True)

    @property
    def slug(self):
        return slugify(self.event_name)
