#!/usr/bin/env bash

# se crea un usuario al que conectarse desde una terminal del usuario postgres
sudo -i -u postgres bash << shell 
psql -c "CREATE USER xabiadmin WITH PASSWORD 'xabi1234';"
shell
