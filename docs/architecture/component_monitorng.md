```puml
@startuml
title Monitoring Service — Component Diagram

!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml

Container_Boundary(Monitoring, "monitoring-service") {

  Component(API, "Monitoring Query API", "HTTP API", "Выдача текущих показаний, истории для UI")
  Component(Listener, "Telemetry Listener", "Consumer", "Приём показаний из очереди")
  Component(Validator, "Telemetry Validator/Normalizer", "Валидация и нормализация показаний")
  Component(Processor, "Telemetry Processor", "Сохранение показаний, обновление текущих значений, расчёты")
  Component(Rules, "Notification Rules", "Проверка условий уведомлений")
  Component(Sender, "Notification Sender", "Отправка уведомлений во внешний сервис")
  Component(Repo, "Telemetry Repository", "Repository", "Доступ к данным мониторинга")
}

ContainerQueue(RabbitMQ, "RabbitMQ", "AMQP", "Брокер сообщений для показаний")
ContainerDb(MonitoringDb, "monitoring-db", "PostgreSQL", "История показаний, текущие значения, правила и журнал уведомлений")
System_Ext(NotificationProvider, "Сервис уведомлений", "Внешний сервис отправки SMS / Email / Push")

Rel(RabbitMQ, Listener, "Доставка событий", "AMQP")
Rel(Listener, Validator, "Передаёт события")
Rel(Validator, Processor, "Передаёт нормализованные данные")

Rel(Processor, Repo, "Сохраняет/читает телеметрию")
Rel(Repo, MonitoringDb, "Чтение/запись", "SQL")

' --- Query API
Rel(API, Repo, "Читает текущие значения и историю")

' --- Notifications
Rel(Processor, Rules, "Передаёт данные для проверки условий")
Rel(Rules, Sender, "Создаёт уведомления")
Rel(Sender, NotificationProvider, "Отправка уведомлений", "HTTPS")

@enduml
```