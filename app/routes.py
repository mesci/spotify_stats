from flask import Blueprint, redirect, url_for, session, request, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import current_app as app
import os

bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    sp_oauth = SpotifyOAuth(client_id=app.config['SPOTIPY_CLIENT_ID'],
                            client_secret=app.config['SPOTIPY_CLIENT_SECRET'],
                            redirect_uri=app.config['SPOTIPY_REDIRECT_URI'],
                            scope="user-top-read")

    auth_url = sp_oauth.get_authorize_url()
    return render_template('index.html', auth_url=auth_url)


@bp.route('/callback')
def callback():
    sp_oauth = SpotifyOAuth(client_id=app.config['SPOTIPY_CLIENT_ID'],
                            client_secret=app.config['SPOTIPY_CLIENT_SECRET'],
                            redirect_uri=app.config['SPOTIPY_REDIRECT_URI'],
                            scope="user-top-read")

    session.clear()
    code = request.args.get('code')
    try:
        token_info = sp_oauth.get_access_token(code)
        session["token_info"] = token_info
    except Exception as e:
        print(f"Error getting token: {e}")
        return redirect(url_for('routes.index'))

    return redirect(url_for('routes.top_items'))


@bp.route('/top_items')
def top_items():
    token_info = session.get("token_info", None)
    if not token_info:
        return redirect(url_for('routes.index'))

    sp = spotipy.Spotify(auth=token_info['access_token'])
    try:
        top_tracks = sp.current_user_top_tracks(limit=5, time_range='medium_term')
        top_artists = sp.current_user_top_artists(limit=5, time_range='medium_term')

        # Collecting genres
        genres = []
        for artist in top_artists['items']:
            genres.extend(artist['genres'])

        # Choosing the 5 most listened to genres
        from collections import Counter
        top_genres = [genre for genre, _ in Counter(genres).most_common(5)]

    except spotipy.SpotifyException as e:
        print(f"Spotify API error: {e}")
        return redirect(url_for('routes.index'))

    # Get necessary information for songs and artists
    top_tracks_info = [{
        'name': track['name'],
        'image': track['album']['images'][0]['url'],
        'url': track['external_urls']['spotify']
    } for track in top_tracks['items']]

    top_artists_info = [{
        'name': artist['name'],
        'image': artist['images'][0]['url'],
        'url': artist['external_urls']['spotify']
    } for artist in top_artists['items']]

    return render_template('top_items.html', top_tracks=top_tracks_info, top_artists=top_artists_info,
                           top_genres=top_genres)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes.index'))
