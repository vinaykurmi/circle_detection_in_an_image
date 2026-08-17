#!/usr/bin/env python3
"""
🚐 Autorickshaw Ki Duniya - Music Player Backend
Flask server for Mumbai autorickshaw-themed music player
Serves the webapp and provides API for music streaming
"""

from flask import Flask, jsonify, render_template_string, send_file, request
from flask_cors import CORS
import os
import json
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configuration
MUSIC_DIR = 'music'  # Directory to store music files
PLAYLISTS_DIR = 'playlists'

# Create directories if they don't exist
os.makedirs(MUSIC_DIR, exist_ok=True)
os.makedirs(PLAYLISTS_DIR, exist_ok=True)

# Mumbai Autorickshaw Playlist Database
AUTORICKSHAW_PLAYLIST = [
    {
        "id": 1,
        "title": "Chaiyya Chaiyya",
        "artist": "A.R. Rahman, Sukhwinder Singh",
        "duration": 253,
        "emoji": "🚂",
        "genre": "Retro Bollywood",
        "year": 1998,
        "movie": "Dil Se..",
        "language": "Hindi",
        "tags": ["classic", "dance", "90s", "romantic"]
    },
    {
        "id": 2,
        "title": "Kabhi Kabhi Mere Dil Mein",
        "artist": "Mukesh",
        "duration": 325,
        "emoji": "💔",
        "genre": "Classic Romance",
        "year": 1976,
        "movie": "Kabhi Kabhi",
        "language": "Hindi",
        "tags": ["vintage", "romance", "classic", "slowburn"]
    },
    {
        "id": 3,
        "title": "Yeh Hai Mera Dil",
        "artist": "Lata Mangeshkar, Kishore Kumar",
        "duration": 287,
        "emoji": "❤️",
        "genre": "Golden Era",
        "year": 1977,
        "movie": "Hera Pheri",
        "language": "Hindi",
        "tags": ["golden-age", "duet", "love", "classic"]
    },
    {
        "id": 4,
        "title": "Aaja Nachle",
        "artist": "Sunidhi Chauhan",
        "duration": 282,
        "emoji": "💃",
        "genre": "Bollywood Dance",
        "year": 2007,
        "movie": "Aaja Nachle",
        "language": "Hindi",
        "tags": ["dance", "modern", "energetic", "party"]
    },
    {
        "id": 5,
        "title": "Tum Jo Aaye",
        "artist": "Vishal Bhardwaj, Rekha Bhardwaj",
        "duration": 272,
        "emoji": "🌹",
        "genre": "Modern Retro",
        "year": 2015,
        "movie": "Piku",
        "language": "Hindi",
        "tags": ["modern", "retro-feel", "romantic", "contemporary"]
    },
    {
        "id": 6,
        "title": "Dil Ka Bhanwar Kare Thalii",
        "artist": "Asha Parekh, Dev Anand",
        "duration": 238,
        "emoji": "🎪",
        "genre": "Vintage Hit",
        "year": 1968,
        "movie": "Guide",
        "language": "Hindi",
        "tags": ["vintage", "iconic", "evergreen", "classic"]
    },
    {
        "id": 7,
        "title": "Mere Sapnon Ki Rani",
        "artist": "Mukesh",
        "duration": 312,
        "emoji": "👑",
        "genre": "Classic Romance",
        "year": 1977,
        "movie": "Hera Pheri",
        "language": "Hindi",
        "tags": ["romantic", "classic", "dreamy", "soft"]
    },
    {
        "id": 8,
        "title": "O Meri Jaan",
        "artist": "Mohammed Rafi",
        "duration": 243,
        "emoji": "😍",
        "genre": "Golden Era",
        "year": 1964,
        "movie": "Brides of Paxford",
        "language": "Hindi",
        "tags": ["golden-age", "love-song", "timeless", "rafi"]
    },
    {
        "id": 9,
        "title": "Kya Khayal Hai",
        "artist": "Shamshad Begum",
        "duration": 261,
        "emoji": "🎤",
        "genre": "Classic Vocal",
        "year": 1949,
        "movie": "Barsaat",
        "language": "Hindi",
        "tags": ["classic", "vintage", "vocal", "historic"]
    },
    {
        "id": 10,
        "title": "Piya Tose Naina",
        "artist": "Lata Mangeshkar",
        "duration": 295,
        "emoji": "✨",
        "genre": "Timeless",
        "year": 1966,
        "movie": "Dil Hi To Hai",
        "language": "Hindi",
        "tags": ["timeless", "romantic", "classic", "mangeshkar"]
    },
    {
        "id": 11,
        "title": "Akele Hain To Kya Gham Hai",
        "artist": "Mohammed Rafi",
        "duration": 268,
        "emoji": "🎸",
        "genre": "Golden Oldie",
        "year": 1957,
        "movie": "Dil Deke Dekho",
        "language": "Hindi",
        "tags": ["golden-oldie", "classic", "rafi", "evergreen"]
    },
    {
        "id": 12,
        "title": "Lag Ja Gale",
        "artist": "Lata Mangeshkar",
        "duration": 224,
        "emoji": "💕",
        "genre": "Classic Duet",
        "year": 1964,
        "movie": "Waqt",
        "language": "Hindi",
        "tags": ["classic", "duet", "romantic", "iconic"]
    }
]

