from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserEmotionFillForm, AudioContentForm, VideoContentForm
from .models import AudioContent, VideoContent
import requests

# Emotion to content type mapping
content_emotion_map = {
    "happy": ["quizzes", "stories", "music", "challenges", "goal_setting_tools", "hype_playlists"],
    "sad": ["comfort_videos", "motivational_talks", "calming_music", "breakup_talks", "emotional_songs", "relatable_stories"],
    "angry": ["venting_games", "stress_relief_tips", "motivational_talks", "hype_playlists"],
    "relaxed": ["calming_music", "meditation_guides", "soothing_podcasts", "affirmations", "minimalist_tools", "focus_timers"],
    "excited": ["interactive_tools", "trending_content", "puzzles", "challenges", "goal_setting_tools"],
    "bored": ["quizzes", "trending_content", "interactive_tools", "puzzles", "short_reads"],
    "anxious": ["calming_music", "soothing_podcasts", "affirmations", "stress_relief_tips", "meditation_guides"],
    "overwhelmed": ["focus_timers", "minimalist_tools", "meditation_guides", "soothing_podcasts", "affirmations"],
    "in_love": ["romantic_stories", "love_songs", "couple_challenges", "stories"],
    "confident": ["goal_setting_tools", "motivational_talks", "challenges", "knowledge_content", "affirmations"],
    "heartbroken": ["breakup_talks", "emotional_songs", "relatable_stories", "comfort_videos", "venting_games"],
    "curious": ["how_to_videos", "documentaries", "knowledge_content", "short_reads", "puzzles"]
}

def gemini_response(string):
    prompt_text = f"""
    You are an AI support assistant.

    Message: "{string}"

    From the following list, choose the **one** content type that best matches the emotion or mood expressed in the message:

    quizzes, stories, music, comfort_videos, motivational_talks, calming_music, venting_games,
    stress_relief_tips, meditation_guides, soothing_podcasts, affirmations, interactive_tools,
    trending_content, puzzles, minimalist_tools, short_reads, focus_timers, romantic_stories,
    love_songs, couple_challenges, challenges, goal_setting_tools, hype_playlists, breakup_talks,
    emotional_songs, relatable_stories, how_to_videos, documentaries, knowledge_content

    Respond with only the category name. Nothing else.
    """

    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyAPYlnVU3g3xwyUKI3XaVXj3h9gqLfAxvA'
    headers = {'Content-Type': 'application/json'}
    data = {'contents': [{'parts': [{'text': prompt_text}]}]}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        try:
            text = response.json()['candidates'][0]['content']['parts'][0]['text'].strip()
            print(text)
            print("Full Gemini reply:\n", text)
            return text.split()[0].strip().lower()
        except Exception as e:
            return 'happy'
    else:
        return 'happy'


@login_required
def update_user_emotion(request):
    if request.method == 'POST':
        form = UserEmotionFillForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('content') 
    else:
        form = UserEmotionFillForm(instance=request.user)
    return render(request, 'content/emotion.html', {'form': form})


@login_required
def upload_audio_view(request):
    if request.method == 'POST':
        form = AudioContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.uploaded_by = request.user
            content.emotion = gemini_response(content.disc)
            content.save()
            return redirect('view_audio_content')
    else:
        form = AudioContentForm()
    return render(request, 'content/upload.html', {'form': form})


@login_required
def upload_video_view(request):
    if request.method == 'POST':
        form = VideoContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.uploaded_by = request.user
            content.emotion = gemini_response(content.disc)
            content.save()
            return redirect('view_video_content')
    else:
        form = VideoContentForm()
    return render(request, 'content/upload.html', {'form': form})


@login_required
def view_audio_content(request):
    user_emotion = request.user.emotion
    matching_emotions = content_emotion_map.get(user_emotion, [])
    audios = AudioContent.objects.filter(emotion__in=matching_emotions)
    return render(request, 'content/audio_list.html', {'audios': audios})


@login_required
def view_video_content(request):
    user_emotion = request.user.emotion
    matching_emotions = content_emotion_map.get(user_emotion, [])
    videos = VideoContent.objects.filter(emotion__in=matching_emotions)
    return render(request, 'content/video_list.html', {'videos': videos})



@login_required
def content_view(request):
    return render(request, 'content/content.html')