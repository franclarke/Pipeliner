#!/usr/bin/python3
"""Modulo main"""
import os


def main():
    """Crea un archivo html en la ruta ./build/"""
    if not os.path.exists("build"):
        os.makedirs("build")
    try:
        with open("build/index.html", "r", encoding="utf8") as _f:
            pass
    except FileNotFoundError:
        with open("build/index.html", "w", encoding="utf8") as _f:
            _f.write("<html><body><h1>HOLA</h1></body></html>")


if __name__ == "__main__":
    main()
