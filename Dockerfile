FROM gentoo/stage3:amd64-uclibc-hardened

RUN mkdir /etc/portage/{sets,repos.conf}
