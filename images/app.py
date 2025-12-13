#Janitor test
import random
names_janitor= ["Hoop", "Dune", "Sky", "Tala"]
janitor_today =random.choice(names_janitor)
print(f"Welcome to Big Red. You will be served by {janitor_today}." )

#initiating bookings
class Big_Red:
  def __init__(self, event, allocation, capacity):
    self.event = event
    self.allocation =allocation
    self.capacity =capacity
upcoming =Big_Red("Guest_Meeting", "Town-Hall", 40)
