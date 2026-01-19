import os
import subprocess
import platform


def build_linux():
    sep = ":"

    app_name = "VectorEditor"

    cmd = [
        "pyinstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        f"--add-data=assets{sep}assets",
        "--name", app_name,
        "main.py"
    ]

    print(f"--- Запуск сборки под {platform.system()} ---")
    subprocess.run(cmd)
    print(f"--- Готово! Проверьте папку dist/{app_name} ---")


if __name__ == "__main__":
    build_linux()