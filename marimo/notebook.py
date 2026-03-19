import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium", layout_file="layouts/notebook.slides.json")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import anywidget
    import traitlets
    import io
    import contextlib
    import traceback

    return anywidget, contextlib, io, mo, traceback, traitlets


@app.cell(hide_code=True)
def _(anywidget, traitlets):
    # Setup Run Button
    class RunButton(anywidget.AnyWidget):

        _esm = """
        function render({ model, el }) {
          let button = document.createElement("button");

          const playIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" 
          stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-play" aria-hidden="true">
            <path d="M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z"></path>
          </svg>`;

          const checkIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" 
          stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-check" aria-hidden="true">
            <path d="M20 6L9 17l-5-5"></path>
          </svg>`;

          const errorIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" 
          stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-x" aria-hidden="true">
            <path d="M18 6L6 18M6 6l12 12"></path>
          </svg>`;

          button.innerHTML = playIcon;

          button.addEventListener("click", () => {
            model.set("value", model.get("value") + 1);
            model.save_changes();
          });

          model.on("change:status", () => {
            const status = model.get("status");

            el.classList.remove("run-button-idle", "run-button-success", "run-button-error");

            void el.offsetWidth;

            el.classList.add(`run-button-${status}`);

            if (status === "success") {
              button.innerHTML = checkIcon;
            } else if (status === "error") {
              button.innerHTML = errorIcon;
            } else {
              button.innerHTML = playIcon;
            }

            if (status !== "idle") {
              setTimeout(() => {
                model.set("status", "idle");
                model.save_changes();
              }, 2000);
            }

          });

          el.classList.add("run-button")
          el.appendChild(button)
        }
        export default { render }
        """

        _css = """
        .run-button button {

          width: 24px;
          height: 24px;
          border-radius: 50%;
          background: white;
          border: 1px solid #e2e8f0;
          display: flex;
          align-items: center;
          justify-content: center;
          cursor: pointer;
          color: #64748b;
          transition: all 0.2s ease;
          flex-shrink: 0;
          box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }

        .run-button button:hover {
          border-color: #cbd5e1;
          color: #0f172a;
          box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }

        .run-button button svg {
          width: 11px;
          height: 11px;
          stroke: black;
          fill: none;
        }

        .run-button-success button {
          color: #00A9A5;
          border-color: #00A9A5;
          animation: pulse-success 0.6s ease-out;
        }

        .run-button-error button {
          color: #A61C3C;
          border-color: #A61C3C;
          animation: pulse-error 0.6s ease-out;
        }

        @keyframes pulse-success {
          0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
          70% { box-shadow: 0 0 0 8px rgba(34, 197, 94, 0); }
          100% { box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        }

        @keyframes pulse-error {
          0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
          70% { box-shadow: 0 0 0 8px rgba(239, 68, 68, 0); }
          100% { box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        }

        .run-button button svg {
          width: 11px;
          height: 11px;
          stroke: currentColor;
          fill: none;
        }
        """

        value = traitlets.Int(0).tag(sync=True)
        status = traitlets.Unicode("idle").tag(sync=True)

    return (RunButton,)


@app.cell(hide_code=True)
def _(RunButton, execute_live_code, mo):
    def create_smart_block(default_code="", language="python"):
        """Creates isolated, click-only execution blocks."""
        raw_btn = RunButton()
        btn = mo.ui.anywidget(raw_btn)
        editor = mo.ui.code_editor(value=default_code, language=language)

        # Track the fragments and the terminal output in Marimo state!
        get_step, set_step = mo.state(0)
        get_out, set_out = mo.state("")

        def on_click(change):
            # Read the code safely INSIDE the click handler
            current_code = editor.value

            # Update our states
            set_step(get_step() + 1)

            # Update output
            output = execute_live_code(current_code)
            set_out(output)

            raw_btn.status = "idle"

            if "Traceback" in output or "Error" in output:
                raw_btn.status = "error"
            else:
                raw_btn.status = "success"

        # Bind the click handler strictly to the play button
        raw_btn.observe(on_click, names='value')

        # Return everything we need
        return btn, editor, get_step, get_out

    return (create_smart_block,)


