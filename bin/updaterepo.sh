#!/bin/sh
rm -f ~/RPMS/x86_64/*.noarch.rpm
ln -s ~/RPMS/noarch/*.rpm ~/RPMS/x86_64/
createrepo ~/RPMS/x86_64/
