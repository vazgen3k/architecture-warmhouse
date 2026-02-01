@startuml
title Device Management — Command Processing (Code Diagram)

skinparam linetype ortho
skinparam classAttributeIconSize 0

class CommandProcessor {
  - commandQueue: CommandQueue
  + validate(device: Device, command: Command): bool
  + execute(device: Device, command: Command): void
}

class Device {
  + id: String
  + isOnline: bool
  + capabilities: List<CommandType>
}

class Command {
  + id: String
  + type: CommandType
  + status: CommandStatus
  + payload: Map
  + markSent(): void
  + markFailed(): void
}

class CommandQueue {
  + publish(command: Command): void
}

enum CommandType {
...
}

enum CommandStatus {
  CREATED
  SENT
  FAILED
}

CommandProcessor --> Device : checks
CommandProcessor --> Command : processes
CommandProcessor --> CommandQueue : sends to
Device "1" o-- "0..*" Command : executes

Command --> CommandType
Command --> CommandStatus

@enduml