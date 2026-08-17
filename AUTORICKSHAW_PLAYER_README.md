# 🚐 Autorickshaw Ki Duniya - Mumbai Music Player

A nostalgic, retro-styled web application inspired by [deluxesalon.org](https://deluxesalon.org/), celebrating the iconic music of Mumbai's autorickshaws (tuk-tuks). This webapp recreates the authentic experience of riding through Mumbai's bustling streets while listening to classic Bollywood hits.

## 🎵 Features

✨ **Authentic Mumbai Vibes**
- Colorful, retro design inspired by Mumbai's iconic three-wheelers
- Decorative striped header and footer (classic autorickshaw aesthetic)
- Nostalgic UI with glowing effects and smooth animations

🎶 **Complete Music Player**
- Play/Pause controls
- Next/Previous song navigation
- Progress bar with time display
- Volume control (0-100%)
- Dynamic playlist with 12+ classic Bollywood songs
- Keyboard shortcuts (Space=Play/Pause, ← →=Previous/Next)

🎨 **Curated Playlist**
- Classic Bollywood songs commonly heard in Mumbai autorickshaws
- Artists: Mukesh, Lata Mangeshkar, Mohammed Rafi, A.R. Rahman, and more
- Mix of vintage classics and modern retro hits
- Song duration and genre information

📱 **Fully Responsive**
- Desktop, tablet, and mobile optimized
- Touch-friendly controls
- Adaptive grid layout for playlist

## 🚀 Quick Start

### Option 1: Open Directly in Browser
Simply download and open one of these files in any modern web browser:
- **`autorickshaw-player.html`** - Basic version (lightweight)
- **`autorickshaw-player-advanced.html`** - Enhanced version (recommended)

```bash
# On macOS
open autorickshaw-player-advanced.html

# On Linux
firefox autorickshaw-player-advanced.html

# Or just double-click the file in file explorer
```

### Option 2: Local Web Server
For better performance, serve via a local web server:

```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js (if installed)
npx http-server

# Then open in browser: http://localhost:8000/autorickshaw-player-advanced.html
```

## 🎯 How to Use

1. **Select a Song**: Click on any song in the playlist on the right
2. **Play**: Click the main play button or press `Space`
3. **Navigate**: Use Previous/Next buttons or arrow keys (← →)
4. **Volume**: Adjust the volume slider (0-100%)
5. **Progress**: Click on the progress bar to seek to a specific time

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| `Space` | Play / Pause |
| `→` | Next Song |
| `←` | Previous Song |

## 🎼 Current Playlist

The webapp includes 12 classic Bollywood hits commonly heard in Mumbai autorickshaws:

1. 🚂 **Chaiyya Chaiyya** - A.R. Rahman, Sukhwinder Singh (4:13)
2. 💔 **Kabhi Kabhi Mere Dil Mein** - Mukesh (5:25)
3. ❤️ **Yeh Hai Mera Dil** - Lata Mangeshkar, Kishore Kumar (4:47)
4. 💃 **Aaja Nachle** - Sunidhi Chauhan (4:42)
5. 🌹 **Tum Jo Aaye** - Vishal Bhardwaj, Rekha Bhardwaj (4:32)
6. 🎪 **Dil Ka Bhanwar Kare Thalii** - Asha Parekh, Dev Anand (3:58)
7. 👑 **Mere Sapnon Ki Rani** - Mukesh (5:12)
8. 😍 **O Meri Jaan** - Mohammed Rafi (4:03)
9. 🎤 **Kya Khayal Hai** - Shamshad Begum (4:21)
10. ✨ **Piya Tose Naina** - Lata Mangeshkar (4:55)
11. 🎸 **Akele Hain To Kya Gham Hai** - Mohammed Rafi (4:28)
12. 💕 **Lag Ja Gale** - Lata Mangeshkar (3:44)

## 🛠️ Customization

### Add Your Own Songs

Edit the `playlist` array in the HTML file:

```javascript
const playlist = [
    {
        title: "Your Song Title",
        artist: "Artist Name",
        duration: "4:30",
        emoji: "🎵",
        videoId: "YouTube_Video_ID",  // Extract from YouTube URL
        genre: "Bollywood"
    },
    // ... more songs
];
```

### Change Colors

The app uses CSS variables. Modify these in the `:root` section:

```css
:root {
    --primary: #FF6B35;      /* Orange */
    --secondary: #004E89;    /* Blue */
    --accent: #F7931E;       /* Gold */
    --gold: #FFD700;
    --pink: #FF1493;
    --green: #00C853;
}
```

### Customize UI Text

Search for these strings and modify:
- `"🚐 AUTORICKSHAW MUSIC 🎵"` - Main title
- `"Classic Bollywood Hits from Mumbai's Iconic Three-Wheelers"` - Subtitle
- `"Your Mumbai Autorickshaw Playlist"` - Playlist section title

## 🎵 Integrating Real Audio

The current version displays YouTube video IDs. To play actual audio, you have several options:

### Option 1: Spotify Web API (Recommended)
```javascript
// Register for free at https://developer.spotify.com
const spotifyTrackId = "3n3Ppam7vgaVa1iaRUc9Lp"; // Chaiyya Chaiyya
const spotifyPlaylistId = "37i9dQZF1DXSjgZvB0UGKy"; // Bollywood playlist
```

### Option 2: JioSaavn API (India-based)
```javascript
// JioSaavn has most Bollywood songs
// Requires integration with their API
```

### Option 3: Free Music Archives
- FreeMusic Archive (freemusicarchive.org)
- Internet Archive (archive.org/details/audio)
- YouTube Audio Library

### Option 4: Local Audio Files
```javascript
const playlist = [
    {
        title: "Chaiyya Chaiyya",
        artist: "A.R. Rahman",
        duration: "4:13",
        emoji: "🚂",
        audioUrl: "/music/chaiyya-chaiyya.mp3"  // Serve locally
    }
];

// Update player code to use audioUrl instead of videoId
audioPlayer.src = song.audioUrl;
```

## 📊 Project Structure

```
circle_detection_in_an_image/
├── autorickshaw-player.html              # Basic version
├── autorickshaw-player-advanced.html     # Enhanced version (recommended)
├── autorickshaw-player-server.py         # Flask backend (optional)
└── AUTORICKSHAW_PLAYER_README.md        # This file
```

## 🔧 Python Flask Backend (Optional)

For advanced features, use the included Flask server:

### Install Dependencies
```bash
pip install flask flask-cors python-dotenv
```

### Run Server
```bash
python autorickshaw-player-server.py
```

The server will start at `http://localhost:5000`

### Features
- Serve music files from local directory
- Stream audio without downloading
- Implement a backend playlist database
- Add shuffle and repeat functionality
- Store user preferences

## 🎨 Design Inspiration

This webapp is inspired by:
- **[Deluxe Salon](https://deluxesalon.org/)** - Retro ambiance music player
- **Mumbai Autorickshaws** - Iconic colorful three-wheelers
- **Bollywood Golden Age** - Classic songs from 1950s-1990s
- **Nostalgic Web Design** - Retro colors and smooth animations

## 📱 Browser Compatibility

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🚨 Known Limitations

1. **Audio Playback**: YouTube embeds have CORS restrictions. For full audio playback, integrate with Spotify/JioSaavn API or use local audio files
2. **Offline Mode**: Requires internet connection to load song metadata and YouTube content
3. **Mobile**: Some browser restrictions on audio autoplay - user must click play button first

## 📝 Future Enhancements

- [ ] Shuffle mode
- [ ] Repeat/Loop functionality
- [ ] Favorites/Liked songs
- [ ] Playlist creation and sharing
- [ ] Dark/Light theme toggle
- [ ] Lyrics display
- [ ] Audio visualization (frequency bars)
- [ ] Autoplay on page load
- [ ] Browser storage for user preferences
- [ ] Social sharing (Twitter, WhatsApp)
- [ ] Spotify/Apple Music integration

## 🤝 Contributing

Want to add more songs or improve the design? Here's how:

1. Fork or clone the repository
2. Edit the `playlist` array with new songs
3. Test the changes in your browser
4. Share your improvements!

## 📄 License

This project is open source and free to use. Feel free to modify and distribute.

## 🚐 Why Autorickshaws?

Autorickshaws are an integral part of Mumbai's culture. These iconic three-wheelers:
- Transport millions daily across the city
- Feature vibrant colors and decorations
- Are known for their unique music systems
- Carry the heartbeat of Mumbai
- Represent the city's energy and chaos

This webapp celebrates this unique aspect of Mumbai's identity!

## 💡 Tips & Tricks

1. **Best Experience**: Use a desktop/laptop for the full visual experience
2. **Keyboard Shortcuts**: Press Space to play/pause from anywhere on the page
3. **Volume Control**: Mobile users can also use system volume controls
4. **Full Screen**: Press F11 for immersive full-screen experience
5. **Console Logs**: Check browser console (F12) for playback logs and Easter eggs

## 🎬 Demo

Simply open `autorickshaw-player-advanced.html` in your browser to see the webapp in action!

---

**Made with ❤️ for Mumbai's autorickshaws and Bollywood classics** 🚐🎵

Chalo, chalti hai! (Let's go!) 🚗💨