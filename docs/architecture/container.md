```puml
@startuml
title WarmHouse Container Diagram

top to bottom direction

!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

Person(user, "User", "A user of the fitness club system")
System(WarmHouse, "WarmHouse System", "Система управления умным домом")

Container_Boundary(WarmHouse, "WarmHouse System"){
    Container(WebApp, "Web Application", "Java, Spring", "Управляет взаимодействием с устройствами")
    Container(MobileApp, "Mobile Application", "Kotlin, Swift", "Управляет взаимодействием с устройствами")
    Container(Automation, "automation-service", "Go", "Программирование устройств/настройка автоматических сценариев и управление")
    Container(DeviceManagement, "device-management-service", "Go", "Управление устройствами. Регистрация устройств и отправка команд. Контроль доступности")
    Container(Monitoring, "monitoring-service", "Go", "Сбор данных, хранение показаний, аналитика и формирование уведомлений")
    
    ContainerQueue(RabbitMQ, "RabbitMQ", "5", "Брокер сообщений для асинхронной передачи команд и данных со счетчиков")
    
    
  ContainerDb(DeviceDb, "device-management-db", "PostgreSQL", "Устройства, привязки, состояние доступности, статусы команд")
  ContainerDb(AutomationDb, "automation-db", "PostgreSQL", "Сценарии автоматизации")
  ContainerDb(MonitoringDb, "monitoring-db", "PostgreSQL", "История показаний счетчиков")
}
System_Ext(Sensors, "Датчики", "Датчики, установленные в домах пользователей")
System_Ext(Relays, "Реле", "Реле для управления устройствами")
System_Ext(NotificationProvider, "Сервис уведомлений", "Внешний сервис отправки SMS / Email / Push-уведомлений")

Rel(user, WebApp, "Использует", "HTTPS")
Rel(user, MobileApp, "Использует", "HTTPS")

Rel(WebApp, DeviceManagement, "Управление устройствами", "HTTPS / REST")
Rel(WebApp, Monitoring, "Просмотр показаний и истории", "HTTPS / REST")
Rel(WebApp, Automation, "Управление сценариями", "HTTPS / REST")

Rel(MobileApp, DeviceManagement, "Управление устройствами", "HTTPS / REST")
Rel(MobileApp, Monitoring, "Просмотр показаний и истории", "HTTPS / REST")
Rel(MobileApp, Automation, "Управление сценариями", "HTTPS / REST")

Rel(DeviceManagement, DeviceDb, "Чтение / запись", "SQL")
Rel(Automation, AutomationDb, "Чтение / запись", "SQL")
Rel(Monitoring, MonitoringDb, "Чтение / запись", "SQL")


Rel(Automation, DeviceManagement, "Запрос на выполнение команды устройством", "HTTPS")
Rel(DeviceManagement, RabbitMQ, "Публикация команд управления", "AMQP")
Rel(RabbitMQ, Relays, "Доставка команд исполнительным устройствам", "AMQP (через агент или шлюз)")
Rel(Sensors, RabbitMQ, "Публикация показаний", "AMQP (через агент или шлюз)")
Rel(RabbitMQ, Monitoring, "Передача показаний счетчиков", "AMQP")
Rel(Monitoring, NotificationProvider, "Отправка уведомлений пользователю", "HTTPS")


@enduml
```