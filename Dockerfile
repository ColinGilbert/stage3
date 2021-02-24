FROM gentoo/stage3:latest:amd64-hardened-nomultilib

RUN mkdir /etc/portage/{repos.conf,sets}
