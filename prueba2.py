import requests
import json

host= "https://sandboxdnac2.cisco.com"
api_token= "/dna/system/api/v1/auth/token"

#Autenticacion "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=" = "devnetuser:Cisco123!" 

headers ={
    "Content-Type" : "application/json",
    'authorization': "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE="
        }
token=requests.post(host+api_token, headers=headers, verify=False)
token= token.json()
print(token)