@app.cell(hide_code=True)
def _(mo):
    def render_block(btn, editor):
        css_style = """
        .editor {
          min-height: 0px;
          display: grid;
          grid-template-columns: 35px auto;
          position: relative;
          margin-left: 50px;
          margin-right: 50px;
          margin-top: 15px;
          align-items: center;
        }
        """

        return mo.Html(f"""
        <style>
        {css_style}
        </style>
        <div class='editor'>
        {btn}{editor}
        </div>
        """)

    return (render_block,)


@app.cell(hide_code=True)
def _(contextlib, demo_globals, io, traceback):
    def execute_live_code(code_string: str) -> str:
        """Executes a Python string and captures any print() statements or errors."""
        if not code_string or not code_string.strip():
            return "No code to execute."

        output_buffer = io.StringIO()

        try:
            # Hijack the terminal output and redirect it to our buffer
            with contextlib.redirect_stdout(output_buffer):
                # Execute the code securely inside our isolated dictionary
                exec(code_string, demo_globals)

        except Exception:
            # If you make a typo on stage, gracefully catch the error
            # so it doesn't crash the Marimo notebook!
            output_buffer.write(traceback.format_exc())

        # Return whatever was printed (or the error)
        return output_buffer.getvalue()

    return (execute_live_code,)


@app.cell(hide_code=True)
def _(mo):
    def terminal_output(step: int, output: str):
        if step < 1:
            return mo.md("""
            <div style="margin-left: 84px; margin-right: 50px; font-family: serif; font-size: 12px">
            </div>
            """)

        if "Traceback" in output or "Error" in output:
            return mo.Html(f"""
            <div style="margin-left: 84px; margin-right: 50px; font-family: serif; font-size: 12px">
            {output}
            </div>
            """)

        return mo.md(f"""
        <div style="margin-left: 84px; margin-right: 50px; font-family: serif; font-size: 12px">
        {output}
        </div>
        """)

    return (terminal_output,)


@app.cell
def _(create_smart_block):
    # A dedicated area to setup code blocks e.g.:
    # btn_1, editor_1, get_step_1, get_out_1 = create_smart_block("print('Hello World')")

    btn_1, editor_1, get_step_1, get_out_1 = create_smart_block("""# SQLite3 Demo


    """)

    btn_2, editor_2, get_step_2, get_out_2 = create_smart_block("""# DuckDB SQL Code-block
    conn.sql("")

    """)

    btn_3, editor_3, get_step_3, get_out_3 = create_smart_block("""# DuckDB SQL Code-block
    conn.sql("INSERT INTO wizards VALUES (?)", [1, "Gandalf]")

    """)

    btn_4, editor_4, get_step_4, get_out_4 = create_smart_block("""# SQLModel Demo


    """)

    btn_5, editor_5, get_step_5, get_out_5 = create_smart_block("""# SQLModel Demo
    from sqlmodel import SQLModel, Field

    class Wizard(SQLModel, table=True):
        id: int | None = Field(default=None, primary_key=True)
        name: str
    """)

    btn_6, editor_6, get_step_6, get_out_6 = create_smart_block("""# SQLModel Engine Demo


    """)
    return (
        btn_1,
        btn_4,
        btn_5,
        btn_6,
        editor_1,
        editor_4,
        editor_5,
        editor_6,
        get_out_1,
        get_out_4,
        get_out_5,
        get_out_6,
        get_step_1,
        get_step_4,
        get_step_5,
        get_step_6,
    )


@app.cell(hide_code=True)
def _():
    # An isolated dictionary to hold the variables created in your live code blocks.
    demo_globals = {}
    return (demo_globals,)


