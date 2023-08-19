import sqlite3 as sql
import requests 
import json
cep = input('Digite o seu cep:')
url = f'https://viacep.com.br/ws/{cep}/json/'
response = requests.get(url)