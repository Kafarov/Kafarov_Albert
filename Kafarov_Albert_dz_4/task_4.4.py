import utils


print(utils.currency_rates('AUD'))
print(utils.currency_rates('NOK'))
print(utils.currency_rates('EUR'))
print(utils.currency_dictionary())

print(utils.currency_rates(input('Введите код валюты: ')))
