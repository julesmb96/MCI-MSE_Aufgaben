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
Es werden jeweils die durchschnittliche Herzrate sowie die maximale Herzrate gemessen und erfasst, sowie die eingestellte Leistung in W anegegeben.
Die Länge der Leistungstest beträgt jeweils 180s.
Jede Testperson wird in einem anderen W Bereich getestet -Wahrscheinlich wegen des Fitnesslevels der Probanden(Profisportler, Hobbysportler,Reha-Paient).
Das wird auch daraus ersichtlich, da die Leistungsdaten bei subject_2.json sehr fluktuieren und öfter unter den geforderten Leisuntgsbereich von 100W fallen, wohingegen die anderen 2 Personen die geforderten W halten und öfter auch darüber sind.
Ich vermute, dass die Frequenz der Aufzeichnungen auf 0,001 Sekunde genau ist, da ca 180000 Einträge bei jeder Person sind.
Sollte aus irgendwelchen Gründen der Test abgebrochen werden, so wird auch dies erfasst und ausgegeben(in Form einer Nachricht) 

NOTE-JHU: Gute Beschreibung. Lesbarkeit könnte man vielleicht noch optimieren, wenn man es nicht als Fließtext formuliert sonden etwas struturiert ;)
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
