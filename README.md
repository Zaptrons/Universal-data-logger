# Universal Data Logger

A clean, modular, and extensible Python project for learning the fundamentals of data acquisition systems and embedded software architecture.

---

## Project Goal

This repository is **not** intended to be a complete industrial application.

Its purpose is to provide small, focused, and reusable examples of the technologies commonly used in data logging systems.

Each milestone introduces one new concept while keeping the code simple, readable, and well documented.

---

## Current Features

- ✅ Virtual Temperature Sensor
- ✅ Sensor Interface
- ✅ Data Collector
- ✅ SQLite Database
  - Create Database
  - Create Table
  - Insert Records
  - Read All Records
  - Read Last Record
  - Count Records
  - Calculate Average Value
  - Delete All Records

---

## Project Structure

```text
Universal-data-logger/

├── src/
│   ├── sensors/
│   │   ├── sensor.py
│   │   └── temperature_sensor.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── data_collector.py
│   └── main.py
│
├── docs/
├── dashboard/
├── database/
└── README.md
```

---

## Roadmap

- [x] Milestone 1 – Virtual Sensor
- [x] Milestone 2 – SQLite Fundamentals
- [x] Milestone 3 – Database Queries
- [ ] Milestone 4 – JSON Configuration
- [ ] Milestone 5 – Logging System
- [ ] Milestone 6 – MQTT Communication
- [ ] Milestone 7 – REST API
- [ ] Milestone 8 – Dashboard

---

## Learning Objectives

This repository demonstrates the fundamentals of:

- Object-Oriented Programming (OOP)
- Interface-based Design
- SQLite Database Operations
- Clean Project Organization
- Incremental Software Development
- Git and GitHub Workflow

---

## Contributions

Contributions, suggestions, and constructive feedback are always welcome.

---

## License

MIT License