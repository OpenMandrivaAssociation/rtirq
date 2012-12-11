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


%changelog
* Thu Jun 28 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20120505-1
+ Revision: 807349
- update to 20120505

* Tue Jan 24 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20111007-1
+ Revision: 767879
- imported package rtirq


* Tue Jan 24 2012 Dmitry Mikhirev <dmikhirev@mandriva.org>
- Adapted for Mandriva
* Fri Oct  7 2011 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Version 20111007.
* Mon Mar 14 2011 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Version 20110314.
* Sun Sep 20 2009 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Version 20090920.
* Fri Sep 11 2009 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Fixed for rtc being missed on newer kernel-rt >= 2.6.31. 
- Version 20090911.
* Mon Aug 10 2009 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Fixed some specific gawk regex particles for portability sake.
- Version 20090810.
* Sat Aug  8 2009 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Starting from kernel-rt >= 2.6.31 the IRQ service threads are
  now being separate to its own and corresponding device-driver,
  giving chance for shared IRQ line tuning resolution.
- Version up to 20090828.
* Fri Jun 26 2009 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Fix status on newer kernels naming soft-irq threads with this
  shorter prefix "sirq-..." instead of older "softirq-...".
- Version bump to 20090626.
* Sat Jan 31 2009 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Ubuntustudio contributed patches.
- LICENSE file added to distribution tarball.
* Fri Oct 12 2007 Rui Nuno Capela <rncbc@users.sourceforge.net>
* Mon Jan 1 2007 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Force bash as specific shell interpreter.
- Add default support for alternate configuration file locations.
- Stamped with 20071012 version.
* Sat Dec 16 2006 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Make headers clear that this is GPLed software.
- Got rid of those softirq-timer highest priority by default.
- Going up for 20061216 encarnation.
* Sat Aug 19 2006 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Apparently the echo to /proc/...threaded does not like a final CR,
  as noted by Fernando Lopez-Lezcano on a PREEMPT_DESKTOP kernel.
- Bumped to 20060819 version.
* Thu Aug 17 2006 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Bumped to 20060817 version.
* Wed Feb 18 2006 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Set all softirq-timers to highest priority; 20060218 version.
* Wed Sep 14 2005 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Touched to 20050914 version.
* Tue Aug 16 2005 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Fixed to 20050816 version.
* Wed Jun 20 2005 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Up to 20050620 tinyfix version.
* Wed Jun 8 2005 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Fixes on non threading IRQ service (thanks to Luis Garrido).
- Bumped to 20050608 version.
* Wed Jun 1 2005 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Missing info on status list was fixed for IRQs>99. 
- Moved to 20050601 version.
* Wed Apr 15 2005 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Non threading IRQ service list configuration option.
- Moved to 20050415 version.
* Wed Apr 8 2005 Rui Nuno Capela <rncbc@users.sourceforge.net>
- IRQ handler refrence name included on status listing.
- Prevent lower priority overriding due to shared IRQs.
- Fixed to 20050408 version.
* Thu Nov 12 2004 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Bumped to 20041112 version.
* Thu Nov 8 2004 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Update for the new 20041108 version.
* Thu Nov 4 2004 Rui Nuno Capela <rncbc@users.sourceforge.net>
- Created initial rtirq.spec
