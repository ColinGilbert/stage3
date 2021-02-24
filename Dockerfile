FROM gentoo/stage3:amd64-musl-hardened

RUN mkdir /etc/portage/{sets,repos.conf}
