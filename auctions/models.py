from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


#Auction Listings Model
class Listing(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    strating_price = models.IntegerField(null=True)
    current_bid = models.IntegerField(null=True)
    seller = models.CharField(max_length=64, default="Default_Value")
    category = models.CharField(max_length=64)
    image_link = models.CharField(max_length=200, default=None, blank=True, null=True)
    winner = models.CharField(max_length=80, default="Default_value")

    def __str__(self):
        return self.title

#Bids Model
#class Bid(models.Model):


#Comments Model
#class Comment(models.Model):


#Watchlist Model
class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    listing_id = models.IntegerField()