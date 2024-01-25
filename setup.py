from cx_Freeze import setup, Executable

executables = [Executable(script="copystream.py")]

setup(
    name="copystream",
    version="1.0",
    description="Console app continuously saving all copied text to a file",
    executables=executables,    
    install_requires=["pyperclip", "python-docx"],  # Add any other dependencies
)
