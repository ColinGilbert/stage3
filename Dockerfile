FROM gentoo/stage3:amd64-musl-vanilla

RUN mkdir /etc/portage/{repos.conf,sets}
