from week5_Static_and_CLass_methods.Exercise.task2.constants import DVD_CAPACITY_OF_MOVIE_WORLD, CUSTOMER_CAPACITY_OF_MOVIE_WORLD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return DVD_CAPACITY_OF_MOVIE_WORLD

    @staticmethod
    def customer_capacity():
        return CUSTOMER_CAPACITY_OF_MOVIE_WORLD

    def add_customer(self, customer):
        if len(self.customers) < CUSTOMER_CAPACITY_OF_MOVIE_WORLD:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < DVD_CAPACITY_OF_MOVIE_WORLD:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        curr_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        for dvd in curr_customer.rented_dvds:
            if dvd.id == dvd_id:
                return f"{curr_customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if curr_customer.age < dvd.age_restriction:
            return f"{curr_customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            curr_customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{curr_customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        curr_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]

        if dvd.id in curr_customer.rented_dvds:
            dvd.is_rented = False
            curr_customer.rented_dvds.remove(dvd)
            return f"{curr_customer.name} has successfully returned {dvd.name}"

        return f"{curr_customer.name} does not have that DVD"

    def __repr__(self):
        customers = ""
        for customer in self.customers:
            customers += f"{customer.__repr__()}\n"

        dvds = ""
        for dvd in self.dvds:
            dvds += f"{dvd.__repr__()}\n"

        return customers + dvds