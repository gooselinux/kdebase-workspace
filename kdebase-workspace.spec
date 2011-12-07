%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: K Desktop Environment - Workspace
Name: kdebase-workspace
Version: 4.3.4
Release: 19%{?dist}
URL: http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdebase-workspace-%{version}.tar.bz2
License: GPLv2
Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# RH/Fedora-specific startkde changes
Patch1: kdebase-workspace-4.2.96-redhat-startkde.patch

# add konsole menuitem
Patch2: kdebase-workspace-4.2.95-plasma-konsole.patch

# only show in KDE
Patch3: kdebase-workspace-4.2.90-show_systemsettings.patch

# ConsoleKit >= 0.2.4 shutdown/reboot support (needed for GDM 2.22)
Patch4: kdebase-workspace-4.2.85-ck-shutdown.patch

# 441062: packagekit tools do not show icons correctly on KDE
Patch7: kdebase-workspace-4.0.3-krdb.patch

# correct quoting
Patch8: kdebase-workspace-4.2.85-klipper-url.patch

# 434824: KDE4 System Settings - No Method To Enter Administrative Mode
Patch9: kdebase-workspace-4.2.95-rootprivs.patch

# drop useless kde font directories
Patch11: kdebase-workspace-4.1.96-font.patch

# drop BR on PyQt4/sip
Patch13: kdebase-workspace-4.2.0-pykde4.patch

# no klipper action on selection for Arora browser
Patch14: kdebase-workspace-4.2.0-klipper-arora.patch

# kio_sysinfo based on OpenSUSE's patch
Patch15: kdebase-workspace-4.2.0-kio_sysinfo.patch

# show the remaining time in the battery plasmoid's popup (as in 4.2) (#515166)
Patch16: kdebase-workspace-4.3.0-battery-plasmoid-showremainingtime.patch

# allow adding a "Leave..." button which brings up the complete shutdown dialog
# to the classic menu (as in KDE <= 4.2.x); the default is still the upstream
# default Leave submenu
Patch17: kdebase-workspace-4.3.1-classicmenu-logout.patch

# support plymouth in kdm
Patch18: kdebase-workspace-4.3.4-kdm_plymouth.patch

# do not link calendar data engine with Akonadi
Patch19: kdebase-workspace-4.3.4-calendar-akonadi.patch

# add missing header files
Patch20: kdebase-workspace-4.3.4-missing_include.patch

# bz#567286, ask user password for locked screen settings 
Patch21: kdebase-workspace-bz#567286-configure-screensaver.patch

# keyboard stops working, https://bugs.kde.org/show_bug.cgi?id=171685#c135
Patch50: kdebase-workspace-4.3.3-kde#171685.patch

# fixup brightness fn keys
Patch51: http://bazaar.launchpad.net/~kubuntu-members/kdebase-workspace/ubuntu/download/head:/kubuntu_101_brightne-20091019223214-s1uoamqahgp3uee7-1/kubuntu_101_brightness_fn_keys_and_osd.diff

# fixups for hal-0.5.14 compat
Patch52: kdebase-workspace-4.3.4-solid_hal_0_5_14.patch

# powerdevil only autosuspends once/twice
Patch53: kdebase-workspace-4.3.4-powerdevil-kde#221637.patch
Patch54: kdebase-workspace-4.3.4-powerdevil-kde#221648.patch

# disable webkit
Patch55: kdebase-workspace-4.3.4-webkit.patch

# 4.3 branch
Patch100: kdebase-workspace-4.3.5.patch

# 4.4 branch
Patch200: kdebase-workspace-4.3.4-solid-crash.patch
# bz#593342, shows KDM background image on second head
Patch201: kdebase-workspace-4.3.4-kdm-rootimage.patch

# trunk

# security fixes
# CVE-2010-0436 kdm privilege escalation flaw 
Patch300: kdebase-workspace-4.3.4-kdm-CVE-2010-0436.patch

# moving to non-multilib hack
Obsoletes: kdebase-workspace < 4.3.0-2
Obsoletes: PolicyKit-kde < %{version}-%{release}
Obsoletes: polkit-qt < 0.10
Obsoletes: polkit-qt-examples < 0.10
Obsoletes: kdmtheme < 1.3

BuildRequires: akonadi-devel
BuildRequires: bluez-libs-devel
BuildRequires: ConsoleKit-devel
BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: kdelibs4-devel >= %{version}
BuildRequires: kdelibs-experimental-devel >= %{version}
BuildRequires: kdepimlibs-devel >= %{version}
BuildRequires: libutempter-devel
BuildRequires: libxklavier-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXres-devel
%ifnarch s390 s390x
BuildRequires: lm_sensors-devel
%endif
BuildRequires: NetworkManager-devel
BuildRequires: pam-devel
BuildRequires: qimageblitz-devel
BuildRequires: soprano-devel
BuildRequires: python-devel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

Requires: kdebase-runtime >= %{version}
Requires: ksysguardd = %{version}-%{release}
Requires: coreutils
Requires: dbus-x11
Requires: xorg-x11-apps
Requires: xorg-x11-utils
Requires: xorg-x11-server-utils
Requires: kio_sysinfo
Requires: %{name}-wallpapers = %{version}-%{release}
Requires: oxygen-cursor-themes = %{version}-%{release}
Requires: PolicyKit-authentication-agent
Requires: redhat-logos >= 60.0.2-1

%description
The KDE Workspace consists of what is the desktop of the
KDE Desktop Environment.

This package contains:
* khotkeys (a hotkey daemon)
* klipper (a cut & paste history utility)
* kmenuedit (the menu editor)
* krandrtray (resize and rotate X screens)
* krunner (a command run interface)
* ksysguard (a performance monitor)
* kwin (the window manager of KDE)
* kxkb (a utility to switch keyboard maps)
* plasma (the KDE desktop, panels and widgets workspace application)
* systemsettings (the configuration editor)

%package devel
Group: Development/Libraries
Summary:Development files for %{name}
Obsoletes: PolicyKit-kde-devel < 4.3.0
Obsoletes: polkit-qt-devel < 0.10
Provides: solid-bluetooth-devel = 4.3-0.1
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kdelibs4-devel

