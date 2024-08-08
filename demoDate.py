from datetime import datetime

# Obtenir la date d'aujourd'hui
currentTime = datetime.now()

# Formater la date au format "DD-MM-YYYY"
date_formatee = currentTime.strftime("%d-%m-%Y %Hh%mm")

# Afficher la date formatée
print(f"La date d'aujourd'hui est : {date_formatee}")
