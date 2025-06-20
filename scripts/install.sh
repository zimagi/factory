#!/usr/bin/env bash
#
# Install module related dependencies
#
if ! which aider 1>/dev/null 2>&1; then
  curl -LsSf https://aider.chat/install.sh | sh
fi
