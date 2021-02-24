FROM gentoo/stage3:amd64-hardened-nomultilib

RUN mkdir /etc/portage/{repos.conf,sets}
