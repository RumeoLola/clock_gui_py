#!/usr/bin

if python -c "import Tkinter" &> /dev/null; then
	echo "All good"
	pip list | grep -F tk
else
	pip install tk
fi
exit 0

