#!/bin/bash

# ======================================== Configurations ========================================

config() {
    venv_dir="venv"
    CONFIG_FILE="config/development.ini"
    use_python="python3.8"
    return 0
}

# ======================================== main ========================================

__main__() {
    config

    export CONFIG_FILE="${CONFIG_FILE}"

    alias_python

    if [ "$1" != "" ]; then
        run_as_cli "$@"
    else
        main_menu
    fi

    return $?
}


# ================================ CLI script ================================

run_as_cli() {
    config

    alias_python

    action=""
    if [ "$1" = "--setup" ]; then action="setup"; fi
    if [ "$1" = "--run" ]; then action="run"; fi
    if [ "$1" = "--test" ]; then action="test"; fi
    if [ "$1" = "--help" ]; then action="help"; fi

    if [ "${action}" = "setup" ]; then
        Project_install_packages
        Project_create_venv
        Project_activate_venv
        Project_install
    elif [ "${action}" = "run" ]; then
        Project_activate_venv
        Project_start_server
    elif [ "${action}" = "test" ]; then
        Project_activate_venv
        Project_test
    elif [ "${action}" = "help" ]; then
        show_help
    else
        echo "error: unknown option specified"
        echo "Try using '--help' for more information."
        return 1
    fi
    return $?
}

# ======================================== User Interfaces ========================================

# ================================ Main Menu ================================

main_menu() {
    while true; do
        clear
        echo "1. Start server"
        echo "2. Install server"
        echo "3. Check PIP path"
        echo "4. Activate virtual environment"
        echo "5. Create virtual environment"
        echo "6. Install required packages"
        echo
        echo "0. Exit"
        echo
        echo "What do you want to do?"
        read -r user_input
        echo
        case "$user_input" in
            "0")    return 0 ;;
            "1")
                clear
                Project_start_server
                pause
                ;;
            "2")    Project_install ; pause ;;
            "3")    Project_check_pip_path ; pause ;;
            "4")    Project_activate_venv ; pause ;;
            "5")    Project_create_venv ; pause ;;
            "6")    Project_install_packages ; pause ;;
            *) continue ;;
        esac
        echo
    done
    return 1
}

# ================================ Help text ================================

show_help() {
    command_name="manage.sh"
    echo "Usage:"
    echo "  ${command_name} [OPTIONS]"
    echo
    echo "OPTIONS"
    echo "  --setup     Setup project environment and installation"
    echo "  --run       Run the project"
    echo "  --test      Test the project"
    echo "  --help      Display this help"
    echo
    echo "NOTES"
    echo "  - This script is only tested in Ubuntu"
}

# ======================================== Core Function ========================================

# ================================ Alias ================================

alias_python() {
    if [ "${use_python}" != "" ]; then
        python() {
            "${use_python}" "$@"
        }
    fi
}

# ================================ Project ================================

Project_start_server() {
    start-web &
    start-sched &
}

Project_install() {
    python -m pip install wheel
    python -m pip install -e .
}

Project_check_pip_path() {
    python -m pip --version
}

Project_activate_venv() {
    source "${venv_dir}/bin/activate"
}

Project_create_venv() {
    python -m venv "${venv_dir}"
}

Project_install_packages() {
    sudo apt -y update
    sudo apt install -y git
    sudo apt install -y "${use_python}"
    sudo apt install -y "python3-pip"
    sudo apt install -y "${use_python}-dev" "${use_python}-venv"
}

# ======================================== Shortcut ========================================

pause() {
    read -n 1 -s -r -p "Press any key to continue..."
}

# ======================================== Run Script ========================================

__main__ "$@"
