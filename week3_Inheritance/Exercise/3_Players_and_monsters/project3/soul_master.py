from project1.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.hero_class = "SoulMaster"

