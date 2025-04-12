from django import forms
from users.models import CustomUser
from . models import AudioContent, VideoContent

class UserEmotionFillForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['emotion']


class AudioContentForm(forms.ModelForm):
    class Meta:
        model = AudioContent
        fields = ['file', 'disc']


    
class VideoContentForm(forms.ModelForm):
    class Meta:
        model = VideoContent
        fields = ['file', 'disc']

