import random

from dotenv import dotenv_values

AMOUNT_MIN = 100  # Min amount to bridge
AMOUNT_MAX = 150  # Max amount to bridge
TIMES = 1  # Number of runs

AMOUNT_TO_SWAP = random.randint(AMOUNT_MIN, AMOUNT_MAX)  # Bridge Quantity Randomization

private_keys = dotenv_values("private_keys.env")
WALLETS = [key for key in private_keys.values()]
