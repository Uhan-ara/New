from youtubesearchpython import VideosSearch

def fetch_youtube_videos(query):
    videosSearch = VideosSearch(query, limit=10)
    results = videosSearch.result()["result"]

    videos = []

    for v in results:
        title = v["title"]
        link = v["link"]

        # Filter out shorts & irrelevant content
        if "shorts" not in link.lower():
            videos.append((title, link))

    return videos