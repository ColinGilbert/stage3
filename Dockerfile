FROM gentoo/stage3:latest

RUN mkdir /etc/portage/repos.conf && \
	mkdir /etc/portage/sets && \
	#touch /etc/portage/package.use && \
	#touch /etc/portage/package.accept_keywords && \
	#touch /etc/portage/package.mask && \
	#touch /etc/portage/package.unmask 
