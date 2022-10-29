import crispy_forms.layout
from django.db import models
from django import forms
import uuid
from autoslug import AutoSlugField
# Create your models here.
from django_json_field_schema_validator.validators import JSONFieldSchemaValidator

class roles(models.Model):
    roleName = models.CharField(max_length=20)

class logIn(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=20)

class signUp(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    userName = models.CharField(max_length=50,default=None)
    email = models.EmailField(max_length=70,default=None)
    password = models.CharField(max_length=200)
    userRoll = models.CharField(max_length=20,default=None)

class setFile(models.Model):
    jpg_image = models.ImageField()
    png_image = models.ImageField(max_length=100)
    audio = models.FileField(max_length=100)
    video = models.FileField(max_length=100)
    pdf = models.FileField(max_length=100)
    text = models.FileField(max_length=100)
    doc = models.FileField(max_length=100)
    html = models.FileField(max_length=100)
    css = models.FileField(max_length=100)
    java = models.FileField(max_length=100)
    psd = models.FileField(max_length=100)

class singleImage(models.Model):
    imgname = models.CharField(max_length=150)
    myImg = models.ImageField()


class setField(models.Model):
    Colour_Sample = [
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('green', 'Green'),
    ]

    dropdown = models.CharField(max_length=100,choices=Colour_Sample,default='blue')
    choice = models.CharField(max_length=100)
    multichoice = models.CharField(max_length=100)
    characterField = models.CharField(max_length=100)
    textField = models.TextField(max_length=100)
    intField = models.IntegerField()
    dateField = models.DateField()
    timeField = models.TimeField()
    datetimeField = models.DateField()
    decimalField = models.DecimalField(max_digits=20,decimal_places=2)
    emailField = models.EmailField("Enter Email")
    floatField = models.FloatField()
    positiveintField = models.PositiveIntegerField()
    positivebigintField = models.PositiveBigIntegerField()
    positivesmallintField = models.PositiveSmallIntegerField()
    smallintField = models.SmallIntegerField()
    bigintField = models.BigIntegerField()
    uuidField = models.UUIDField(primary_key=False,default=uuid.uuid4,editable=True)
    durationField = models.DurationField()
    jsonField = models.JSONField(null=True,validators=[JSONFieldSchemaValidator])
    slugField = models.SlugField()
    urlField = models.URLField()
    genericipaddrsField = models.GenericIPAddressField()
    image = models.ImageField()
    autoslugField = AutoSlugField(populate_from='characterField',default=None,unique=True)
    binaryField = models.BinaryField(default=1)
    passwordField = models.TextField(default=None)
    '''
    filepathField = models.FilePathField(path="/", max_length=100)
    smallautoField = models.SmallAutoField()
    autoField = models.AutoField()
    bigautoField = models.BigAutoField()
    rowRangeField = models.RowRange()
    valueRangedField = models.RowRange()
    '''



