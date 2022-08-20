from uuid import uuid4


class Field:
    def __init__(self):
        cards_on_field: []
        # list of cards used and thrown
        trash: []
        # TODO method to randomly fill the deck
        deck: []
        def set_deck(self):
            self.deck = []


class Player:
    def __init__(self):
        self.uuid = uuid4()
    cards_on_hand: []
    # uuid`s of cards on field
    cards_on_field: []


class GameMain:
    def __init__(self):
        self.field = Field()
    # List of players objects
    players = []

    def game_start(self):
        # set deck
        # set deck iterations
        # give cards to every player
        # start game
        print("game is started")
        pass

    def one_game_iteration(self):
        # Faza razvitiya
        # Faza pitaniya
        # Faza vimiraniya
        pass
