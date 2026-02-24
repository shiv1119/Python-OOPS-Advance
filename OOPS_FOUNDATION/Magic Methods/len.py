class PlayList:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)
    
p = PlayList(["Lambi Lambi Chori", "Sahiba", "Paro"])
print(len(p))