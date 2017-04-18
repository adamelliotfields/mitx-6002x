def song_playlist(songs, max_size):
    '''
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order in which they were chosen.
    '''
    result = []
    space = 0

    if songs[0][2] > max_size:
        return []
    else:
        result.append(songs[0][0])
        space += songs[0][2]
        songs.remove(songs[0])
        sorted_songs = sorted(songs, key=lambda x: x[2])

        while True:
            if sorted_songs == []:
                break
            elif sorted_songs[0][2] + space < max_size:
                result.append(sorted_songs[0][0])
                space += sorted_songs[0][2]
                sorted_songs.remove(sorted_songs[0])
            else:
                break

    return result
