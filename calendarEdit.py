from ics import Calendar, Event
import arrow

calendarPath = "/home/matthieu/Downloads/matthieu.ics"
oldestEvent  = arrow.get("18/9/2023 4:00", "D/M/YYYY H:m")

with open(calendarPath, 'r') as icsFile:
    ics_text = icsFile.read()

skiped = 0
anomymized = 0
kept = 0

c = Calendar(ics_text) 
out = Calendar()

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

with open('my.ics', 'w') as f:
    f.writelines(out.serialize())