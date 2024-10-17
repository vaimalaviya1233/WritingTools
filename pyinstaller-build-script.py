import os
import subprocess

def run_pyinstaller_build():
    pyinstaller_command = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--add-data", "icons;icons",
        "--add-data", "background_light.png;.",
        "--add-data", "background_light_popup.png;.",
        "--add-data", "background_dark.png;.",
        "--add-data", "background_dark_popup.png;.",
        "--icon=icons/app_icon.ico",
        "main.py"
    ]

    try:
        subprocess.run(pyinstaller_command, check=True)
        print("Build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pyinstaller_build()
