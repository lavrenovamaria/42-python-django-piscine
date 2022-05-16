#!/bin/sh

curl -slI $1 | grep -i Location | cut -d ':' -d ' ' -f 2-



