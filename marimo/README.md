# Databases 101: Ditch the Ancient SQL for SQLModels

A live interactive presentation by **Christian Mark P. Francisco**.

This presentation explores the transition from traditional SQL interactions in Python (using standard connections and raw SQL strings) to a modern Object-Relational Mapping (ORM) approach utilizing [SQLModel](https://sqlmodel.tiangolo.com/).

The slides are built entirely in Python using [Marimo](https://marimo.io/), an open-source reactive data science notebook. It features custom interactive widgets that allow live code execution directly within the slides!

## 🚀 Features

- Interactive Marimo-powered slides.
- Live, isolated code execution blocks for real-time demonstrations.
- Custom stateful UI widgets (like animated run/add block buttons).
- Comparisons between DuckDB raw SQL workflows and SQLModel ORM patterns.

## 🛠️ Prerequisites

To run this presentation locally, you will need Python installed. The project dependencies are managed via standard Python packaging (refer to `pyproject.toml`).

Main dependencies:
- `marimo`
- `anywidget`
- `duckdb`
- `sqlmodel`

## 📦 Installation & Setup

1. **Clone the repository or navigate to the project directory:**
   ```bash
   cd "Marimo Presentation"
   ```

2. Sync the project dependencies using uv:
   ```bash
   uv sync
   ```
   _Note: This will automatically create a virtual environment (.venv) and install all required packages inside it._

3. Activate the virtual environment:
   ```bash
   # Windows
   .venv\Scripts\activate

   # macOS / Linux
   source .venv/bin/activate
   ```

## 📖 How to Run the Presentation
To start the interactive presentation, use the Marimo command-line interface.

**Edit Mode**

If you want to view, edit, or tweak the slides and internal code:

```bash
marimo edit notebook.py
```

## 🗺️ Presentation Flow
he presentation is structured as follows:

1. **The Hook:** Introduces the concept that "Data runs the world" (from what we eat to human DNA) before officially starting the talk.
2. **Introduction:** Speaker introduction (Christian Mark P. Francisco) and topic reveal.
3. What is a Database: A brief overview of how data is historically stored via SQL.
4. T**he Old Way (Live Demo):** Using Python and DuckDB to write raw SQL strings. Demonstrates the boilerplate and potential friction.
5. **The Pythonic Alternative:** Asking "What if we can just use PURE Python instead?"
Understanding ORMs: A visual diagram (Mermaid) explaining how Object-Relational Mapping (ORM) sits between Python code and the Database.
6. **The New Way (Live Demo):** Using SQLModel to define tables as Python classes, showing how it simplifies database operations.
7. **Conclusion & Benefits:** "No more rows[0][1]" — highlighting the shift from accessing data with list indices to using predictable object attributes.
8. **Q&A**