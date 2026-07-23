# Universal Data Logger

A clean, modular, and extensible Python project for learning data acquisition systems, clean software architecture, and embedded programming concepts.

---

## Project Goal

This repository is an educational project.

Its purpose is to demonstrate the core building blocks used in real-world data acquisition and embedded software projects while keeping the code simple, readable, and well documented.

Each milestone introduces one new concept without making the project unnecessarily complex.

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
- ✅ JSON Configuration Loader
- ✅ Centralized Logging System

---

## Project Structure

```text
Universal-data-logger/

├── src/
│   ├── config/
│   │   └── config.json
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── sensors/
│   │   ├── sensor.py
│   │   └── temperature_sensor.py
│   │
│   ├── config_loader.py
│   ├── data_collector.py
│   ├── logger.py
│   └── main.py
│
├── docs/
├── dashboard/
├── database/
├── logger.log
└── README.md
```

---

## Roadmap

- [x] Milestone 1 – Virtual Sensor
- [x] Milestone 2 – SQLite Fundamentals
- [x] Milestone 3 – Database Queries
- [x] Milestone 4 – JSON Configuration
- [x] Milestone 5 – Logging & Configuration
- [ ] Milestone 6 – MQTT Communication
- [ ] Milestone 7 – REST API
- [ ] Milestone 8 – Dashboard
- [ ] Milestone 9 – Unit Testing
- [ ] Milestone 10 – CI/CD

---

## Learning Objectives

This repository demonstrates the fundamentals of:

- Object-Oriented Programming (OOP)
- Interface-based design
- Clean project architecture
- SQLite database programming
- JSON configuration files
- Python logging
- Incremental software development
- Git and GitHub workflow

---

## Requirements

- Python 3.10+
- SQLite (included with Python)

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Zaptrons/Universal-data-logger.git
```

Move into the project directory:

```bash
cd Universal-data-logger
```

Run the application:

```bash
python src/main.py
```

---

## License

MIT License

---

Contributions, suggestions, and constructive feedback are always welcome.