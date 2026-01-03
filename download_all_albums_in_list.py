import subprocess
from pathlib import Path

ALBUM_LIST_FILE = Path("_album_list.txt")

def run_spotdl_for_albums():
    if not ALBUM_LIST_FILE.exists():
        raise FileNotFoundError("_album_list.txt not found")

    with ALBUM_LIST_FILE.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            album_link = line.strip()

            # Skip blanks and comments
            if not album_link or album_link.startswith("#"):
                continue

            print(f"[{line_no}] Processing album: {album_link}")

            result = subprocess.run(
                ["python", "-m", "spotdl", album_link],
                check=False,   # do not crash entire batch
                text=True,
            )

            if result.returncode != 0:
                print(f"Failed: {album_link}")

if __name__ == "__main__":
    run_spotdl_for_albums()