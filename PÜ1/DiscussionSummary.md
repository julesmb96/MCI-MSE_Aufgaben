## Project background

### Purpose of project

Erstellen einer Software zur Datenerhebung, Analyse und Visualisierung für eine Leistungsdiagnostik auf einem Ergometer.
NOTE-JHU: Datenerhebung wird für die Übung gestellt ;)

...

### Scope of project

Erhebung, Zusammenfassung und Analyse von Leistungsdaten.

...

### Other background information

...

## Perspectives
### Who will use the system?

Jeder der Interesse an einem Lesitungstest hat. Im privaten als auch auch professionellen Bereich.
z.B. Ärzte, Sportwissenschaftler, etc...

...

### Who can provide input about the system?

Daten können durch das Ergometer oder den Leistungsdiagnostiker bereitgestellt werden.
NOTE-JHU: Hier eher gemeint: wer sind Experten, die man um Rat / meinungen zur Aufgabe fragen könnte. Weniger, den Prozess der Datenbereitstellung als Teil der Software.
...


## Project Objectives
### Known business rules

NOTE-JHU: Leistungstest folgen festem Ablauf. Aufwertung erfolgt nach Durchführung des Tests.
...

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies
Jede der Testpersonen bekommt eine ID zugewiesen, damit man die Daten mit der Person in Verbindung bringen kann.
Außerdem wird auch das Alter der Person angegeben(anhand vom Geburtsjahr).
Es werden jeweils die durchschnittliche Herzrate sowie die maximale Herzrate bei 300W gemessen.
Die Länge der Leistungstest beträgt jeweils 180s.
Daraus schließe ich dass, sobald die Testperson 300 W erreicht, 180 Sekunden lang die oben genannten Daten erfasst werden.
Sollte aus irgendwelchen Gründen der Test abgebrochen werden, so wird auch dies erfasst und ausgegeben(wahrscheinlich in Form einer Nachricht, wenn zBsp. eine Testperson unter 300W fallen sollte, etc.) 
Bei näherer Betrachtung komme ich zu dem Schluss, dass es eher so sein wird, dass ein Widerstand von 300 W am Ergometer eingestellt wird, da dies sinnvoller wäre.

NOTE-JHU: Eingangsdatenformate etc. In der nächsten HA
...

### Design and implementation constraints



...

## Risks


Output von falschen Daten

...

## Known future enhancements

Verwendung über Smartphone oder Tablet -->  Bluetooth/WIFI Schnittstelle zum Ergometer

...

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

...