# ============================================
# Routes
# ============================================

@app.route('/')
def home():
    """Serve the autorickshaw player"""
    return render_template_string(open('autorickshaw-player-advanced.html').read())

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Autorickshaw Music Player Server",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

@app.route('/api/playlist', methods=['GET'])
def get_playlist():
    """Get the complete Mumbai autorickshaw playlist"""
    return jsonify({
        "status": "success",
        "playlist": AUTORICKSHAW_PLAYLIST,
        "count": len(AUTORICKSHAW_PLAYLIST),
        "total_duration": sum(song["duration"] for song in AUTORICKSHAW_PLAYLIST),
        "theme": "Mumbai Autorickshaw Classics"
    })

@app.route('/api/playlist/<int:song_id>', methods=['GET'])
def get_song(song_id):
    """Get a specific song from the playlist"""
    song = next((s for s in AUTORICKSHAW_PLAYLIST if s["id"] == song_id), None)
    if song:
        return jsonify({
            "status": "success",
            "song": song
        })
    return jsonify({
        "status": "error",
        "message": f"Song with ID {song_id} not found"
    }), 404

@app.route('/api/playlist/search', methods=['GET'])
def search_songs():
    """Search songs by title, artist, or genre"""
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({
            "status": "error",
            "message": "No search query provided"
        }), 400

    results = [
        s for s in AUTORICKSHAW_PLAYLIST
        if query in s["title"].lower() or
           query in s["artist"].lower() or
           query in s["genre"].lower()
    ]

    return jsonify({
        "status": "success",
        "query": query,
        "results": results,
        "count": len(results)
    })

