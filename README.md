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

---

## 🧪 Automated Testing

This project includes a comprehensive automated test suite built with Python's native `unittest` framework. The suite consists of **19 robust test cases** designed to validate edge cases, mathematical precision, and defensive error boundaries.

### What is Covered:

- **Currency Network & Cache:** Validates cold/warm caching logic, identity short-circuits (e.g., USD to USD), API timeout handles, and HTTP network error grace states.
- **Defensive Boundaries:** Ensures incorrect categories, mismatched units, empty strings, and `None` inputs fail safely and predictably.
- **Conversion Accuracy:** Verifies multi-directional linear unit conversions and complex non-linear temperature round-trips ($A \rightarrow B \rightarrow A$) within floating-point precision.

### How to Run the Tests

If you are using **VS Code**, the easiest way to execute the tests is to open `test_converter.py` and click the **Run/Play** button in the top right corner of the editor.

Alternatively, you can execute them directly via your terminal using the project's virtual environment:

```powershell
# Navigate to the project directory
cd "Portfolio Projects\Univeral Unit Converter"

# Run the test suite via the local virtual environment
.venv\Scripts\python.exe -m unittest test_converter.py
```
