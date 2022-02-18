from classes.car_manager import Car

from unittest import TestCase, main


class CarManagerTests(TestCase):

    def setUp(self) -> None:
        self.car = Car("Kr", "fast", 1.7, 400)

    def test_init_happy(self):
        self.assertEqual("Kr", self.car.make)
        self.assertEqual("fast", self.car.model)
        self.assertEqual(1.7, self.car.fuel_consumption)
        self.assertEqual(400, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_no_value(self):
        with self.assertRaises(Exception) as error:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_model_no_value(self):
        with self.assertRaises(Exception) as error:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_fuel_consumption_invalid(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_fuel_capacity_invalid(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_fuel_amount_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(error.exception))

    def test_refuelling_happy(self):
        self.car.refuel(399)
        self.assertEqual(399, self.car.fuel_amount)

    def test_refuelling_over_capacity(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(401)
        self.assertEqual("Error", str(error.exception))

    def test_refuelling_fuel_0_or_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_drive_happy(self):
        self.car.fuel_amount = 200
        self.car.drive(100)
        fuel_consumed = 100 * 1.7 / 100
        expected = 200 - fuel_consumed
        self.assertEqual(expected, self.car.fuel_amount)

    def test_drive_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.drive(-1)
        self.assertEqual("Error", str(error.exception))

    def test_drive_not_enough_fuel(self):
        self.car.fuel_amount = 0
        with self.assertRaises(Exception) as error:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(error.exception))


if __name__ == "__main__":
    main()