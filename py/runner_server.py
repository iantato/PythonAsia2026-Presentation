# runner_server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import io
import traceback

app = FastAPI()

# Allow Slidev to talk to this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodePayload(BaseModel):
    code: str

# Dictionary to keep the Python state alive between slide runs!
session_globals = {}

@app.post("/run")
async def execute_python(payload: CodePayload):
    # Capture standard output (print statements)
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    try:
        # Execute the code using your real, local Python environment
        exec(payload.code, session_globals)
        output = redirected_output.getvalue()
    except Exception:
        output = traceback.format_exc()
    finally:
        sys.stdout = old_stdout

    return {"text": output}

# Run this script with: uvicorn runner_server:app --reload