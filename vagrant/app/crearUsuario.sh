#!/usr/bin/env bash
whoami
sudo -i -u postgres bash << EOF
psql -c "CREATE USER xabiadmin WITH PASSWORD 'xabi1234';"
EOF
