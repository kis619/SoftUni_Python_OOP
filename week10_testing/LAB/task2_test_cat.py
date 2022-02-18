class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main

class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Tom")

    def test_size_increases_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_cat_cannot_eat_if_fed_raises(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as e:
            self.cat.eat()
        self.assertEqual("Already fed.", str(e.exception))

    def test_cat_cannot_sleep_if_not_fed_raises(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as e:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(e.exception))

    def test_cat_not_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == "__main__":
    main()