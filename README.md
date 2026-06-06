# cicdbasics
A basic cicd pipeline using github actions

### Dependencies 
#### Running the FASTAPI server
uv add fastapi
uv run fastapi dev .\src\main.py (if you are at the root ,give full file path)

#### FASTAPI Server & Swagger
    - server   Server started at http://127.0.0.1:8000
    - server   Documentation at http://127.0.0.1:8000/docs
#### Optional Dependecies
To install optional dependencies we have to issue below command with uv
uv sync --all-extras

- Option A — optional-dependencies style
    [project.optional-dependencies]
    dev = [
        "pytest>=8.0",
        "httpx>=0.27",
    ]
# For [project.optional-dependencies]
uv sync                        # ❌ won't install pytest/httpx
uv sync --extra dev            # ✅ installs them

# For [dependency-groups]
uv sync                        # ✅ installs them automatically
uv sync --group dev            # ✅ also works explicitly
 




