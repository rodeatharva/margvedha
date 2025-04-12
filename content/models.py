from django.db import models
from users.models import CustomUser
from django.core.exceptions import ValidationError
import os


def audio_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3', '.wav', '.aac']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported audio file format.')

def video_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.avi', '.mov']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported video file format.')


content_emotion_dict = {
    "quizzes": "quizzes",
    "stories": "stories",
    "music": "music",
    "comfort_videos": "comfort_videos",
    "motivational_talks": "motivational_talks",
    "calming_music": "calming_music",
    "venting_games": "venting_games",
    "stress_relief_tips": "stress_relief_tips",
    "meditation_guides": "meditation_guides",
    "soothing_podcasts": "soothing_podcasts",
    "affirmations": "affirmations",
    "interactive_tools": "interactive_tools",
    "trending_content": "trending_content",
    "puzzles": "puzzles",
    "minimalist_tools": "minimalist_tools",
    "short_reads": "short_reads",
    "focus_timers": "focus_timers",
    "romantic_stories": "romantic_stories",
    "love_songs": "love_songs",
    "couple_challenges": "couple_challenges",
    "challenges": "challenges",
    "goal_setting_tools": "goal_setting_tools",
    "hype_playlists": "hype_playlists",
    "breakup_talks": "breakup_talks",
    "emotional_songs": "emotional_songs",
    "relatable_stories": "relatable_stories",
    "how_to_videos": "how_to_videos",
    "documentaries": "documentaries",
    "knowledge_content": "knowledge_content"
}


class AudioContent(models.Model):
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='audiofiles', validators=[audio_validator])
    disc = models.TextField(max_length=200)
    emotion = models.CharField(max_length=50, choices=content_emotion_dict, default='happy')

    def __str__(self):
        return self.disc
    

class VideoContent(models.Model):
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videofiles', validators=[video_validator])
    disc = models.TextField(max_length=200)
    emotion = models.CharField(max_length=50, choices=content_emotion_dict, default='happy')

    def __str__(self):
        return self.disc
    