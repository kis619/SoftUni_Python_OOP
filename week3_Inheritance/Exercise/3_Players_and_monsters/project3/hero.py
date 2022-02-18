class Hero:
    def __init__(self, username: str, level: int):
        self.level = level
        self.username = username
        self.hero_class = "Hero"

    def __str__(self):
        return f"{self.username} of type {self.hero_class} has level {self.level}"


