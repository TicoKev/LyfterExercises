def read_archives(path):
  try:
    with open(path, "r", encoding="utf-8") as file:
      lines = file.readlines()
      songs_list= []
      for line in lines:
        songs_list.append(line)
    return songs_list
  except FileNotFoundError as error:
    print("El archivo no existe", error)

def sort_songs(songs):
  try:
    sorted_songs = sorted(songs)
    return sorted_songs
  except TypeError as error:
    print("El elemento que se pasó como parámetro no es una lista")


def create_arhive(songs, path):
    with open(path, "w", encoding="utf-8") as file:
      for song in songs:
        file.write(song)

 
def main ():
    songs = read_archives("songs.txt")
    sorted_songs = sort_songs(songs)
    new_songs_archive = create_arhive(sorted_songs, "sortedSongs.txt")

if __name__ == "__main__":
    main()





