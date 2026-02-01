@startuml
title Device State Manager (Code Diagram)

skinparam linetype ortho
skinparam classAttributeIconSize 0

class DeviceStateManager {
  - repo: DeviceStateRepository
  + updateFromCommand(event: CommandStatusEvent): void
  + updateHeartbeat(deviceId: String, ts: DateTime): void
  + markOffline(deviceId: String): void
}

class DeviceState {
  + deviceId: String
  + availability: AvailabilityStatus
  + lastSeenAt: DateTime
  + lastError: String
  + setOnline(ts: DateTime): void
  + setOffline(reason: String): void
}

interface DeviceStateRepository {
  + get(deviceId: String): DeviceState
  + save(state: DeviceState): void
}

class CommandStatusEvent {
  + commandId: String
  + deviceId: String
  + status: CommandStatus
  + occurredAt: DateTime
  + error: String
}

enum AvailabilityStatus {
  ONLINE
  OFFLINE
  ...
}

enum CommandStatus {
  SENT
  ACK
  FAILED
  TIMEOUT
}

DeviceStateManager --> DeviceStateRepository : reads/writes
DeviceStateManager --> CommandStatusEvent : consumes
DeviceStateManager --> DeviceState : updates
DeviceState --> AvailabilityStatus
CommandStatusEvent --> CommandStatus

@enduml