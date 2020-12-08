#!/usr/bin/env bash
whoami
sudo -i -u postgres bash << EOF
echo "In"
psql -c "CREATE USER xabiadmin WITH PASSWORD 'xabi1234';"
EOF
echo "Out"
whoami
