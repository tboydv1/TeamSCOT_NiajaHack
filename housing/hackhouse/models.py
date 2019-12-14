from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
# Here, we created a model class with its attributes
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Here, we created a method to know post time.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #
    def __str__(self):
        return self.title