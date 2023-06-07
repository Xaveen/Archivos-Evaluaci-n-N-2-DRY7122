import urllib.parse
import requests
while True:
    host= "https://www.mapquestapi.com/directions/v2/route?"
    orig= input("Escriba un lugar de Origen: ")
    if orig == "quit" or orig == "q":
        break
    dest= input("Escriba un lugar de Destino: ")
    if dest == "quit" or dest == "q":
        break
    token="CbQoH61K50hjNsXNHsg85XbwxyMPSt6Y"

    url = host + urllib.parse.urlencode({"key":token, "from":orig, "to":dest, "unit": "k"})

    respuesta= requests.get(url).json()
    estado= respuesta["info"]["statuscode"]
    if estado == 0:
        print("=============================================")
        print("Para ir desde: " + (orig) + " Hasta " + (dest))
        print("El viaje dura:   " + respuesta["route"]["formattedTime"])
        print("Kilometros:      " + str("{:.2f}".format((respuesta["route"]["distance"]))))
        print("=============================================")
    for each in respuesta["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " km)"))
        print("=============================================\n")