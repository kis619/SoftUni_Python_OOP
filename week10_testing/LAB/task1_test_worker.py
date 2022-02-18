class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


# import unittest

from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_initialisation(self):
        worker = Worker("John", 100, 10)
        self.assertEqual("John", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        # self.assertEqual(0, worker.money)

    def test_energy_incremented_after_rest(self):
        worker = Worker("Johanna", 1000, 100)
        worker.rest()
        self.assertEqual(101, worker.energy)

    def test_working_with_negative_or_zero_energy_raises(self):
        worker = Worker("John", 100, 0)

        with self.assertRaises(Exception) as e:
            worker.work()

        self.assertEqual("Not enough energy.", str(e.exception))

    def test_money_increased_by_salary_after_work(self):
        worker = Worker("Johanna", 1000, 100)
        worker.work()
        self.assertEqual(1000, worker.money)

    def test_energy_decreased_after_work(self):
        worker = Worker("Johanna", 1000, 100)
        worker.work()
        self.assertEqual(99, worker.energy)

    def test_get_info(self):
        worker = Worker("Johanna", 1000, 100)
        worker.work()
        worker.work()
        expected = f'Johanna has saved 2000 money.'
        self.assertEqual(expected, worker.get_info())


if __name__ == "__main__":
    main()
