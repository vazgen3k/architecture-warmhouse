```puml
@startuml

title WarmHouse Context Diagram

top to bottom direction

!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml

Person(user, "Пользователь")
Person(admin, "Специалист по установке")

System(warmhouse, "Система 'Тёплый дом'", "Удалённое управление отоплением в доме")


System_Ext(sensor, "Датчик температуры", "Отправляет данные о температуре")
System_Ext(relay, "Реле отопления", "Включает/выключает отопление")

Rel(user, warmhouse, "Включает/выключает отопление, просматривает температуру", "Веб. интерфейс")
Rel(warmhouse, sensor, "Считывает показания", "HTTP")
Rel(warmhouse, relay, "Отправляет команды", "HTTP")
Rel(admin, warmhouse, "Подключает устройства")

@enduml
``` 