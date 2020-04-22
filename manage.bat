@setlocal EnableDelayedExpansion EnableExtensions
@echo off
prompt $$

set "venv_dir=venv"
set "CONFIG_FILE=config/development.ini"

call :main_menu
exit /b 0


rem ================================ Main menu ================================

:main_menu
set "user_input="
cls
echo 1. Start server
echo 2. Install server
echo 3. Check PIP path
echo 4. Activate virtual environment
echo 5. Create virtual environment
echo=
echo 0. Exit
echo=
echo What do you want to do?
set /p "user_input="
echo=
if "!user_input!" == "0" exit /b 0
if "!user_input!" == "1" (
    cls
    call :Project.start_server
    pause
    goto main_menu
)
if "!user_input!" == "2" (
    echo Installing project...
    call :Project.install
    pause
    goto main_menu
)
if "!user_input!" == "3" (
    call :Project.check_pip_path
    pause
    goto main_menu
)
if "!user_input!" == "4" (
    echo Activating virtual environment...
    call :Project.activate_venv
    pause
    goto main_menu
)
if "!user_input!" == "5" (
    echo Creating virtual environment...
    call :Project.create_venv
    pause
    goto main_menu
)
if /i "!user_input!" == "C" call :script_cli
goto main_menu


rem ================================ Project ================================

:Project.start_server
start-web
rem start-sched
exit /b 0


:Project.install
pip install -e .
exit /b 0


:Project.check_pip_path
python -m pip --version
exit /b 0


:Project.activate_venv
call "!venv_dir!\Scripts\activate.bat"
exit /b 0


:Project.create_venv
rmdir /s /q "!venv_dir!"
python -m venv "!venv_dir!"
exit /b 0
