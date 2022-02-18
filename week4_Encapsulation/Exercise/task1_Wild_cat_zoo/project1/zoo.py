from project1.caretaker import Caretaker
from project1.keeper import Keeper
from project1.vet import Vet
from project1.cheetah import Cheetah
from project1.lion import Lion
from project1.tiger import Tiger


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        if not self.__budget >= price and len(self.animals) < self.__animal_capacity:
            return f"Not enough budget"

        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [employee for employee in self.workers if employee.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        to_be_paid = sum(
            worker.salary for worker in self.workers)  # sum(map(lambda worker: worker.salary, self.workers))
        if self.__budget >= to_be_paid:
            self.__budget -= to_be_paid
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        # lions = filter(lambda animal: type(animal) == Lion, self.animals)
        # tigers = filter(lambda animal: type(animal) == Tiger, self.animals)
        # cheetahs = filter(lambda animal: type(animal) == Cheetah, self.animals)

        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if type(animal) == Lion:
                lions.append(repr(animal))

            elif type(animal) == Tiger:
                tigers.append(repr(animal))
            else:
                cheetahs.append(repr(animal))

        separator = "\n"

        text = f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{separator.join(lions)}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{separator.join(tigers)}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{separator.join(cheetahs)}"

        return text

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if type(worker) == Keeper:
                keepers.append(repr(worker))
            elif type(worker) == Caretaker:
                caretakers.append(repr(worker))
            elif type(worker) == Vet:
                vets.append(repr(worker))

        separator = "\n"

        text = f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{separator.join(keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{separator.join(caretakers)}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{separator.join(vets)}"

        return text

