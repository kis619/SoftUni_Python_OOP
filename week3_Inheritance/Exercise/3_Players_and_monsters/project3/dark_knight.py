from project1.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)
        self.hero_class = "DarkKnight"