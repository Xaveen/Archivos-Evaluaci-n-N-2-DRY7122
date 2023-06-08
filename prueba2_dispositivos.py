import requests
import json

host= "https://sandboxdnac2.cisco.com"
get_device= "/dna/intent/api/v1/network-device"
token= "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MjQxOTIzZTU3MjU5NTA2YTU2YjRhYTEiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYyM2YwMjlhNTcyNTk1MDZhNTZhZDljNCJdLCJ0ZW5hbnRJZCI6IjYyM2YwMjk4NTcyNTk1MDZhNTZhZDliZCIsImV4cCI6MTY4NjA4NzYxMywiaWF0IjoxNjg2MDg0MDEzLCJqdGkiOiIxMTdlM2Y5My1iNWFkLTRiNjMtOGQ2My0wNzgzNmY1YmFhZmEiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.hp8gOnIAdf4hU2jQ4mN0XPsW08kzqAhhWaE4tAX4Svv4ncO4a0Ybh3sj07pLlhOpIQFsH9VTlIhJt0ItDLK31OOr-TfjQOeG5c1-GxD_vNnMs4ZMorylstbJoZGRRz61vWmDJrPEJ8PO8EW2gCas_ZOFVFS1swqorNvFZXq_6T4mLpVrIFYb8TZn2kQ4y0SvMwdr1LCdsEYzwN7REI18GqPETnn9B_RVKdT5prbFk8rB1ktCkyRMLzqOlSnPyp_LFDiH5nosidyiePjqNb-Q5wHXcbEdSDq4JP0ZlF7YeEt3oaCNU6ZW2qLcQyA5yqN4GwK7qtcLFMnqNUkV4WTjhg"

header= {"Content-Type": "application/json",
         "x-auth-token": token}

equipos= requests.get(host+get_device, headers=header, verify=False)
equipos= equipos.json()["response"]
for i in equipos:
   print(f"El dispositivo {i['hostname']}, tiene la ip de administracion: {i['managementIpAddress']}")
