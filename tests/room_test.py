import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Highway to Hell", "AC/DC")
        self.song_2 = Song("The Clansman", "Iron Maiden")
        self.song_3 = Song("Ace of Spades", "Motorhead")

        self.songs = [self.song_1, self.song_2, self.song_3]

        self.jack = Guest("Jack")
        self.victor = Guest("Victor")
        self.isa = Guest("Isa")

        self.guests = [self.jack, self.victor, self.isa]

        self.room = Room("The Metal Room")

    

    
