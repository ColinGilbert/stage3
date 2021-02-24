FROM gentoo/stage3:amd64-musl-hardened

RUN mkdir /etc/portage/{repos.conf,sets}
