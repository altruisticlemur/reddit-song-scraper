# Reddit Song Scraper

## About
Scrapes the top-level comments from a Reddit thread and creates a Spotify playlist.

## Demo
This is a playlist produced from the [beautiful songs thread on r/AskReddit](https://www.reddit.com/r/AskReddit/comments/s9oaa6/what_is_the_most_beautiful_song_you_have_ever/).

https://open.spotify.com/playlist/0kEVbXM9LM5pQi5vUUFRzN?si=c6442c54c6f34f9e

## How it Works
The process is split between three separate scripts. This was done so that data would not be lost between steps if an error were to occur.

The reddit_song_scraper.py file scrapes the top-level comments from a specified Reddit thread and writes each comment to the comments.txt file.

The spotify_song_finder.py uses the comments generated in the comments.txt file to search for the specified song using the Spotify API. For each song that is found, its track ID is added to songs.txt file.

Finally, the spotify_playlist_adder.py file retrieves the individuals track IDs from the songs.txt file and adds them to a specified Spotify playlist.

Note: The comments_generated and songs_generated files are the outputs generated from running the scripts on the beautiful songs thread on r/AskReddit. Additionally, I apologize for the lack of comments throughout my code, but feel free to DM me on Reddit if you have any questions.
