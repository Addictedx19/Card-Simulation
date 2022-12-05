# card.py

class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITES = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

    def __init__(self, face, suit):

        if (face in Card.FACES) and (suit in Card.SUITES):
            self._face = face
            self._suit = suit
        else:
            raise ValueError('Invalid input')

    @property
    def face(self):
        return self._face

    @property
    def suit(self):
        return self._suit

    @property
    def image_name(self):
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation for repr()"""
        return f"Card(face = '{self.face}', suit = '{self.suit}')"

    def __str__(self):
        """Return string representation for str()"""
        return f"{self.face} of {self.suit}"

    def __format__(self,format):
        """Return formatted string in format"""
        return f'{str(self):{format}}'