@app.cell
def _():
    # SLIDE 1 [NOTES]: This is the first slide that everyone will see. Although, don't introduce the whole topic nor yourself at this slide
    #                  just yet. We first want them to understand the importance of this topic. Hence we got to move to the next slide before
    #                  actually introducing yourself and the topic.
    #
    # ADDITIONAL NOTES: People may have a hard time reading the powerpoint so make sure to set the browser to 200% zoom.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Databases 101: Ditch the Ancient SQL Scrolls for SQLModel
    ### A talk by Christian Mark P. Francisco
    """)
    return


@app.cell
def _():
    # SLIDE 2 [NOTES]: Tell everyone that the world revolves around the data. Give examples of data such as:
    #                  - What you're eating is data.
    #                  - How far or how long you've been walking is data
    #                  - Even your whole human composition or DNA is data.
    #                  Then introduce them the other part where we can even take this further and say that data runs the world.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The world revolves around data.
    """)
    return


@app.cell
def _():
    # SLIDE 3 [NOTES]: For engagement and hook, tell them to say this with you out loud. Count from 3, 2, 1 and then say the phrase again
    #                    "Data runs the world". Tell them to pause, and repeat this phrase over and over inside their head. While they are
    #                    doing that, tell them to think about systems, businesses, or companies that makes decisions based on data, whether
    #                    it's AI, fast-food chains, or the government, tell them to just keep thinking about it and for the meanwhile you will
    #                    introduce yourself.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ~~The world revolves around data.~~
    ### Data runs the world
    """)
    return


@app.cell
def _():
    # SLIDE 4 [NOTES]: Say hello once again and introduce your name and nickname. Say your credentials:
    #                  - 3rd Year student in Computer Science
    #                  - Devcon Kids Lead Learner in the Manila Chapter
    #                  - Part-Time Automation Engineer
    #                  - 5+ Years of learning, studying, and teaching Python
    #                  After the introduction go back to what they were thinking about and ask them, from all of the systems they tought about
    #                  where do they store the data? The answer is databases.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Databases 101: Ditch the Ancient SQL for SQLModels
    ### A talk by Christian Mark P. Francisco
    """)
    return


@app.cell
def _():
    # SLIDE 5 [NOTES]: We store all information and data in computers in a table that are called databases. And normally they are created
    #                  with the Structured Query Language or the SQL language. Even in Python this is the case.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Databases
    """)
    return


@app.cell
def _():
    # SLIDE 6 [NOTES]: This is a demo slide where we get to code. Use sqlite3 for the demo so that we can actually check it using
    #                  `sqlite_web`.
    #
    #                  [SYNTAX]:
    #                  import sqlite3
    #                  conn = sqlite3.connect("example.db")
    #                  cur = conn.cursor()
    #                  cur.execute("[YOUR QUERY HERE]")
    #                  # For the results
    #                  res = cur.execute("[FETCH QUERY]")
    #                  res.fetchall()
    #                  print(res)
    #                  x = res[0][1]
    #
    #                  [QUERIES]:
    #                  CREATE TABLE wizards (id INT PRIMARY KEY, name TEXT)
    #                  INSERT INTO wizards VALUES (?)
    #                  SELECT * FROM wizards
    #
    #                  We need to show them the problems of using sqlite3 or normal SQL in python. Make sure to highlight these problems:
    #                  - Writing SQL in quotes means your editor is blind. No autocomplete or syntax highlighting to guide your spell.
    #                  - A single typo like SELEC * crashes the entire application. These "Ancient Scrolls" offer no protection against human 
    #                    error.
    #                  - You must manually transform database rows into Python objects. It's tedious labor that distracts from your actual magic.
    #                  To do some of this, make sure we make a funny little scene were we accidentally create a syntax error. Not only that
    #                  but make sure to do the `.fetchall()` to show them how we normally access data from the database. Joke about when trying
    #                  to access the data, using `res[0][1]`, pause for a sec, and ask, "Let me ask you, what does this represent?" and jokingly
    #                  answer, "I am just hoping it will be a name."
    #                  Now tell them that although this works, it is not that maintainable nor readable.
    return


@app.cell
def _(
    btn_1,
    editor_1,
    get_out_1,
    get_step_1,
    mo,
    render_block,
    terminal_output,
):
    mo.vstack([
        mo.md("### Databases with Python (The normal way)"),

        # Render the duckdb connection
        render_block(btn_1, editor_1),
        terminal_output(get_step_1(), get_out_1()),
    ])
    return


@app.cell
def _():
    # SLIDE 7 [NOTES]: Introduce the solution. "So what if we can just write everything using Python?". No SQL at all, with syntax highlighting,
    #                  and better readability. Introduce Object Relational Mapping (ORM) to the crowd.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What if we can just use PURE Python instead?
    """)
    return


