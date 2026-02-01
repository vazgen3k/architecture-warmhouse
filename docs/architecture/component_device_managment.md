```puml
@startuml
title Device Management — Component Diagram

!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml

Component(DeviceRegistry, "Device Registry", "Регистрация и привязка устройств")
Component(DeviceState, "Device State Manager", "Управление состоянием устройств")
Component(CommandProcessor, "Command Processor", "Обработка и валидация команд")
Component(CommandPublisher, "Command Publisher", "RabbitMQ Adapter", "Публикация команд в брокер")
Component(CommandListener, "Command Status Listener", "RabbitMQ Consumer", "Обработка статусов команд")
Component(DeviceRepo, "Device Repository", "PostgreSQL", "Хранение устройств и команд")

Rel(API, DeviceRegistry, "Использует")
Rel(API, CommandProcessor, "Создаёт команды")
Rel(CommandProcessor, DeviceState, "Проверяет доступность")
Rel(CommandProcessor, CommandPublisher, "Публикует команды")
Rel(CommandListener, DeviceState, "Обновляет состояние")
Rel(DeviceRegistry, DeviceRepo, "CRUD")
Rel(DeviceState, DeviceRepo, "CRUD")
Rel(CommandProcessor, DeviceRepo, "Сохраняет команды")

@enduml
```