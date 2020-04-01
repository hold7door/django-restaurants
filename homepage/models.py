from django.db import models

# Create your models here.

class Restaurant(models.Model):
    RestaurantId = models.IntegerField(db_column = 'Restaurant ID', primary_key=True)
    RestaurantName= models.CharField(db_column = 'Restaurant Name', max_length=250)
    Cuisines = models.CharField(max_length=350, blank=True)
    AverageCostForTwo = models.IntegerField(db_column = 'Average Cost for two', blank=True)
    Currency = models.CharField(max_length=100, blank = True)
    HasTableBooking = models.CharField(db_column = 'Has Table booking', max_length=10, blank=True)
    HasOnlineDelivery = models.CharField(db_column = 'Has Online delivery', max_length=10, blank=True)
    AggregateRating = models.FloatField(db_column = 'Aggregate rating', blank=True)
    RatingColor = models.CharField(db_column = 'Rating color', max_length=50, blank=True)
    RatingText = models.CharField(db_column = 'Rating text', max_length=50, blank=True)
    Votes = models.IntegerField(blank=True)

