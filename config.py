import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_super_secret_key'
    SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID') or 'write_your_clien_id_here'
    SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET') or 'write_your_client_secret_here'
    SPOTIPY_REDIRECT_URI = 'http://localhost:5001/callback'
    SESSION_COOKIE_NAME = 'spotify-login-session'
    SESSION_TYPE = 'filesystem'
