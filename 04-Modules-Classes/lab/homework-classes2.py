class Song:
  def __init__(self, lyrics):
    self.lyrics = lyrics
  def print_lyrics(self):
    for line in self.lyrics:
      print(line)

a_lyrics = ["A sailor went to sea, sea, sea", "To see what he could see, see, see", "But all that he could see, see, see", "Was the bottom of the deep blue sea, sea, sea!"]
new_song = Song(a_lyrics)
new_song.print_lyrics()

##Well done - 10/10