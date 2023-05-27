import requests

from typing import List
from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup


class YoutubeController():
    def __init__(self) -> None:
        self.youtube_url: str
    
    def set_youtube_url(self, youtube_url) -> None:
        self.youtube_url = youtube_url
    
    def get_youtube_video_id(self) -> str:
        
        youtube_video_id: str
        
        if "www.youtube.com" in self.youtube_url and "&" in self.youtube_url:
            youtube_video_id = self.youtube_url[self.youtube_url.find("v=") + 2: self.youtube_url.find("&")]
        elif "www.youtube.com" in self.youtube_url:
            youtube_video_id = self.youtube_url[self.youtube_url.find("v=") + 2:]
        elif "youtu.be" in self.youtube_url:
            youtube_video_id = self.youtube_url[self.youtube_url.find("be/") + 3:]
        
        return youtube_video_id


    def get_korean_script(self) -> str:
        
        korean_script: str = ""
        youtube_video_id: str = self.get_youtube_video_id()
        scripts: List[dict] = YouTubeTranscriptApi.get_transcript(youtube_video_id, languages=['ko'])
        
        for script in scripts:
            korean_script += script['text'] + " "
        
        return korean_script
