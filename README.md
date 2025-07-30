# 🤖 Robot Repair Simulation

A Python program that simulates building and repairing modular robots. It shows basic object-oriented programming and simple error handling.

## 🧩 Project Overview

This project has two main classes:

### `Robot`

This class creates a modular robot with three parts: head, arms, and legs. Each part is connected randomly with a 50% chance using the `random` module.

#### Methods:
- `__init__(name)`: Creates the robot with a given name and tries to connect each part.
- `connect_body_part()`: Randomly returns `True` (connected) or `False` (not connected).
- `start()`: Checks if all parts are connected. If any part is missing, it raises an `Exception` with a message.

### `RepairShop`

This class simulates a repair shop that fixes broken parts of robots and keeps a record of all repairs.

#### Methods:
- `__init__(owner)`: Sets the shop owner’s name and creates an empty list for repair records.
- `repair_logging()`: Prints the list of all repairs done.
- `new_repair_log(robot_name, part_name)`: Adds a record of a fixed part for a robot.
- `fix_robot(robot)`: Checks the robot for broken parts, repairs them, logs each repair, and makes sure the robot can start.

## 📌 Example

```python
shop = RepairShop("Smith")
robot1 = Robot("Wall-E")
robot2 = Robot("R2-D2")

shop.fix_robot(robot1)
shop.fix_robot(robot2)

print("The robots are up and running!")
shop.repair_logging()
