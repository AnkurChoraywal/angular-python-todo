import uvicorn
import subprocess
from app.main import app
import subprocess

if __name__ == "__main__":
    process = subprocess.run(["alembic", "upgrade", "head"], capture_output=True, text=True)  # Capture as text
    output = process.stdout
    if process.returncode == 0:
        print("DB updated")
        # Run Server
        uvicorn.run(app, host="0.0.0.0", port=8080)
    else:
        print(f"DB Create Command failed: {output}")
    