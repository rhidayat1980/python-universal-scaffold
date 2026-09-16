#!/usr/bin/env bash
# media/record-demo.sh: Declarative execution script for Asciinema
set -euo pipefail

# ANSI color codes
CYAN='\033[1;36m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RESET='\033[0m'

# Smooth realistic typing simulation
type_command() {
    local cmd="$1"
    local delay=0.075 # Kecepatan ketik lebih santai & mudah dibaca
    echo -ne "${CYAN}❯ ${RESET}"
    for ((i=0; i<${#cmd}; i++)); do
        echo -ne "${cmd:$i:1}"
        sleep "$delay"
    done
    echo ""
    sleep 1.2 # Beri jeda sebelum command dijalankan agar terbaca
}

# 1. Clear terminal
clear
sleep 1

echo -e "${YELLOW}# =========================================================================${RESET}"
echo -e "${GREEN}# 🚀 Python Universal Scaffold: Enterprise Golden Path Demo${RESET}"
echo -e "${YELLOW}# =========================================================================${RESET}\n"
sleep 2

# Clean up previous target if exists
rm -rf payment-service

# 2. Run Copier with defaults non-interactively
type_command "uvx copier copy --defaults gh:rhidayat1980/python-universal-scaffold payment-service"
uvx copier copy --defaults gh:rhidayat1980/python-universal-scaffold payment-service
sleep 3

# 3. Enter project directory
type_command "cd payment-service"
cd payment-service
sleep 1.5

# 4. Provision environment via uv
type_command "task setup"
task setup
sleep 3

# 5. Run DevSecOps Quality Gate
type_command "task check:all"
task check:all
sleep 3.5

echo -e "\n${GREEN}=========================================================================${RESET}"
echo -e "${GREEN}✓ All 5 Quality Gates Passed (Ruff + Pyright + Pytest + Bandit + pip-audit)!${RESET}"
echo -e "${GREEN}✓ Production-grade service ready for Kubernetes deployment in < 60 seconds.${RESET}"
echo -e "${GREEN}=========================================================================${RESET}\n"
sleep 4
