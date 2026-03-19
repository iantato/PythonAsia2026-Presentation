# PythonAsia 2026 Presentation

A live interactive presentation by **Christian Mark P. Francisco**.

This presentation explores the transition from traditional SQL interactions in Python (using standard connections and raw SQL strings) to a modern Object-Relational Mapping (ORM) approach utilizing [SQLModel](https://sqlmodel.tiangolo.com/). The slides are built with [Slidev](https://sli.dev/) and complemented by a Python backend server that executes interactive code snippets in real-time.

## 🚀 Features

- Interactive Slidev presentation with live code execution.
- Python FastAPI backend server for running code snippets.
- Comparisons between traditional SQL workflows and SQLModel ORM patterns.
- Real-time output capture and display.
- *Backup option:* Use the [Marimo](https://marimo.io/) notebook for an alternative interactive experience.

## 🛠️ Prerequisites

You will need:
- **Node.js & pnpm** (for Slidev frontend)
- **Python 3.14+** (for backend server)

## 📦 Installation & Setup

### 1. Install Frontend Dependencies

```bash
pnpm install
```

### 2. Install Backend Dependencies

Navigate to the `py` directory:

```bash
cd py
```

Install the required Python packages:

```bash
# Using pip
pip install fastapi uvicorn sqlmodel

# Or using uv (recommended if you have it)
uv sync
```

## 🚀 Running the Presentation

You'll need **two terminal windows**:

### Terminal 1: Start the Python Backend Server

```bash
cd py
uvicorn runner_server:app --reload
# Or using uv:
# uv run uvicorn runner_server:app --reload
```

The server will be running at `http://localhost:8000`.

### Terminal 2: Start the Slidev Frontend

```bash
pnpm dev
```

This will open the presentation at `http://localhost:3030`.

Edit the [slides.md](./slides.md) to see changes in real-time.

Learn more about Slidev at the [documentation](https://sli.dev/).

## 🗺️ Presentation Flow

The presentation is structured as follows:

1. **The Hook:** Introduces the concept that "Data runs the world" (from what we eat to human DNA) before officially starting the talk.
2. **Introduction:** Speaker introduction (Christian Mark P. Francisco) and topic reveal.
3. **What is a Database:** A brief overview of how data is historically stored via SQL.
4. **The Old Way (Live Demo):** Using Python and DuckDB to write raw SQL strings. Demonstrates the boilerplate and potential friction.
5. **The Pythonic Alternative:** Asking "What if we can just use PURE Python instead?"
6. **Understanding ORMs:** A visual diagram explaining how Object-Relational Mapping (ORM) sits between Python code and the database.
7. **The New Way (Live Demo):** Using SQLModel to define tables as Python classes, showing how it simplifies database operations.
8. **Conclusion & Benefits:** "No more rows[0][1]" — highlighting the shift from accessing data with list indices to using predictable object attributes.
9. **Q&A**

## 📚 Alternative: Marimo Notebook

As a backup option, you can run the presentation as an interactive [Marimo](https://marimo.io/) notebook instead:

```bash
cd marimo
marimo edit notebook.py
```

This provides an alternative interactive experience with the same core content. See [marimo/README.md](./marimo/README.md) for more details.
