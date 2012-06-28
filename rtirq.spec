Name:		rtirq
Summary:	Realtime IRQ thread system tunning
Version:	20120505
Release:	1
License:	GPLv2
URL:		http://www.rncbc.org/jack/#rtirq
Group:		System/Configuration/Boot and Init
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	/bin/sh,util-linux,sysvinit-tools
Requires(post,preun):	/sbin/chkconfig

%description
Startup scripts for tunning the realtime scheduling policy and priority
of relevant IRQ service threads, featured for a realtime-preempt enabled
kernel configuration. 

%prep
%setup -q

%build

%install
install -vD rtirq.sh   -m 0755 %{buildroot}/etc/init.d/rtirq
install -vD rtirq.conf -m 0644 %{buildroot}/etc/sysconfig/rtirq

%post
# Only run on install, not upgrade.
if [ "$1" = "1" ]; then
    chkconfig --add rtirq
    chkconfig rtirq on
fi

%preun
# Only run if this is the last instance to be removed.
if [ "$1" = "0" ]; then
    chkconfig rtirq off
    chkconfig --del rtirq
fi

%files
%config(noreplace) /etc/sysconfig/rtirq
/etc/init.d/rtirq
