hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hour_final = (hour + (mins + dura) // 60) % 24
minute_final = (mins + dura) % 60

# Imprime o resultado
print("Hora final: " + str(hour_final) + ":" + str(minute_final).zfill(2))