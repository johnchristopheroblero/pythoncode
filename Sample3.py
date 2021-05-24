importjson
importxml.etree.ElementTree as et

class Song:
def __init__(self, song_id, title, artist):
self.song_id = song_id
self.title = title
self.artist = artist




classSongSerializer:
def serialize(self, song, format):
if format == 'JSON':
song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
returnjson.dumps(song_info)
elif format == 'XML':
song_info = et.Element('song', attrib={'id': song.song_id})
title = et.SubElement(song_info, 'title')
title.text = song.title
artist = et.SubElement(song_info, 'artist')
artist.text = song.artist
returnet.tostring(song_info, encoding='unicode')
else:
raiseValueError(format)
