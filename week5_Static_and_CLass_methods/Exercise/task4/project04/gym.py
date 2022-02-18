class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def add_entity_to_list(entity, given_list):
        if entity not in given_list:
            given_list.append(entity)

    def add_customer(self, customer):
        Gym.add_entity_to_list(customer, self.customers)

    def add_trainer(self, trainer):
        Gym.add_entity_to_list(trainer, self.trainers)

    def add_equipment(self, equipment):
        Gym.add_entity_to_list(equipment, self.equipment)

    def add_plan(self, plan):
        Gym.add_entity_to_list(plan, self.plans)

    def add_subscription(self, subscription):
        Gym.add_entity_to_list(subscription, self.subscriptions)

    @staticmethod
    def find_entity(given_id, given_list):
        return [item for item in given_list if item.id == given_id][0]

    def subscription_info(self, subscription_id: int):
        subscription = Gym.find_entity(subscription_id, self.subscriptions)
        customer = Gym.find_entity(subscription.customer_id, self.customers)
        trainer = Gym.find_entity(subscription.trainer_id, self.trainers)
        exercise_plan = Gym.find_entity(subscription.exercise_id, self.plans)
        equipment = Gym.find_entity(exercise_plan.equipment_id, self.equipment)
        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{exercise_plan}"