from datetime import datetime
def sampleresponses(input):
    message = str(input).lower()
    
    if message in ("hello","hi"):
        return "wala bala dub dub"
    if message in ("who are you"):
        return "a B O T"
    if message in ("time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y , %H:%M:%S")
        return str(date_time)
    
    return "don get it" 