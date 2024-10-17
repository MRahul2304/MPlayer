# Music Player Web Application 🎵

This project is a **Music Player Web Application** built using **Django**, **Django REST Framework**, and **Bootstrap**. It allows users to upload songs with metadata like title, artist, album, and duration, and play the uploaded songs directly in the web interface.

## Features ✨

- **User Authentication:** Users can register, login, and upload songs.
- **Song Management:** Users can upload songs with metadata such as title, artist, album, and duration.
- **Song Search:** Allows users to search for uploaded songs by name.
- **Audio Player:** Users can play songs directly within the web application.
- **Responsive Design:** The UI is built using Bootstrap, making it responsive across devices.

## Technologies Used 🛠️

- **Backend:**
  - Django 5.0
  - Django REST Framework
  - MySQL (for production, SQLite for development)
  
- **Frontend:**
  - HTML/CSS (Bootstrap)
  - JavaScript (Fetch API for file uploads)
  
- **Other:**
  - `mysqlclient` for MySQL integration
  - CSRF protection for secure forms

## Requirements 📝

- Python 3.10+
- Django 5.0+
- MySQL
- Bootstrap (linked via CDN)

## Setup Instructions ⚙️

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/music-player-webapp.git
cd music-player-webapp
```

### 2. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### MySQL Setup

Make sure you have MySQL running and a database created. Configure your database settings in `settings.py` under the `DATABASES` section. Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MPlayer',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': 'your_port_number',
    }
}
```

#### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Start the Server

```bash
python manage.py runserver
```

Now, navigate to `http://127.0.0.1:8000/` in your web browser to see the application in action.

## Usage 🖥️

### Uploading Songs

1. Register or login to the system.
2. Navigate to the **Add Song** page.
3. Fill in the form with the song’s details (Title, Artist, Album, Duration) and upload the audio file.
4. Submit the form and you'll be redirected to the home page.

### Playing Songs

- All uploaded songs can be played from the home page or searched for using the song's title.

## API Endpoints (for development) 🌐

- **List Songs:** `GET /api/songs/`
- **Create Song:** `POST /api/songs/`
  
When uploading via API, the payload should include the song metadata and the song file (Multipart form).

### Example API Request

```bash
curl -X POST http://127.0.0.1:8000/api/songs/ -F "title=My Song" -F "artist=My Artist" -F "album=My Album" -F "duration=00:03:45" -F "file=@/path/to/song.mp3"
```

## File Structure 📁

The core project structure looks like this:

```
music_player_project/
│
├── music_player_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── music_player_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── AddSong.html
│   │   └── ...
│   └── ...
│
├── media/              # Stores uploaded song files
├── manage.py
└── requirements.txt
```

## Known Issues 🐛

- If the song is not showing up after upload, check the database and ensure the media files are being saved correctly.
- Ensure the correct `CSRF` token is included in the form during file uploads.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
