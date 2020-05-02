from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    top_name = models.CharField(max_length= 264, unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length= 264, unique=True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

# This class to make the User able to upload his website and his profile picture
# As extending the User model
class PersonProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_url = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = "profile_pics",blank = True)

    def __str__(self):
        return self.user.username