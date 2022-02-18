from project04.customer import Customer
from project04.equipment import Equipment
from project04.exercise_plan import ExercisePlan
from project04.subscription import Subscription
from project04.trainer import Trainer
from project04.gym import Gym

customer = Customer("John", "Dianabad", "kis619@abv.bg")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))

