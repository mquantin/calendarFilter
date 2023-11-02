from ics import Calendar, Event
import arrow
from pathlib import Path

calendarPath = "sallesMQ.ics"
oldestEvent  = arrow.get("06/11/2023 4:00", "D/M/YYYY H:m")

def appendStringInPath(filePath, str2append):
    path = Path(filePath)
    return path.with_stem(f"{path.stem}_{str2append}")


with open(calendarPath, 'r') as icsFile:
    ics_text = icsFile.read()
c = Calendar(ics_text) 

    
def anonymize ():
    out = Calendar()
    anomymized = 0
    kept = 0
    skiped = 0

    for e in c.events:
        new = Event
        if e.begin < oldestEvent:
            skiped += 1
            continue
        elif e.name.startswith(('devWeb', 'humaNum', '3D', 'CM', 'editathon', 'Impact')):
            kept += 1
            newlocation = e.location
            newname = e.name
        else:
            newlocation = "private"
            newname = "private"
            anomymized += 1
        start = e.begin.clone()
        end = e.end.clone()
        out.events.add(Event(
            name=newname,
            location = newlocation,
            begin = e.begin,
            end= e.end,
            ))

    print(f"{kept} events kept \n{anomymized} events anomymized \n{skiped} events skiped")

    with open(appendStringInPath(calendarPath, 'edited'), 'w') as f:
        f.writelines(out.serialize())
        
def printcalendar():
    skiped = 0
    for e in c.events:
        new = Event
        if e.begin < oldestEvent:
            skiped += 1
            continue  
        else:
            print(f"{e.name}\n\t{e.begin.format('DD-MM HH:mm')}-{e.end.format('HH:mm')}\n\t{e.location}\n")

printcalendar()
     
