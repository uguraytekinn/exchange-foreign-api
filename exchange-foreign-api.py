import requests
import json

api_key = "999ccfb6e0955dd9602da547"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

change = input("Bozdurmak İstediğiniz Döviz Türü: ") # USD
changeResult = input("Alınan Döviz İşlemi: ") # TRY
amount = input(f"Bozdurmak İstediğiniz {change} Miktarını Giriniz: ") #Miktar USD

result = requests.get(api_url + change)
result_json = json.loads(result.text)

print(result_json["conversion_rates"][changeResult])

print("1 {0} = {1} {2}".format(change,result_json["conversion_rates"][changeResult],changeResult))