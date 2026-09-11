#!/bin/bash
set -e

# Return to parent directory if currently inside terraform directory
if [ -d "../terraform" ]; then
    cd ..
fi

ansible ec2app -m ping -i hosts.ini

ansible-playbook -i hosts.ini my-playbook.yml