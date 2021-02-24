FROM gentoo/stage3:latest:amd64-hardened-nomultilib:amd64-nomultilib

RUN mkdir /etc/portage/{repos.conf,sets}
