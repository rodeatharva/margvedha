from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    EMOTION_CHOICES_DICT = {
        "happy": "happy",
        "sad": "sad",
        "angry": "angry",
        "relaxed": "relaxed",
        "excited": "excited",
        "bored": "bored",
        "anxious": "anxious",
        "overwhelmed": "overwhelmed",
        "in_love": "in_love",
        "confident": "confident",
        "heartbroken": "heartbroken",
        "curious": "curious"
    }
    GENDER = {
        'male' : 'male',
        'female' : 'female', 
        'other' : 'other',
        'prefer-not-to-say' : 'prefer-not-to-say',
    }

    emotion = models.CharField(max_length=20, choices=EMOTION_CHOICES_DICT, default='happy')
    phone_number = models.IntegerField(blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='prefer-not-to-say')
    terms_agree = models.BooleanField(default=False)
