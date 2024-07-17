
# Spotify Stats
Through this application, after logging in with your Spotify account, you can see the 5 songs, 5 artists and 5 genres you have listened to most in the medium term.
## Installation

#### 1️⃣ Download the code and open it in your editor.
1.1 Create an APP on [Spotify Developers Dashboard](https://developer.spotify.com/dashboard/).

1.2 Type ```http://localhost:5001/callback``` in the Redirect URIs input, you can edit it according to the port you are running the application on.

1.3 Select Web API and create the application.

1.4 Save the ```Client ID``` and ```Client Secret``` you will get after creating the application.

#### 2️⃣ Edit the following sections in the ```config.py``` file.



```bash 
SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID') or 'write_your_client_id_here'
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET') or 'write_your_client_secret_here'
```
```write_your_clien_id_here``` — Enter your Client ID here.

```write_your_client_secret_here``` — Enter your Client Secret here.

#### 3️⃣ Create virtual environment.
Navigate to the directory where you want to create the virtual environment.

Windows:
```bash
python -m venv myenv
myenv\Scripts\activate
```
Mac and Linux:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

#### 4️⃣ Install the libraries.
```bash
pip install Flask
pip install Flask-Session
pip install spotipy
```

#### 5️⃣ Run the project.
```bash
python run.py
```
## Feedback

📨 If you have any feedback, please reach out to:
```bash 
mail(@)mesci.dev
```