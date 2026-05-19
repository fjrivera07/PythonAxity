from pathlib import Path

from laboratorio8_1.downloader import download_file


def main():
    url = "https://ash-speed.hetzner.com/100MB.bin"
    output = Path("downloads/file.bin")
    download_file(url=url, output=output)
    print("descarga completa")


if __name__ == "__main__":
    main()