@app.cell
def _():
    # SLIDE 7 [NOTES]: Tell them that you won't be explaining the deep concept of ORM, but let them know that the most simplest and high-level
    #                  explanation of ORM is that it represents database tables in Python using classes or objects. This means that we no longer
    #                  have to write code to access or manipulate our databases, but instead we can just use normal Python code.
    #                  Now tell them, so that we can understand this more clearly, we can use SQLModel which is one of the ORM libraries in
    #                  Python. Briefly tell them that it was created by Sebastián Ramírez which is the writer of FastAPI and is an ORM library.
    #                  Say that you know those are a lot of words and those are a lot of jargons and tell them that you understand that it is
    #                  hard to understand right now hence why you'll show them what ORM are through code.
    return


@app.cell
def _(mo):
    diagram = """
    graph LR
        A["🐍 Python Code"] --> B["🔗 ORM<br/>(SQLModel)"]
        B --> C["🗄️ Database<br/>(SQL)"]

        style A fill:#3776ab,stroke:#333,color:#fff
        style B fill:#f39c12,stroke:#333,color:#fff
        style C fill:#336791,stroke:#333,color:#fff
    """

    mo.md(f"""
    ### An Object-Relational Mapping (ORM) lets us represent database tables as Python classes

    {mo.mermaid(diagram).text}
    """)
    return


@app.cell
def _():
    # SLIDE 8 [NOTES]: This is where we create the Wizards table. Show them the step-by-step process of creating tables in SQLModel.
    #                  Tell them that we'll be creating the Wizards table but instead of using SQL we'll be defining a class called Wizards.
    #                  Then introduce them to fields or the columns in databases, tell them that we'll be using attributes or variable names
    #                  for creating these fields. Tell them that SQLModel has Field() which we can use to define special database properties such
    #                  as Primary Keys. Tell them that every type hints automatically becomes SQL column data types.
    #
    #                  [SYNTAX]:
    #                  from sqlmodel import SQLModel, Field
    #                  
    #                  class Wizard(SQLModel, table=True):
    #                       id: int | None = Field(default=None, primary_key=True)
    #                       name: str
    # SLIDE 8.5 [NOTES]: Now we'll be introducing to them the engine which handles all the actual communication between databases.
    #                   We'll be showing them how they can create tables in this slide and insert data into the database.
    #                   Tell them that adding data to the database is just like creating normal Python objects and placing it into
    #                   the session.
    #                   Emphasize that we've completely removed SQL strings and are now using Python functionalities. Also say that the
    #                   fun thing about this is that our model automatically validates our data. And if we want to do more validation, we can
    #                   also do that.
    #
    #                   [SYNTAX]:
    #                   from sqlmodel import SQLModel, create_engine
    #
    #                   sqlite_url = "sqlite:///database.db"
    #                   engine = create_engine(sqlite_url)
    #
    #                   SQLModel.metadata.create_all(engine)
    #
    #                   # Adding stuff
    #                   from sqlmodel import Session
    #                   
    #                   wizard_1 = Wizard(name="Harry Potter")
    #                   with Session(engine) as session:
    #                        session.add(wizard_1)
    #                        session.commit()
    #
    #                   # Selecting stuff
    #                   from sqlmodel import select
    #                   
    #                   with Session(engine) as session:
    #                        statement = select(Wizard).where(Wizard.name == "Gandalf")
    #                        wizard = session.exec(statement).first()
    #                        print(wizard.name)
    #
    #                   BONUS if there's time: Briefly say that there is another magic that ORM/SQLModel can do. What if you're using two
    #                                          different databases but has the same model. Well... We can do that too with ORM's. You don't 
    #                                          need to change anything but just the URL of your engine.
    return


