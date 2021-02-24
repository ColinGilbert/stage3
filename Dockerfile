FROM gentoo/stage3:latest:amd64-hardened-nomultilib:amd64-nomultilib:amd64-musl-hardened:amd64-musli-vanilla:amd64-uclibc-hardened

RUN mkdir /etc/portage/{repos.conf,sets}
