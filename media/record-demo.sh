#!/usr/bin/env bash
# media/record-demo.sh: Declarative execution script for Asciinema
set -euo pipefail

# ANSI color codes
CYAN='\033[1;36m'
GREEN='\033[1;32m'
RESET='\033[0m'

type_command() {
    local cmd="$1"
    local delay=0.03
    echo -ne "${CYAN}❯ ${RESET}"
    for ((i=0; i<${#cmd}; i++)); do
        echo -ne "${cmd:$i:1}"
        sleep "$delay"
    done
    echo ""
    sleep 0.5
}

# 1. Clear terminal
clear
sleep 0.5

echo -e "# ------------------------------------------------------------"
echo -e "# 🚀 Python Universal Scaffold: Bootstrapping in < 60 Seconds"
echo -e "# ------------------------------------------------------------\n"
sleep 1

# Clean up previous target if exists
rm -rf payment-service

# 2. Run Copier with defaults non-interactively
type_command "uvx copier copy --defaults gh:rhidayat1980/python-universal-scaffold payment-service"
uvx copier copy --defaults gh:rhidayat1980/python-universal-scaffold payment-service
sleep 1.5

# 3. Enter project directory
type_command "cd payment-service"
cd payment-service
sleep 0.5

# 4. Provision environment via uv
type_command "task setup"
task setup
sleep 1.5

# 5. Run DevSecOps Quality Gate
type_command "task check:all"
task check:all
sleep 2

echo -e "\n${GREEN}✓ All 5 Quality Gates Passed (Ruff + Pyright + Pytest + Bandit + pip-audit)!${RESET}"
echo -e "${GREEN}✓ Production-grade service ready for deployment in under 60 seconds.${RESET}\n"
sleep 2
