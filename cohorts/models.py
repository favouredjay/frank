from django.db import models


# Create your models here.


class Cohort(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " : " + self.description


class Native(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.DO_NOTHING)
    scvn = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.ImageField(upload_to="images/")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
