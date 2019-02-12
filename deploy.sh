#!/bin/bash

git push
ssh iespto.ddns.net "cd ~/turno && git pull"
