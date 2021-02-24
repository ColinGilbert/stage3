FROM gentoo/stage3:amd64-hardened-nomultilib

RUN mkdir /etc/portage/{sets,repos.conf}
