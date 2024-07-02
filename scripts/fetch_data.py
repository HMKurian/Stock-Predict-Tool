import requests

url = "https://twelve-data1.p.rapidapi.com/price"

querystring = {"format":"json","outputsize":"30","symbol":"AQB"}

headers = {
	"x-rapidapi-key": "703e75cec2msh678d6c73540a186p1fb32ejsn50e85eb2608f",
	"x-rapidapi-host": "twelve-data1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())