@app.route('/api/playlist/filter', methods=['GET'])
def filter_songs():
    """Filter songs by genre, year, or tags"""
    genre = request.args.get('genre', '').lower()
    year = request.args.get('year', type=int)
    tag = request.args.get('tag', '').lower()

    results = AUTORICKSHAW_PLAYLIST

    if genre:
        results = [s for s in results if genre in s["genre"].lower()]
    if year:
        results = [s for s in results if s["year"] == year]
    if tag:
        results = [s for s in results if tag in s["tags"]]

    return jsonify({
        "status": "success",
        "filters": {
            "genre": genre or None,
            "year": year,
            "tag": tag or None
        },
        "results": results,
        "count": len(results)
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get playlist statistics"""
    total_duration = sum(s["duration"] for s in AUTORICKSHAW_PLAYLIST)
    years = sorted(set(s["year"] for s in AUTORICKSHAW_PLAYLIST))
    genres = list(set(s["genre"] for s in AUTORICKSHAW_PLAYLIST))
    artists = list(set(s["artist"] for s in AUTORICKSHAW_PLAYLIST))

    return jsonify({
        "status": "success",
        "stats": {
            "total_songs": len(AUTORICKSHAW_PLAYLIST),
            "total_duration_seconds": total_duration,
            "total_duration_minutes": total_duration // 60,
            "total_duration_formatted": f"{total_duration // 60}:{total_duration % 60:02d}",
            "years_span": f"{min(years)} - {max(years)}",
            "unique_genres": len(genres),
            "genres": genres,
            "unique_artists": len(artists),
            "artists": artists,
            "average_song_duration": total_duration // len(AUTORICKSHAW_PLAYLIST)
        }
    })

@app.route('/api/random-song', methods=['GET'])
def get_random_song():
    """Get a random song from the playlist"""
    import random
    song = random.choice(AUTORICKSHAW_PLAYLIST)
    return jsonify({
        "status": "success",
        "song": song,
        "message": "🚐 Random song selected! Press play to start your journey."
    })

@app.route('/api/trending', methods=['GET'])
def get_trending():
    """Get trending/popular songs (by play count, can be enhanced)"""
    # In a real implementation, this would track play counts
    # For now, return most recent songs
    trending = sorted(AUTORICKSHAW_PLAYLIST, key=lambda x: x["year"], reverse=True)[:5]
    return jsonify({
        "status": "success",
        "trending": trending,
        "count": len(trending),
        "category": "Most Popular Mumbai Autorickshaw Hits"
    })

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    """Get song recommendations based on a song ID"""
    song_id = request.args.get('song_id', type=int)
    if not song_id:
        return jsonify({
            "status": "error",
            "message": "song_id parameter required"
        }), 400

    song = next((s for s in AUTORICKSHAW_PLAYLIST if s["id"] == song_id), None)
    if not song:
        return jsonify({
            "status": "error",
            "message": f"Song {song_id} not found"
        }), 404

    # Recommend songs with similar tags or genre
    recommendations = [
        s for s in AUTORICKSHAW_PLAYLIST
        if s["id"] != song_id and (
            s["genre"] == song["genre"] or
            any(tag in s["tags"] for tag in song["tags"])
        )
    ][:5]

    return jsonify({
        "status": "success",
        "original_song": song,
        "recommendations": recommendations,
        "count": len(recommendations)
    })

@app.route('/api/playlist/export', methods=['GET'])
def export_playlist():
    """Export playlist as JSON"""
    format_type = request.args.get('format', 'json')

    if format_type == 'json':
        return jsonify({
            "playlist_name": "Mumbai Autorickshaw Classics",
            "created": datetime.now().isoformat(),
            "songs": AUTORICKSHAW_PLAYLIST,
            "total_songs": len(AUTORICKSHAW_PLAYLIST)
        })
    elif format_type == 'm3u':
        # M3U format for media players
        m3u_content = "#EXTM3U\n"
        for song in AUTORICKSHAW_PLAYLIST:
            m3u_content += f"#EXTINF:{song['duration']},{song['artist']} - {song['title']}\n"
            m3u_content += f"{song['id']}\n"
        return m3u_content, 200, {'Content-Type': 'audio/x-mpegurl'}
    else:
        return jsonify({
            "status": "error",
            "message": f"Format '{format_type}' not supported. Use 'json' or 'm3u'"
        }), 400

@app.route('/api/now-playing', methods=['POST'])
def set_now_playing():
    """Track currently playing song (for analytics)"""
    data = request.get_json()
    song_id = data.get('song_id')

    if not song_id:
        return jsonify({
            "status": "error",
            "message": "song_id required"
        }), 400

    # In a real implementation, this would save to database
    return jsonify({
        "status": "success",
        "message": f"Now playing song {song_id}",
        "timestamp": datetime.now().isoformat()
    })

# ============================================
# Error Handlers
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "status": "error",
        "message": "Endpoint not found",
        "path": request.path
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "status": "error",
        "message": "Internal server error",
        "error": str(error)
    }), 500

# ============================================
# CLI Info
# ============================================

def print_info():
    """Print server information"""
    print("\n" + "="*60)
    print("🚐 AUTORICKSHAW KI DUNIYA - Music Player Server 🎵")
    print("="*60)
    print("\n✨ API Endpoints:\n")
    print("  GET  /api/health              - Health check")
    print("  GET  /api/playlist            - Get complete playlist")
    print("  GET  /api/playlist/<id>       - Get specific song")
    print("  GET  /api/playlist/search     - Search songs (q=query)")
    print("  GET  /api/playlist/filter     - Filter songs")
    print("  GET  /api/stats               - Get playlist statistics")
    print("  GET  /api/random-song         - Get random song")
    print("  GET  /api/trending            - Get trending songs")
    print("  GET  /api/recommendations     - Get recommendations")
    print("  GET  /api/playlist/export     - Export playlist")
    print("  POST /api/now-playing         - Track now playing")
    print("\n🌐 Web Interface:")
    print("  http://localhost:5000")
    print("\n" + "="*60 + "\n")

# ============================================
# Main
# ============================================

if __name__ == '__main__':
    print_info()
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True
    )