@app.cell
def _(
    btn_4,
    editor_4,
    get_out_4,
    get_step_4,
    mo,
    render_block,
    terminal_output,
):
    mo.vstack([
        mo.md("### Databases with Python (SQLModel ORM)"),

        # Render the SQLModel code blocks
        render_block(btn_4, editor_4),
        terminal_output(get_step_4(), get_out_4()),
    ])
    return


@app.cell
def _():
    # SLIDE 10 [NOTES]: Now we'll be introducing to them the engine which handles all the actual communication between databases.
    #                   We'll be showing them how they can create tables in this slide and insert data into the database.
    #                   Tell them that adding data to the database is just like creating normal Python objects and placing it into
    #                   the session.
    #                   Emphasize that we've completely removed SQL strings and are now using Python functionalities. Also say that the
    #                   fun thing about this is that our model automatically validates our data. And if we want to do more validation, we can
    #                   also do that.
    #
    #                   [SYNTAX]:
    #                   from sqlmodel import SQLModel, create_engine
    #
    #                   sqlite_url = "sqlite:///database.db"
    #                   engine = create_engine(sqlite_url)
    #
    #                   SQLModel.metadata.create_all(engine)
    #
    #                   # Adding stuff
    #                   from sqlmodel import Session
    #                   
    #                   wizard_1 = Wizard(name="Harry Potter")
    #                   with Session(engine) as session:
    #                        session.add(wizard_1)
    #                        session.commit()
    #
    #                   # Selecting stuff
    #                   from sqlmodel import select
    #                   
    #                   with Session(engine) as session:
    #                        statement = select(Wizard).where(Wizard.name == "Gandalf")
    #                        wizard = session.exec(statement).first()
    #                        print(wizard.name)
    #
    #                   BONUS if there's time: Briefly say that there is another magic that ORM/SQLModel can do. What if you're using two
    #                                          different databases but has the same model. Well... We can do that too with ORM's. You don't 
    #                                          need to change anything but just the URL of your engine.
    return


@app.cell
def _(
    btn_5,
    btn_6,
    editor_5,
    editor_6,
    get_out_5,
    get_out_6,
    get_step_5,
    get_step_6,
    mo,
    render_block,
    terminal_output,
):
    mo.vstack([
        mo.md("### Databases with Python (SQLModel ORM)"),

        # Render the SQLModel code blocks
        render_block(btn_5, editor_5),
        terminal_output(get_step_5(), get_out_5()),

        render_block(btn_6, editor_6),
        terminal_output(get_step_6(), get_out_6()),
    ])
    return


@app.cell
def _():
    # SLIDE 11 [NOTES]: This is the final stretch, ask them "So why SQLModel?". It's fast, it's Pythonic, it makes your development a lot faster
    #                   and safer, and it removes abuigity like rows[0][1].
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### No more rows[0][1]
    """)
    return


@app.cell
def _():
    # SLIDE 11.5 [NOTES]: End off with saying your name again and the title as well.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Databases 101: Ditch the Ancient SQL for SQLModels
    ### A talk by Christian Mark P. Francisco
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Next steps
    ### Official docs: **sqlmodel.tiangolo.com**
    ### Checkout **FastAPI integrations**
    ### Start casting your first database sorcery
    """)
    return


@app.cell
def _():
    # SLIDE 12 [NOTES]: Tell them that we'll be moving towards the Q&A portion and what is next
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Q&A
    """)
    return


if __name__ == "__main__":
    app.run()