%description devel
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Group: System Environment/Libraries
Provides: solid-bluetooth = 4.3-0.1
Requires: kdelibs4%{?_isa} >= %{version}
Requires: %{name} = %{version}-%{release}

%description libs
%{summary}.

%package wallpapers
Summary: KDE wallpapers
Group: User Interface/Desktops
Requires: kde-filesystem
BuildArch: noarch

%description wallpapers
%{summary}.

%package -n kdm
Summary: The KDE login manager
group: User Interface/X
Provides: kdebase-kdm = %{version}-%{release}
Provides: service(graphical-login) = kdm
Requires: kdelibs4%{?_isa} >= %{version}
Requires: kde-settings-kdm

%description -n kdm
KDM provides the graphical login screen, shown shortly after boot up,
log out, and when user switching.

%package -n ksysguardd
Summary: Performance monitor daemon
Group:   System Environment/Daemons

%description -n ksysguardd
%{summary}.

%package -n oxygen-cursor-themes
Summary: Oxygen cursor themes
Group: User Interface/Desktops
BuildArch: noarch

%description -n oxygen-cursor-themes
%{summary}.

%package python-applet
Summary: Plasma widget in Python
Group: User Interface/Desktops
Provides: plasma-scriptengine-python = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: PyKDE4 >= %{version}

%description python-applet
%{summary}.

%package akonadi
Summary: Akonadi integration for KDE Workspace
Group: User Interface/Desktops
Provides: plasma-dataengine-akonadi = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: akonadi

%description akonadi
%{summary}.

%prep
%setup -q

%patch1 -p1 -b .redhat-startkde
%patch2 -p1 -b .plasma-konsole
%patch3 -p1 -b .show_systemsettings
%patch4 -p1 -b .ck-shutdown
%patch7 -p0 -b .krdb
%patch8 -p1 -b .klipper-url
%patch9 -p1 -b .rootprivs

%patch11 -p1 -b .font
%patch13 -p1 -b .pykde4
%patch15 -p1 -b .kio_sysinfo
%patch16 -p1 -b .showremainingtime
%patch17 -p1 -b .classicmenu-logout
%patch18 -p1 -b .kdm_plymouth
%patch19 -p1 -b .calendar-akonadi
%patch20 -p1 -b .missing_include
%patch21 -p1 -b .bz#567286
%patch50 -p1 -b .kde#171685
%patch51 -p1 -b .brightness_keys
%patch52 -p1 -b .solid_hal_0_5_14
%patch53 -p1 -b .kde#221637
%patch54 -p1 -b .kde#221648
%patch55 -p1 -b .nowebkit

# 4.3 branch
%patch100 -p1 -b .kde435

# 4.4 branch
%patch200 -p1 -b .solid_crash
%patch201 -p1 -b .kdm-rootimage

#security fixes
# CVE-2010-0436 kdm privilege escalation flaw
%patch300 -p1 -b .kdm-CVE-2010-0436

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  -DKDE4_KDM_PAM_SERVICE=kdm \
  -DKDE4_KCHECKPASS_PAM_SERVICE=kcheckpass \
  -DKDE4_KSCREENSAVER_PAM_SERVICE=kscreensaver \
  ..
popd

make -C %{_target_platform}

%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# xsession support
mkdir -p %{buildroot}%{_datadir}/xsessions/
mv %{buildroot}%{_kde4_appsdir}/kdm/sessions/kde.desktop %{buildroot}%{_datadir}/xsessions/kde.desktop

# remove the rest of useless xsession files
rm -rf %{buildroot}%{_kde4_appsdir}/kdm/sessions/

# nuke, use external kde-settings-kdm
rm -rf  %{buildroot}%{_kde4_configdir}/kdm

# unpackaged files
rm -fv %{buildroot}%{_kde4_libdir}/libpolkitkdeprivate*.so


%check
for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done


%clean
rm -rf %{buildroot}

%post
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
update-desktop-database -q &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
  touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :
  gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
  gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
  update-desktop-database -q &> /dev/null || :
fi

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_kde4_bindir}/kaccess                           
%{_kde4_bindir}/kapplymousetheme                  
%{_kde4_bindir}/kblankscrn.kss                    
%{_kde4_bindir}/kcheckrunning                     
%{_kde4_bindir}/kcminit                           
%{_kde4_bindir}/kcminit_startup                   
%{_kde4_bindir}/kdostartupconfig4                 
%{_kde4_bindir}/kfontinst
%{_kde4_bindir}/kfontview
%{_kde4_bindir}/klipper
%{_kde4_bindir}/kmenuedit
%{_kde4_bindir}/krandom.kss
%{_kde4_bindir}/krandrtray
%{_kde4_bindir}/krdb
%{_kde4_bindir}/krunner
%{_kde4_bindir}/ksmserver
%{_kde4_bindir}/ksplashsimple
%{_kde4_bindir}/ksplashx
%{_kde4_bindir}/ksplashx_scale
%{_kde4_bindir}/kstartupconfig4
%{_kde4_bindir}/ksysguard
%{_kde4_bindir}/ksystraycmd
%{_kde4_bindir}/kwin*
%{_kde4_bindir}/kxkb
%{_kde4_bindir}/plasma-desktop
%{_kde4_bindir}/plasma-overlay
%{_kde4_bindir}/plasmaengineexplorer
%{_kde4_bindir}/plasmoidviewer
%{_kde4_bindir}/plasmawallpaperviewer
%{_kde4_bindir}/safestartkde
%{_kde4_bindir}/setscheduler
%{_kde4_bindir}/solid-action-desktop-gen
%{_kde4_bindir}/solid-bluetooth
%{_kde4_bindir}/solid-network
%{_kde4_bindir}/solid-powermanagement
%{_kde4_bindir}/startkde
%{_kde4_bindir}/systemsettings

