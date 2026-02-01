```puml
@startuml
title Automation Service — Component Diagram

!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml

Container_Boundary(Automation, "automation-service") {

  Component(API, "API", "HTTP API", "Создание и управление сценариями автоматизации")
  Component(Listener, "Event Listener", "RabbitMQ Consumer", "Приём событий для триггеров")
  Component(Engine, "Scenario Engine", "Проверка триггеров и условий сценариев")
  Component(Scheduler, "Scheduler", "Запуск сценариев по расписанию")
  Component(Planner, "Action Planner", "Формирование команд из сценария")
  Component(Gateway, "Command Gateway",  "Запрос исполнения команд в device-management-service")
  Component(Repo, "Automation Repository", "Repository", "Доступ к данным сценариев и журналу срабатываний")
}

ContainerQueue(RabbitMQ, "RabbitMQ", "AMQP", "Брокер сообщений для событий (телеметрия/статусы)")
ContainerDb(AutomationDb, "automation-db", "PostgreSQL", "Сценарии, триггеры, условия, действия, журнал срабатываний")

Container_Ext(DeviceManagement, "device-management-service", "Go", "Исполнение команд и управление устройствами")

Rel(API, Repo, "CRUD сценариев и чтение статусов")
Rel(Repo, AutomationDb, "Чтение/запись", "SQL")

Rel(RabbitMQ, Listener, "Доставка событий", "AMQP")
Rel(Listener, Engine, "Передаёт события")
Rel(Engine, Repo, "Читает сценарии/состояние")

Rel(Scheduler, Engine, "Запускает проверки по расписанию")

Rel(Engine, Planner, "Формирует список действий")
Rel(Planner, Gateway, "Создаёт команды для исполнения")
Rel(Gateway, DeviceManagement, "Запрос на исполнение команд", "HTTPS/REST")

@enduml
```