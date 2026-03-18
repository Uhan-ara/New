from youtube_fetcher import fetch_youtube_videos

def recommend_videos(user_input):
    
    query = user_input + " full course lecture tutorial"
    
    videos = fetch_youtube_videos(query)

    return videos[:5]