%{_kde4_appsdir}/color-schemes/
%{_kde4_appsdir}/desktoptheme/
%{_kde4_appsdir}/kaccess/
%{_kde4_appsdir}/kcminput/
%{_kde4_appsdir}/kcmkeys/
%{_kde4_appsdir}/kcmsolidactions/
%{_kde4_appsdir}/kconf_update/
%{_kde4_appsdir}/kcontrol/
%{_kde4_appsdir}/kdisplay/
%{_kde4_appsdir}/kfontinst/
%{_kde4_appsdir}/kfontview/
%{_kde4_appsdir}/khotkeys/
%{_kde4_appsdir}/kmenuedit/
%{_kde4_appsdir}/konqsidebartng/
%{_kde4_appsdir}/ksplash/
%{_kde4_appsdir}/ksysguard/
%{_kde4_appsdir}/kthememanager/
%{_kde4_appsdir}/kwin/
%{_kde4_appsdir}/kwrited/
%{_kde4_appsdir}/plasma/
#{_kde4_appsdir}/plasma_scriptengine_ruby/
%{_kde4_appsdir}/powerdevil/
%{_kde4_appsdir}/solid/
%{_kde4_appsdir}/solidfakenetbackend/
%{_kde4_appsdir}/systemsettings/

%{_kde4_configdir}/background.knsrc
%{_kde4_configdir}/colorschemes.knsrc
%{_kde4_configdir}/ksplash.knsrc
%{_kde4_configdir}/ksysguard.knsrc
%{_kde4_configdir}/plasma-overlayrc
%{_kde4_configdir}/plasma-themes.knsrc
%{_kde4_configdir}/wallpaper.knsrc

