
#!/bin/bash

echo "================================"
echo "Running DnD Adventure unit tests"
echo "================================"

if [ -f "venv/Scripts/python.exe" ]; then
    ./venv/Scripts/python.exe -m unittest discover -s tests -v
else
    python -m unittest discover -s tests -v
fi
