#!/usr/bin/env bash
set -euo pipefail

# Install Python dependencies early, while the container still has egress.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# You can add any one-off tooling here (e.g. apt-get) before the network flip.
echo "Setup complete – dependencies cached in image."

