from week1_First_steps.Exercise.project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {Pokemon.pokemon_details(pokemon)}"

    def release_pokemon(self, pokemon_name: str):
        for each_pokemon in self.pokemons:
            if each_pokemon.name == pokemon_name:
                self.pokemons.remove(each_pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        separator = '\n'
        return f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemons)}\n" \
               f"{f'{separator}'.join([f'- {poki.pokemon_details()}' for poki in self.pokemons])}"


