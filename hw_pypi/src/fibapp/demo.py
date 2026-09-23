import subprocess
import sys
import time
import urllib.request

from fibapp import client


def _wait_for_server(url: str, timeout: float = 15.0) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=1) as r:
                if r.status == 200:
                    return
        except Exception:
            time.sleep(0.5)
    raise RuntimeError("server did not start in time")


def main() -> None:
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "fibapp.server:app",
         "--host", "127.0.0.1", "--port", "8000"],
    )
    try:
        _wait_for_server("http://127.0.0.1:8000/health")
        client.main()
    finally:
        proc.terminate()
        proc.wait()

