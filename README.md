# Universal Unit Converter & Live Financial Tracker

A high-performance desktop application built with **Python 3** and **PyQt6** that handles standard scientific metrics, advanced temperature formulas, and live global currency exchange rates.

This project demonstrates strong foundational software engineering principles, specifically focusing on the separation of concerns, defensive network programming, and asynchronous-style UI behaviors.

---

## 🚀 Key Engineering Highlights

- **In-Memory Network Caching Backend:** Engineered a client-side caching mechanism for the currency network layer. By storing retrieved REST API rates in memory, the application minimizes redundant network overhead, optimizes performance, and prevents UI-blocking freezes during rapid user keystrokes.
- **Live API Integration & Defensive Programming:** Integrated the Open Exchange Rates REST API via the `requests` library. Implemented rigorous error handling, explicit timeouts, and network failure fallback states (`try/except` safeguards) to ensure an uninterrupted user experience even in offline scenarios.
- **Decoupled Architectural Design (MVC Concept):** Enforced a strict separation of concerns. The front-end presentation layer (`PyQt6`) is entirely independent of the core computational engine, allowing for a modular system where new conversion categories can be scaled seamlessly without refactoring UI files.
- **Dynamic & Responsive Presentation:** Leveraged layout managers, automated spacing constraints, and stacked widget components to ensure the UI scales fluids across varying desktop resolutions.
- **Automated Regression Testing:** Authored an automated unit testing suite targeting core mathematical boundaries to guarantee structural accuracy and eliminate computational regressions.

---

## 🛠️ Tech Stack & Concepts Demonstrated

- **Language:** Python 3
- **GUI Framework:** PyQt6 (Layouts, Slots/Signals, View Switching)
- **Networking:** HTTP Client Requests, REST APIs, JSON Parsing
- **Systems Architecture:** Caching strategies, Defensive validation, Exception handling
