# =======================================================================================#
# rtirq - modified from https://github.com/rncbc/rtirq
# =======================================================================================#

%define commit_id 9945bcd018cc36815154107eba8d6e9d023276a0
%define commit_date 20240905

Summary:	Realtime IRQ thread system tunning
Name:		rtirq
Version:	%{commit_date}.48.1
Release:	1
License:	GPL-2.0+
Source0:	https://github.com/rncbc/rtirq/archive/%{commit_id}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	coreutils
BuildRequires:	util-linux
BuildRequires:	systemd

%description
Startup scripts for tunning the realtime scheduling policy and priority
of relevant IRQ service threads, featured for a PREEMPT_RT / threadirqs
enabled kernel configuration.

%prep

%autosetup -p1 -n %name-%{commit_id}

%build

%install

install -d %{buildroot}%{_sbindir}
install -vD %name.sh      -m 0755 %{buildroot}%{_sbindir}/rtirq
install -vD %name.conf    -m 0644 %{buildroot}%{_sysconfdir}/rtirq.conf
install -vD %name.service -m 0644 %{buildroot}%{_unitdir}/%name.service
install -vD %name-resume.service -m 0644 %{buildroot}%{_unitdir}/%name-resume.service

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_sbindir}/%name
%config(noreplace) %{_sysconfdir}/%name.conf
%{_unitdir}/%name.service
%{_unitdir}/%name-resume.service
