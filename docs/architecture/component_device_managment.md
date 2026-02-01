```puml
@startuml
title Device Management — Component Diagram

!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

Container_Boundary(DeviceManagement, "Device Management"){
Component(API, "Device API Controller", "HTTP API", "Приём запросов от UI и automation")
Component(DeviceRegistry, "Device Registry", "Регистрация и привязка устройств")
Component(DeviceState, "Device State Manager", "Управление состоянием устройств")
Component(CommandProcessor, "Command Processor", "Обработка и валидация команд")
Component(CommandPublisher, "Command Publisher", "RabbitMQ Adapter", "Публикация команд в брокер")
Component(CommandListener, "Command Status Listener", "RabbitMQ Consumer", "Обработка статусов команд")
Component(DeviceRepo, "Device Repository", "Доступ к данным")
}

ContainerQueue(RabbitMQ, "RabbitMQ", "Брокер сообщений для асинхронной передачи команд и данных со счетчиков")
ContainerDb(DeviceDb, "device-management-db", "PostgreSQL", "Устройства, привязки, состояние доступности, статусы команд")

Rel(API, DeviceRegistry, "Использует")
Rel(API, CommandProcessor, "Создаёт команды")
Rel(CommandProcessor, DeviceState, "Проверяет доступность")
Rel(CommandProcessor, CommandPublisher, "Публикует команды")
Rel(CommandListener, DeviceState, "Обновляет состояние")
Rel(DeviceRegistry, DeviceRepo, "CRUD")
Rel(DeviceState, DeviceRepo, "Фиксирует состояние команд")
Rel(CommandProcessor, DeviceRepo, "Сохраняет команды")
Rel(DeviceRepo, DeviceDb, "Чтение / запись", "SQL")
Rel(CommandPublisher, RabbitMQ, "Запись команд", "AMQP")


@enduml
```