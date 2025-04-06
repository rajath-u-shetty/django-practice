from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class variety(models.Model):
    CHAI_TYPE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('MN','MINT'),
        ('LM','LEMON'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai/') # install Pillow for image storage
    dob = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE)

    def __str__(self):
        return self.name


# One-to-many

class ChaiReview(models.Model):
    chai = models.ForeignKey(variety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'

# Many-to-many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(variety, related_name='stores')

    def __str__(self):
        return self.name
    
# One-to-one
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(variety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'