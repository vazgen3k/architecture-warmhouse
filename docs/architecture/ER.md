@startuml
title WarmHouse — ER Diagram

hide circle
skinparam linetype ortho

entity "User" as user {
  * id : uuid <<PK>>
  --
  name : varchar
  email : varchar <<UQ>>
  created_at : datetime
}

entity "House" as house {
  * id : uuid <<PK>>
  --
  owner_user_id : uuid <<FK>>
  name : varchar
  address : varchar
  created_at : datetime
}

entity "HouseAccess" as house_access {
  * id : uuid <<PK>>
  --
  house_id : uuid <<FK>>
  user_id : uuid <<FK>>
  role : varchar
  created_at : datetime
}

entity "DeviceType" as device_type {
  * id : uuid <<PK>>
  --
  code : varchar <<UQ>>
  name : varchar
  vendor : varchar
  protocol : varchar
  created_at : datetime
}

entity "Device" as device {
  * id : uuid <<PK>>
  --
  house_id : uuid <<FK>>
  device_type_id : uuid <<FK>>
  serial_number : varchar <<UQ>>
  name : varchar
  availability : varchar
  last_seen_at : datetime
  created_at : datetime
}

entity "Module" as module {
  * id : uuid <<PK>>
  --
  house_id : uuid <<FK>>
  module_type : varchar
  name : varchar
  created_at : datetime
}

entity "ModuleDevice" as module_device {
  * module_id : uuid <<FK>>
  * device_id : uuid <<FK>>
}

entity "Command" as cmd {
  * id : uuid <<PK>>
  --
  device_id : uuid <<FK>>
  command_type : varchar
  payload : json
  status : varchar
  idempotency_key : varchar <<UQ>>
  requested_by : varchar
  created_at : datetime
}

entity "TelemetryData" as telemetry {
  * id : uuid <<PK>>
  --
  device_id : uuid <<FK>>
  metric : varchar
  value : varchar
  unit : varchar
  measured_at : datetime
  received_at : datetime
}

entity "AutomationScenario" as scenario {
  * id : uuid <<PK>>
  --
  house_id : uuid <<FK>>
  name : varchar
  enabled : bool
  trigger_type : varchar
  trigger_config : json
  created_by : uuid <<FK>>
  created_at : datetime
}

entity "ScenarioAction" as action {
  * id : uuid <<PK>>
  --
  scenario_id : uuid <<FK>>
  device_id : uuid <<FK>>
  command_type : varchar
  payload : json
}

entity "NotificationRule" as notif_rule {
  * id : uuid <<PK>>
  --
  house_id : uuid <<FK>>
  metric : varchar
  condition : varchar
  threshold : varchar
  cooldown_sec : int
  enabled : bool
  created_by : uuid <<FK>>
}

' --- Relationships

user ||--o{ house
user ||--o{ house_access
house ||--o{ house_access

house ||--o{ device
device_type ||--o{ device

house ||--o{ module
module ||--o{ module_device
device ||--o{ module_device

device ||--o{ telemetry
device ||--o{ cmd

house ||--o{ scenario
user ||--o{ scenario
scenario ||--o{ action
device ||--o{ action

house ||--o{ notif_rule
user ||--o{ notif_rule

@enduml