import utils
import sys

for arg in sys.argv[1:]:
    print(utils.currency_rates(arg))