%{_kde4_datadir}/kde4/services/*
%exclude %{_kde4_datadir}/kde4/services/kdm.desktop
%{_kde4_datadir}/kde4/servicetypes/*
%{_kde4_datadir}/sounds/pop.wav
%{_kde4_datadir}/autostart/klipper.desktop
%{_kde4_datadir}/autostart/krunner.desktop
%{_kde4_datadir}/autostart/plasma.desktop
%{_kde4_datadir}/autostart/plasma-desktop.desktop
%{_kde4_datadir}/applications/kde4/*
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_kde4_datadir}/config.kcfg/*
%{_datadir}/xsessions/*.desktop
%{_kde4_docdir}/HTML/en/kcontrol/
%{_kde4_docdir}/HTML/en/klipper/
%{_kde4_docdir}/HTML/en/kmenuedit/
%{_kde4_docdir}/HTML/en/ksysguard/
%{_kde4_docdir}/HTML/en/kxkb/
%{_kde4_docdir}/HTML/en/plasma/
%{_kde4_docdir}/HTML/en/systemsettings/
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_iconsdir}/oxygen/*/*/*
%{_kde4_libdir}/kde4/classic_mode.so
%{_kde4_libdir}/kde4/fontthumbnail.so
%{_kde4_libdir}/kde4/icon_mode.so
%{_kde4_libdir}/kde4/ion_*.so
%{_kde4_libdir}/kde4/kcm_*.so
%exclude %{_kde4_libdir}/kde4/kcm_kdm.so
%{_kde4_libdir}/kde4/kded_*.so
%{_kde4_libdir}/kde4/kfontviewpart.so
%{_kde4_libdir}/kde4/kio_fonts.so
%{_kde4_libdir}/kde4/krunner_*.so
%{_kde4_libdir}/kde4/kstyle_keramik_config.so
%{_kde4_libdir}/kde4/kwin*_*.so
%{_kde4_libdir}/kde4/plasma_animator_default.so
%{_kde4_libdir}/kde4/plasma_applet_*.so
#{_kde4_libdir}/kde4/plasma_appletscriptengine_dashboard.so
#{_kde4_libdir}/kde4/plasma_appletscriptengine_webapplet.so
#{_kde4_libdir}/kde4/plasma_package*_*.so
%{_kde4_libdir}/kde4/plasma_containment_*.so
%{_kde4_libdir}/kde4/plasma_engine_*.so
%{_kde4_libdir}/kde4/plasma-geolocation-ip.so
%{_kde4_libdir}/kde4/plasma_wallpaper_*.so
%{_kde4_libdir}/kde4/solid_*.so
%{_kde4_libexecdir}/kcheckpass
%{_kde4_libexecdir}/kcmdatetimehelper
%{_kde4_libexecdir}/kfontprint
%{_kde4_libexecdir}/kio_fonts_helper
%{_kde4_libexecdir}/krootimage
%{_kde4_libexecdir}/kscreenlocker
%{_kde4_libexecdir}/test_kcm_xinerama
%{_libdir}/strigi/
%{_kde4_libdir}/libkdeinit*.so
%{_kde4_libdir}/libkickoff.so
%{_kde4_libdir}/libsystemsettingsview.so
%{_kde4_libdir}/kconf_update_bin/*
%{_mandir}/man1/plasmaengineexplorer.1*

# python widget
%exclude %{_kde4_datadir}/kde4/services/plasma-scriptengine*python.desktop

# akonadi
%exclude %{_kde4_libdir}/kde4/plasma_engine_akonadi.so
%exclude %{_kde4_datadir}/kde4/services/plasma-engine-akonadi.desktop

%files libs
%defattr(-,root,root,-)
%{_kde4_libdir}/lib*.so.*
%{_kde4_libdir}/libplasma_applet-system-monitor.so
%{_kde4_libdir}/kde4/plugins/designer/ksysguardwidgets.so
%{_kde4_libdir}/kde4/plugins/designer/ksysguardlsofwidgets.so

%files devel
%defattr(-,root,root,-)
%{_kde4_includedir}/*
%{_kde4_libdir}/lib*.so
%{_kde4_appsdir}/cmake/modules/*.cmake
%{_kde4_libdir}/cmake/KDE4Workspace-%{version}/
%exclude %{_kde4_libdir}/libkdeinit*.so
%exclude %{_kde4_libdir}/libkickoff.so
%exclude %{_kde4_libdir}/libplasma_applet-system-monitor.so
%exclude %{_kde4_libdir}/libsystemsettingsview.so

%files wallpapers
%defattr(-,root,root,-)
%{_kde4_datadir}/wallpapers/*

%files -n kdm
%defattr(-,root,root,-)
%{_kde4_bindir}/genkdmconf
%{_kde4_bindir}/kdm
%{_kde4_bindir}/kdmctl
%{_kde4_libdir}/kde4/kcm_kdm.so
%{_kde4_libexecdir}/kdm_config
%{_kde4_libexecdir}/kdm_greet
%{_kde4_libdir}/kde4/kgreet_*.so
%{_kde4_configdir}/kdm.knsrc
%{_kde4_docdir}/HTML/en/kdm/
%dir %{_kde4_appsdir}/doc
%{_kde4_appsdir}/doc/kdm/
%{_kde4_appsdir}/kdm/
%{_kde4_datadir}/kde4/services/kdm.desktop

%files -n ksysguardd
%defattr(-,root,root,-)
%config(noreplace) %{_kde4_sysconfdir}/ksysguarddrc
%{_kde4_bindir}/ksysguardd

%files -n oxygen-cursor-themes
%defattr(-,root,root,-)
%{_kde4_iconsdir}/Oxygen_Black/
%{_kde4_iconsdir}/Oxygen_Black_Big/
%{_kde4_iconsdir}/Oxygen_Blue/
%{_kde4_iconsdir}/Oxygen_Blue_Big/
%{_kde4_iconsdir}/Oxygen_White/
%{_kde4_iconsdir}/Oxygen_White_Big/
%{_kde4_iconsdir}/Oxygen_Yellow/
%{_kde4_iconsdir}/Oxygen_Yellow_Big/
%{_kde4_iconsdir}/Oxygen_Zion/
%{_kde4_iconsdir}/Oxygen_Zion_Big/

%files python-applet
%defattr(-,root,root,-)
%{python_sitearch}/PyKDE4/plasmascript.py*
%{_kde4_appsdir}/plasma_scriptengine_python
%{_kde4_datadir}/kde4/services/plasma-scriptengine*python.desktop

%files akonadi
%defattr(-,root,root,-)
%{_kde4_libdir}/kde4/plasma_engine_akonadi.so
%{_kde4_datadir}/kde4/services/plasma-engine-akonadi.desktop


%changelog
* Wed Jun 23 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.3.4-19
- Resolves: bz#593342, shows KDM background image on second head

* Tue Jun 01 2010 Than Ngo <than@redhat.com> - 4.3.4-18
- Resolves: bz#597271, drop WebKit support in Qt

* Wed Apr 14 2010 Than Ngo <than@redhat.com> - 4.3.4-17
- powerdevil only autosuspends once/twice

* Wed Apr 14 2010 Than Ngo <than@redhat.com> - 4.3.4-16
- Resolves: #570625, CVE-2010-0436, kdm privilege escalation flaw 

* Tue Mar 30 2010 Than Ngo <than@redhat.com> - 4.3.4-15
- rebuild against qt-4.6.2

* Tue Mar 30 2010 Than Ngo <than@redhat.com> - 4.3.4-14
- rebuild against qt-4.6.2
- Resolves: #567286, Anyone can change locked screen settings

* Wed Feb 17 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.3.4-13
- Resolves: bz#566017, KDE theme merged into redhat-logos
 
* Fri Feb 12 2010 Than Ngo <than@redhat.com> - 4.3.4-12
- Resolves: bz#563855, KDE cannot be started from GDM

* Fri Feb 12 2010 Than Ngo <than@redhat.com> - 4.3.4-11
- Resolves: bz#563855, KDE cannot be started from GDM

* Thu Feb 11 2010 Than Ngo <than@redhat.com> - 4.3.4-10
- Resolves: bz#563855, KDE cannot be started from GDM

* Mon Jan 25 2010 Than Ngo <than@redhat.com> - 4.3.4-9
- update theme to use the new wallpaper in PNG
- update Preview.png in ksplash to match new splash

* Fri Jan 22 2010 Than Ngo <than@redhat.com> - 4.3.4-8
- backport 4.3.5 fixes

* Thu Jan 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.3.4-7
- RHEL 6 KDE theme (#556528)

* Wed Jan 20 2010 Than Ngo <than@redhat.com> - 4.3.4-6
- do not link calendar data engine with Akonadi, move to main package (#552473)
- fix infinite recursion in the patch for #556643
- fix build problem in kdm

* Mon Jan 04 2010 Than Ngo <than@redhat.com> - 4.3.4-5
- fix crash in solid

* Mon Dec 14 2009 Than Ngo <than@redhat.com> - 4.3.4-4
- cleanup

* Mon Dec 14 2009 Rex Dieter <rdieter@fedoraproject.org> 4.3.4-3
- hal-0.5.14-1 and failures with brightness controls (#545258)

* Sun Dec 06 2009 Than Ngo <than@redhat.com> - 4.3.4-2
- fix conditional for RHEL

* Tue Dec 01 2009 Than Ngo <than@redhat.com> - 4.3.4-1
- 4.3.4
- kdm_plymouth patch (#475890)

* Tue Nov 24 2009 Rex Dieter <rdieter@fedoraproject.org> 4.3.3-7.1
- Requires: PolicyKit-authentication-agent unconditionally (ie, in F-12 too)

* Fri Nov 13 2009 Rex Dieter <rdieter@fedoraproject.org> 4.3.3-7
- kubuntu_101_brightness_fn_keys_and_osd.diff (#475247)

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-6
- rhel cleanup, fix conditional for RHEL

* Thu Nov 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-5
- fix logic on Requires: kdm  (ie, make F-12 builds not include it)

* Thu Nov 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-4
- try experimental patch for "keyboard stops working" (kde#171685)

* Wed Nov 11 2009 Than Ngo <than@redhat.com> - 4.3.3-3
- rhel cleanup, drop BR on libcaptury-devel

* Mon Nov 09 2009 Rex Dieter <rdieter@fedoraprojectg.org> - 4.3.3-2
- Obsoletes: polkit-qt-examples (f12+)
- -devel: Obsoletes: polkit-qt-devel (f12+)

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3
- BR: libXau-devel libXdmcp-devel

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.2-2
- drop Requires: oxygen-icon-theme (dep moved to kdebase-runtime)

* Sun Oct 04 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Sun Sep 27 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-9
- fix classicmenu-logout ("Leave...") patch

* Sun Sep 27 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-8
- support "Leave..." which brings up complete shutdown dialog in classic menu

* Fri Sep 25 2009 Than Ngo <than@redhat.com> - 4.3.1-7
- don't include googlegadgets on RHEL

* Thu Sep 24 2009 Than Ngo <than@redhat.com> - 4.3.1-6
- rhel cleanup

* Wed Sep 23 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.1-5
- fix spontaneous Plasma crashes due to uninitialized vars

* Mon Sep 14 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-4
- drop PolicyKit 0.9 support (PolicyKit-kde) on F12+/EL

* Sat Sep 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.1-3
- -python-applet: Provides: plasma-scriptengine-python
- Requires: system-ksplash-theme (f12+,rhel6+)

* Fri Sep 11 2009 Than Ngo <than@redhat.com> - 4.3.1-2
- drop  BR: lm_sensors-devel on s390(x)

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1
- drop Requires: kde-plasma-folderview, rely on comps instead

* Fri Aug 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.3.0-102
- Fix typo

* Thu Aug 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-101
- inflate Release tag, avoiding possible upgrade/obsoletes pain 
- -devel: drop Provides: PolicyKit-kde-devel, bump Obsoletes

* Thu Aug 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-12
- PolicyKit-kde subpkg (#519172, #519654)

* Wed Aug 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-11
- Requires: system-backgrounds-kde (f12+)

* Tue Aug 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-10
- Requires: kde-plasma-folderview

* Sun Aug 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-9
- -akonadi: move plasma_engine_calendar here
- drop Requires: kdm (F-12+)

* Wed Aug 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-8
- adjust default-applets patch to not load plasma-networkmanagement

* Tue Aug 18 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.0-7
- move akonadi stuff to subpackage

* Fri Aug 07 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-6
- Requires: oxygen-icon-theme >= 4.3.0

* Tue Aug 04 2009 Than Ngo <than@redhat.com> - 4.3.0-5
- respin

* Mon Aug 03 2009 Than Ngo <than@redhat.com> - 4.3.0-4
- respin

* Mon Aug 03 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.0-3
- show the remaining time in the battery plasmoid's popup (as in 4.2) (#515166)

* Sat Aug 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-2
- move designer plugins to -libs, fixes
  Multilib conflicts for index.cache.bz2 (#515088)
- tighten -libs deps, using %%{?_isa}
- %%check: desktop-file-validate

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Mon Jul 27 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.98-3
- backport forgotten method impl in Solid from 4.3 branch, r1000715

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Thu Jul 09 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Mon Jul 06 2009 Than Ngo <than@redhat.com> - 4.2.95-7
- plasma-desktop crashes when closing/opening windows (upstream patch)

* Fri Jul 03 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.95-6
- add kde-plasma-networkmanagement to the default panel if installed

* Wed Jul 01 2009 Michel Salim <salimma@fedoraproject.org> - 4.2.95-5
- rebuild (google-gadgets)

* Wed Jul 01 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.95-4
- rebuild (libxklavier)

* Mon Jun 29 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.95-3
- omit a few kdm bits from main pkg (#508647)

* Mon Jun 29 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.95-2
- port and reapply rootprivs (#434824) patch (#508593)
- fix internal version number (otherwise it mismatches with our file list)

* Fri Jun 26 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Thu Jun 18 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-3
- startkde: make MALLOC_CHECK opt-in (default off)

* Fri Jun 12 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-2
- bump Obsoletes: PolicyKit-kde

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Sun May 31 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.85-5
- make default_leonidas.png the default face icon on F11

* Sat May 30 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-4
- -devel:  exclude libkickoff.so, libsystemsettingsview.so
- drop old cmake crud

* Fri May 29 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-3
- omit/revert session-button patch (kde#194506,rh#502953)
- drop unused knotificationitem-1 patch

* Wed May 27 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-2
- upgrade path broken (F-11+), Obsoletes: guidance-power-manager (#502892)
- drop < F-10 crud, have_bluez3

* Mon May 11 2009 Than Ngo <than@redhat.com> 4.2.85-1
- 4.2.85
- Obsoletes/Provides: PolicyKit-kde(-devel)

* Wed May 06 2009 Than Ngo <than@redhat.com> - 4.2.3-2
- Requires: oxygen-icon-theme >= 4.2.2
- fix oxygen-cursor-themes noarch'ness

* Sun May 03 2009 Than Ngo <than@redhat.com> - 4.2.3-1
- 4.2.3

* Tue Apr 28 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-5
- #497657 -  kpackagekit/kopete notification misrendering/missing 
  buttons with qt-4.5.1

* Wed Apr 22 2009 Than Ngo <than@redhat.com> - 4.2.2-4
- dropp unused BR on libraw1394, it breaks the build on s390(x)

* Sun Apr 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-3
- Calendar standalone plasmoid on Desktop using 100% of CPU (kde#187699)

* Wed Apr 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-2
- optimize scriptlets
- drop upstreamed patches

* Mon Mar 30 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Mon Mar 23 2009 Than Ngo <than@redhat.com> - 4.2.1-12
- upstream patch to fix suspending issue

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-11
- Obsoletes: guidance-power-manager (-> powerdevil upgrade path, F-11+)

* Wed Mar 18 2009 Than Ngo <than@redhat.com> - 4.2.1-10
- upstream patch to fix MenuEntryActions created from khotkeys

* Mon Mar 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-9
- kdm subpkg
- -devel: move cmake modules here
- Requires: kdelibs4%%{?_isa} ..
- BR: libutempter-devel (drops need for kwrited helper)

* Thu Mar 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-8
- oxygen-cursor-themes: make noarch (f10+)

* Thu Mar 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-7
- fix quicklauch (kdebug#185585,rh#489769)
- -wallpapers: make noarch (f10+)

* Tue Mar 10 2009 Than Ngo <than@redhat.com> - 4.2.1-6
- fix konsole patch to use invokeTerminal

* Mon Mar  9 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.1-5
- fix pager not displaying desktop numbers (kdebug#184152)

* Mon Mar 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-4
- kde 4.2 update crashes plasma (kdebug#185736)

* Wed Mar 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-3
- move designer plugins to main/runtime (#487622)

* Tue Mar 03 2009 Than Ngo <than@redhat.com> - 4.2.1-2
- respin

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Thu Feb 26 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.2.0-17
- kio_sysinfo kick-off integration

* Tue Feb 24 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.2.0-16
- no klipper action on selection for Arora browser

* Fri Feb 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-15
- Provides: service(graphical-login) = kdm

* Fri Feb 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-14
- Requires: oxygen-icon-theme >= %%version

* Thu Feb 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-13
- dpms issues (kdebug#177123)

* Wed Feb 18 2009 Than Ngo <than@redhat.com> - 4.2.0-12
- drop the BR on PyKDE4, it's just needed for runtime
- python-applet subpackage

* Tue Feb 17 2009 Than Ngo <than@redhat.com> - 4.2.0-11
- googlegadgets subpackage

* Mon Feb 16 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-10
- fix shutdown dialog not centered, sometimes entirely off screen (kde#181199)

* Wed Feb 11 2009 Than Ngo <than@redhat.com> - 4.2.0-9
- fix kdm crash with Qt-4.5

* Mon Feb 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-8
- kickoff logout shuts down system (#484737, kdebug#180576)

* Sun Feb 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-7
- include awol rss dataengine, BR: kdepimlibs-devel (see also kdebug#179050)

* Fri Jan 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-4.2
- respin default_applets patch for kpowersave too (#483163)

* Thu Jan 29 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-4.1
- conditionalize bluetooth backport on F10+
- F9: revert solid-bluetooth to the version from KDE 4.1.4

* Thu Jan 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-4
- omit ldap hack (#457638), kde42's reduced linkage to the rescue

* Thu Jan 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-3
- Requires: PyKDE4 (for plasmascript bits)
- solid-bluetoothTrunkTo42.diff (bug #481801), and 
  +Provides: solid-bluetooth(-devel) = 4.3

* Wed Jan 28 2009 Than Ngo <than@redhat.com> - 4.2.0-2
- readd the patch that omist battery applet when guidance-power-manager is installed

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Fri Jan 16 2009 Than Ngo <than@redhat.com> - 4.1.96-4
- backport fix from trunk to allow symlinks in wallpaper theme

* Wed Jan 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.1.96-3
- BR: google-gadgets-devel > 0.10.5

* Fri Jan 09 2009 Than Ngo <than@redhat.com> - 4.1.96-2
- remove Provides: plasma-devel  

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Tue Dec 23 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.85-7
- Obsoletes: kpowersave (kpowersave -> powerdevil upgrade path, F-11+)

* Mon Dec 22 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.85-6
- (re)enable edje, google-gadget support

* Thu Dec 18 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.85-5
- drop BR edje-devel, we need QEdje instead, which we don't have yet
- comment out BR google-gadgets-* for now, need 0.10.4, have 0.10.3

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-4
- BR: edje-devel
- BR: google-gadgets-devel

* Tue Dec 16 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-3
- respun tarball

* Fri Dec 12 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-2
- BR: PyKDE4-devel >= %%version

* Thu Dec 11 2008 Than Ngo <than@redhat.com> -  4.1.85-1
- 4.2beta2

* Wed Dec 10 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.82-1
- 4.1.82
- rebase redhat-startkde patch

* Fri Dec 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-12
- move libplasma_applet-system-monitor.so from -devel to -libs (not a symlink)

* Fri Dec 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-11
- drop devel symlink (parallel -devel) hacks, not needed anymore in this package

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-10
- keep libtaskmanager.so in libdir

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-9
- keep libweather_ion.so in libdir

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-8
- keep libplasmaclock.so in libdir

* Mon Dec 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-7
- rebuild for Python 2.6

* Thu Nov 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-6
- disable Logitech mouse KCM again until #399931 is fixed

* Thu Nov 27 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-5
- use python_sitearch for x86_64 systems
- kephal seems to be disabled/removed, re-adapted file lists

* Tue Nov 25 2008 Than Ngo <than@redhat.com> 4.1.80-4
- respin

* Sun Nov 23 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-3
- rebase kdebase-workspace-4.1.1-show-systemsettings.patch
- new library: Kephal -> adapt file lists

* Wed Nov 19 2008 Than Ngo <than@redhat.com> 4.1.80-2
- merged
- drop kdebase-workspace-4.1.2-kdm-i18n.patch, it's included in upstream
- drop kdebase-workspace-4.0.85-plasma-default-wallpaper.patch, it's included in upstream
- drop kdebase-workspace-4.1.65-consolekit-kdm.patch
- add kdebase-workspace-4.1.80-session-button.patch
- add kdebase-workspace-4.1.2-ldap.patch

* Wed Nov 19 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-1
- 4.1.80
- BR cmake >= 2.6.2
- make install/fast
- drop _default_patch_fuzz 2
- rebase startkde patch
- rebase plasma-konsole patch
- rebase ck-shutdown patch
- add PyKDE4-devel, python-devel and PyQt4-devel to build plasma's python
  scripting interface
- BR google-gadgets-devel for google gadgets scriptengine
- BR libusb-devel for Logitech USB support in KControl

* Thu Nov 13 2008 Than Ngo <than@redhat.com> 4.1.3-5
- apply upstream patch to fix X crash when disabling compositing

* Wed Nov 12 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Fri Nov 07 2008 Than Ngo <than@redhat.com> 4.1.2-14
- only omit battery applet when guidance-power-manager is installed

* Fri Nov 07 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-13
- omit battery applet from default panel

* Wed Nov 05 2008 Than Ngo <than@redhat.com> 4.1.2-12
- fix i18n issue in kdm

* Tue Nov 04 2008 Than Ngo <than@redhat.com> 4.1.2-11
- add workaround for ldap issue (#457638)

* Sun Nov 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-10
- never touch PATH in startkde, prepending $QTDIR/bin is unnecessary on Fedora
  and breaks locating Qt 3 Assistant and other Qt 3 stuff (startkde gets run
  with a full path by KDM)

* Sat Nov 01 2008 Than Ngo <than@redhat.com> 4.1.2-9
- previous session button should be enabled

* Fri Oct 31 2008 Than Ngo <than@redhat.com> 4.1.2-8
- apply patch to fix multihead issue
- bz#469235, use non-blocking QProcess:startDetacted

* Sat Oct 25 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-7
- F10: use KDM default face icon from solar-kde-theme, require it

* Sat Oct 18 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-6
- reenable panel-autohide-fix-flicker patch
- backport revision 866998 to fix the CPU consumption problem (kde#172549)
- backport panelview.cpp coordinate fixes (revisions 869882, 869925, 870041)
- backport revision 871058 (request config sync when panel controller goes away)

* Fri Oct 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-5
- disable panel-autohide-fix-flicker patch for now, eats CPU

* Thu Oct 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-4
- backport panel autohide from 4.2 / plasma-4.1-openSUSE

* Wed Oct  8 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.2-3
- fix crash when invoking a klipper command for a second time

* Sun Sep 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-2
- make VERBOSE=1
- respin against new(er) kde-filesystem

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2

* Mon Sep 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.1-2
- show KCM icon in rootprivs patch (thanks to Harald Sitter "apachelogger")

* Thu Aug 28 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Mon Aug 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-8
- patch another place where systemsettings was hidden from the menu (#457739)

* Mon Aug 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-7
- enable KWin taskbarthumbnail effect (used by backported tooltip manager)

* Fri Aug 01 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-6
- patch to help krandr issues/crashes (kde#152914)

* Fri Aug 01 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.0-5
- fix 457479: "Run as root" dialog of kdm system settings is shown twice
  (due to activated signal being connected to twice)

* Fri Aug 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-4
- fix KDM configuration using the wrong appsdir for themes (#455623)

* Mon Jul 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-3
- respun tarball

* Sun Jul 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-2
- updated tooltip manager from 4.2 (fixes Plasma crash on theme change, #456820)

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Wed Jul 23 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-5
- F10+: fix circular kdebase<->kdebase-workspace dependency: don't Obsolete or
  Require kdebase, as kdebase now requires kdebase-workspace, obviating the
  upgrade path hack

* Tue Jul 22 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-4
- oxygen-cursor-themes, -wallpapers subpkgs

* Sat Jul 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-3
- BR soprano-devel (optional dependency of the Plasma Engine Explorer)

* Sat Jul 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-2
- backport Plasma tooltip manager from KDE 4.2 (fixes regression from 4.0)
  WARNING: Adds some new APIs from 4.2 (Plasma::popupPosition, Plasma::viewFor,
           Plasma::ToolTip*), use at your own risk, we have no control to
           guarantee that they will not change!

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-1
- 4.0.99

* Wed Jul 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-8
- fix KDM ConsoleKit patch to use x11-display-device instead of display-device

* Wed Jul 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-7
- fix segfault in KDM ConsoleKit patch (#455562)

* Tue Jul 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-6
- move systemsettings back from System to Settings in the menu

* Mon Jul 14 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-5
- new consolekit-kdm patch using libck-connector, BR ConsoleKit-devel (#430388)

* Mon Jul 14 2008 Rex Dieter <rdieter@fedorproject.org> 4.0.98-4
- install circles kdm theme

* Sun Jul 13 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-3
- sync kickoff-suspend patch from F9 (loads ksmserver translations)

* Fri Jul 11 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-2
- respun tarball (with systray patch)

* Thu Jul 10 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-1
- 4.0.98

* Wed Jul 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.85-3
- rewrite and reapply plasma-default-wallpaper patch
- (no more separate plasma-default-wallpaper-config part)
- rediff kde#154119 patch one last time

* Wed Jul 09 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-2
- systray icon patch (kde#164786)

* Sun Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-1
- 4.0.85

* Fri Jun 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-1
- 4.0.84

* Fri Jun 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.83-2
- port and apply kde#154119/kde#158301 patch for moving icons on panel (#439587)

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Tue Jun 17 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-2
- +Provides: kdm

* Sat Jun 14 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-1
- 4.0.82

* Wed Jun 04 2008 Than Ngo <than@redhat.com> 4.0.80-4
- fix #449881, ksysguard OnlyShowIn=KDE

* Tue Jun 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.80-3
- enable NetworkManager support, now compatible with NM 0.7

* Thu May 29 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.80-2
- BR: libcaptury-devel

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Wed May 21 2008 Than Ngo <than@redhat.com> 4.0.72-4
- fix #447030, hyperlinks do not open correctly in firefox

* Thu May 08 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.72-3
- ksysguardd subpkg (#426543)
- %%config(noreplace) systemsettingsrc

* Thu May 08 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.72-2
- gtkrc patch (rh#443309, kde#146779)

* Wed May 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.72-1
- update to 4.0.72
- update file list (Lorenzo Villani)
- port plasma-konsole, ck-shutdown, rootprivs, plasma-default-wallpaper patches
- remove NoDisplay=true in systemsettings onlyshowkde patch (still add
  OnlyShowIn=KDE), rename to show-systemsettings
- drop upstreamed suspend patch
- drop backported kde#155362 and menu-switch patches
- drop rh#443610 patch, "Zoom Out" should be working in 4.1
- disable kde#158301 patch for now (fails to apply, looks hard to port)

* Fri May 02 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.3-20
- Requires: kdebase , so it doesn't go missing on upgrades from kde3 (#444928)

* Mon Apr 28 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-19
- #444141: Initial wallpaper chooser has "EOS" preselected but wallpaper is "Fedora Waves"

* Sun Apr 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-18
- don't show "Zoom Out" toolbox action (#443610, patch from openSUSE branch)

* Sat Apr 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-17
- allow moving plasmoids on panels (#439587, kde#158301) (upstream patch)

* Fri Apr 18 2008 Than Ngo <than@redhat.com> 4.0.3-16
- fix #442559, Suspend/Hibernate issue on logout

* Tue Apr 15 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-15
- workaround #434824: KDE4 System Settings - No Method To Enter Administrative Mode
- fix #441062: packagekit tools do not show icons correctly on KDE

* Tue Apr 15 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.3-13
- update redhat-startkde.patch to match waves background color (#442312)

* Fri Apr 11 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-12
- allow to define a default wallpaper (plasmarc:wallpaper)

* Wed Apr 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-11
- read the default KSplash theme from kde-settings in startkde (#441565)

* Mon Apr 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-7
- own %%{_kde4_appsdir}/kdm/faces and set default user image (#441154)

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-6
- rebuild for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-5
- update file list for _kde4_libexecdir

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-4
- backport context menu switch between Kickoff and simple menu from 4.1

* Sat Mar 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- add support for shutdown/reboot through ConsoleKit >= 0.2.4 (#431817)

* Fri Mar 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- most of the kde#155362 patch has been merged, keep only the config part

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.2-9
- add onlyshowin=KDE for systemsetting

* Thu Mar 13 2008 Than Ngo <than@redhat.com> 4.0.2-8
- backport upstream patch to fix crash in kmenuedit when users
  delete entry and save it

* Wed Mar 12 2008 Than Ngo <than@redhat.com> 4.0.2-7
- apply upstream patch to fix changing wallpaper causes desktop to go white
- apply upstream patch to check whether the to-be-embedded window has been destroyed, (bz#437058)

* Mon Mar 10 2008 Than Ngo <than@redhat.com> 4.0.2-6
- add gestures=false in kde-settings, remove kdebase-workspace-4.0.2-Gestures.patch

* Thu Mar 06 2008 Than Ngo <than@redhat.com> 4.0.2-5
- typo fix

* Tue Mar 04 2008 Than Ngo <than@redhat.com> 4.0.2-4
- disable gestures as default
- add konsole in desktop menu

* Mon Mar 03 2008 Than Ngo <than@redhat.com> 4.0.2-3
- apply upstream patch to fix crash in khotkeys

* Fri Feb 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-2
- drop upstreamed kde#155974 patch
- update kde#155362 patch

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Mon Feb 25 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-8
- %%files: don't own %%_kde4_libdir/kde4/plugins (thanks wolfy!)

* Sat Feb 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-7
- omit broken disk space checking hunk from redhat-startkde patch (#426871)

* Wed Feb 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-6
- revert Conflicts, it matches against Provides from kdelibs3.

* Wed Feb 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-5
- Conflicts: kdelibs < 6:4 (temporary, to ease upgrade pain)
- -devel: Requires: %%name-libs

* Mon Feb 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-4
- backport enhancement to allow multi-line taskbar from 4.1 (kde#155974)

* Mon Feb 04 2008 Than Ngo <than@redhat.com> 4.0.1-3
- respin

* Fri Feb 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-2
- update kde#155362 (simple menu) patch for 4.0.1 (thanks to Jan Mette)

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-1
- 4.0.1

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-8
- respin (qt4)

* Sat Jan 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.0-7
- backport simple menu enhancement to show .desktop Name from 4.1 (kde#155362)

* Wed Jan 23 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-6
- Obsoletes: kdebase < 6:4

* Wed Jan 09 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-5
- initial login with white background (#428131, kde#155122)

* Wed Jan 09 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-4
- use upstream systemtray patch (#427442, kde#153193)

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-3
- respun tarball
- omit gtk_applet patch (for now, doesn't build)

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-2
- omit plasma-pager patch
- pull upstream patch to workaround gtk applet crasher (#427442)

* Mon Jan 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.0-1
- update to 4.0.0
- drop upstreamed creategtkrc-gtk212 patch
- update redhat-startkde and consolekit-kdm patches

* Mon Dec 31 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.97.0-5
- fix createGtkrc to set tooltip colors also for GTK+ 2.12+

* Sun Dec 30 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-4
- Obsoletes: kdmtheme

* Mon Dec 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.97.0-3
- Requires: coreutils dbus-x11 xorg-x11-apps xorg-x11-utils
            xorg-x11-server-utils (used in startkde)
- drop pam configs that were previously moved to kde-settings

* Tue Dec 11 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-2
- rebuild for changed _kde4_includedir

* Wed Dec 05 2007 Rex Dieter <rdieter[AT]fedoraprojec.torg. 3.97.0-1
- kde-3.97.0
- move pam configs to kde-settings
- Requires: kde-settings-kdm

* Tue Dec 04 2007 Than Ngo <than@redhat.com> 3.96.2-3
- fix kdm/kcheckpass/kscreensaver to get working

* Sat Dec 01 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.2-2
- BR: dbus-devel
- crystalsvg icons are not part of kdebase-workspace anymore
- make sure libkdeinit_plasma.so is in normal package

* Sat Dec 01 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.2-1
- kde-3.96.2

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.96.1-4
- Obsoletes and Provides kdebase-kdm for upgrades from old kde-redhat

* Fri Nov 30 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.96.1-3
- update and apply redhat-startkde patch
- update and apply KDM ConsoleKit patch (#228111, kde#147790)
- ConsoleKit patch also includes xdmcp fixes from Mandriva (#243560)

* Wed Nov 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.1-2
- %%doc README COPYING
- -libs subpkg
- -libs: Requires: kdelibs4
- don't remove libplasma.so from %%{_kde4_libdir}
- %%files: use %%_datadir for dbus-1/interfaces,xsessions

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.1-1
- kde-3.96.1

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-7
- use kde.desktop from /usr/share/apps/kdm/sessions/kde.desktop
- use %%config(noreplace) for /etc/ksysguarddrc
- Requires: kdebase, kdebase-runtime, oxygen-icon-theme
- fix url

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-6
- add patch to get pager in plasma bar
- re-added BR: libraw1394-devel

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-5
- leave libkworkspace.so for kate
- BR: kde-filesystem >= 4

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-4
- BR: libXtst-devel
- BR: libXScrnSaver-devel

* Fri Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-3
- own some more directories
- add %%defattr to package devel
- some spec cleanups
- -R: kdepimlibs-devel
- +BR: libXpm-devel
- +BR: glib2-devel (do we really need this?)

* Thu Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-2
- BR: libXxf86misc-devel
- BR: libXxf86misc-devel
- BR: libXcomposite-devel
- BR: bluez-libs-devel
- BR: libxklavier-devel
- BR: pam-devel
- BR: lm_sensors-devel
- BR: libXdamage-devel
- BR: libXv-devel
- BR: libXres-devel

* Wed Nov 14 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-1
- kde-3.96.0

* Wed Nov 14 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.95.2-1
- Initial version of kdebase-workspace
