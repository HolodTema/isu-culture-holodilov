import os
import pathlib
import requests
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

DEFAULT_URL = "http://127.0.0.1:8000"
DEFAULT_N = 10
DEFAULT_OUTPUT = Path("output/fib.png")

def fetch_fibonacci(server_url: str, n: int) -> list:
    response = requests.get(
        server_url.rstrip("/") + "/fib",
        params={"n": n},
        timeout=5,
    )
    response.raise_for_status()
    list_fib = response.json()["values"]
    return [int(v) for v in list_fib]


def save_plot(values: list, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    xs = list(range(len(values)))
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(xs, values, marker="o", color="red", linewidth=2)
    ax.set_title("Fibonacci numbers")
    ax.set_xlabel("index")
    ax.set_ylabel("value")
    fig.tight_layout()
    fig.savefig(output, dpi=120)
    plt.close(fig)


def main() -> None:
    server_url = os.environ.get("FIBONACCI_SERVER_URL", DEFAULT_URL)
    n = int(os.environ.get("FIBONACCI_N", str(DEFAULT_N)))
    output = Path(os.environ.get("FIBONACCI_OUTPUT", str(DEFAULT_OUTPUT)))

    values = fetch_fibonacci(server_url, n)
    save_plot(values, output)
    print("Fetched " + str(len(values)) + " numbers from " + server_url + ": " + str(values))
    print("Plot was saved to " + str(output.resolve()))


if __name__ == "__main__":
    main()

