# -*- dockerfile -*-

FROM python:trixie
RUN pip install flask gunicorn

RUN apt-get update -yq \
    && apt-get install emacs x11-utils openssh-server sudo -yq \
	&& apt-get install iproute2 iputils-ping iputils-tracepath -yq \
	&& apt-get clean 

# Add user and enable x11 through ssh
RUN useradd -s /bin/bash erik \
    && echo "erik:erik" | chpasswd \
    && usermod -aG sudo erik \
    && echo "AllowTcpForwarding yes" >> /etc/ssh/sshd_config \
    && echo "X11Forwarding yes"      >> /etc/ssh/sshd_config \
    && echo "X11DisplayOffset 10"    >> /etc/ssh/sshd_config \
    && echo "X11UseLocalhost yes"    >> /etc/ssh/sshd_config \
    && echo "AddressFamily inet"     >> /etc/ssh/sshd_config

# Minimal debian does not have all locales set up
RUN apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG=en_US.utf8

# Start command (overridden by compose.yml)
CMD ["/usr/sbin/sshd","-D"]

# End
