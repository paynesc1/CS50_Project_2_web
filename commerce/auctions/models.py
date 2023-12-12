from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing():
    listing_title = models.CharField(max_length=64)
    listing_description = models.TextField()
    starting_bid = models.CharField()
    # listing_category =
    # listing_image =

# class Bid():
    

# class Comment():



#one for auction listings, one for bids, and one for comments