#!/bin/sh
rm -f RPMS/x86_64/*.noarch.rpm
(cd RPMS/x86_64 && ln -s ../../RPMS/noarch/*.rpm .)
createrepo RPMS/x86_64/
