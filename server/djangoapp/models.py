from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    # Toyota Models
    TOYOTA_CAMRY = 'toyota_camry'
    TOYOTA_COROLLA = 'toyota_corolla'
    TOYOTA_RAV4 = 'toyota_rav4'
    TOYOTA_PRIUS = 'toyota_prius'
    TOYOTA_HIGHLANDER = 'toyota_highlander'

    # Tesla Models
    TESLA_MODEL_S = 'tesla_model_s'
    TESLA_MODEL_3 = 'tesla_model_3'
    TESLA_MODEL_X = 'tesla_model_x'
    TESLA_MODEL_Y = 'tesla_model_y'

    # Audi Models
    AUDI_A4 = 'audi_a4'
    AUDI_A6 = 'audi_a6'
    AUDI_Q5 = 'audi_q5'
    AUDI_Q7 = 'audi_q7'
    AUDI_A3 = 'audi_a3'

    CAR_MODEL_CHOICES = [
        (TOYOTA_CAMRY, 'Toyota Camry'),
        (TOYOTA_COROLLA, 'Toyota Corolla'),
        (TOYOTA_RAV4, 'Toyota RAV4'),
        (TOYOTA_PRIUS, 'Toyota Prius'),
        (TOYOTA_HIGHLANDER, 'Toyota Highlander'),
        (TESLA_MODEL_S, 'Tesla Model S'),
        (TESLA_MODEL_3, 'Tesla Model 3'),
        (TESLA_MODEL_X, 'Tesla Model X'),
        (TESLA_MODEL_Y, 'Tesla Model Y'),
        (AUDI_A4, 'Audi A4'),
        (AUDI_A6, 'Audi A6'),
        (AUDI_Q5, 'Audi Q5'),
        (AUDI_Q7, 'Audi Q7'),
        (AUDI_A3, 'Audi A3'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(default=1,primary_key=True)
    name = models.CharField(null=False, max_length=100, default='Car')
    car_type = models.CharField(
        null=False,
        max_length=20,
        choices=CAR_MODEL_CHOICES,
        default=TESLA_MODEL_3
    )
    year = models.DateField(default=now)



    def __str__(self):
        return "Name: " + self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
