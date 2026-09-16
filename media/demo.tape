# VHS Tape Script: Python Universal Scaffold Quickstart Demo
# Output: media/demo.gif
# To generate: vhs media/demo.tape

Output media/demo.gif

Set Shell "bash"
Set FontSize 16
Set Width 1200
Set Height 680
Set Padding 20
Set Theme "Catppuccin Mocha"
Set WindowBar Colorful
Set Framerate 30

Type "# Scaffold a production-grade FastAPI microservice in seconds"
Sleep 500ms
Enter
Sleep 1s

Hide
Type "rm -rf payment-service"
Enter
Show

Type "uvx copier copy gh:rhidayat1980/python-universal-scaffold payment-service"
Sleep 500ms
Enter

# Wait for interactive prompt
Sleep 3s

# Archetype selection (api-service)
Enter
Sleep 1s

# Python version (3.13)
Enter
Sleep 1s

# Include container (Yes)
Enter
Sleep 1s

# Include database (Yes)
Enter
Sleep 1s

# Author Name
Enter
Sleep 500ms

# Author Email
Enter
Sleep 3s

# Move into generated project
Type "cd payment-service"
Enter
Sleep 1s

# One-click environment provisioning with uv
Type "task setup"
Enter
Sleep 2.5s

# Run comprehensive quality & security gate
Type "task check:all"
Enter
Sleep 4s

Type "# All 5 DevSecOps quality gates passed! 🚀"
Sleep 500ms
Enter
Sleep 3s
