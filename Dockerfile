FROM gentoo/stage3:amd64-nomultilib

RUN mkdir /etc/portage/{repos.conf,sets}
