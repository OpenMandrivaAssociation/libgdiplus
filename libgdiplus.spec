%define lib_major       0
%define libname        %mklibname gdiplus %{lib_major}
%define develname     %mklibname -d gdiplus

Name:		libgdiplus
Summary:	An Open Source implementation of the GDI+ API
Version:	2.10.9
Release:	1
License:	MIT
Group:		System/Libraries
URL:		http://go-mono.com
Source0:	http://www.go-mono.com/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		libgdiplus-2.10-libpng15.diff
Patch1:		libgdiplus-2.10.9-giflib5.patch

BuildRequires:	jpeg-devel
BuildRequires:	ungif-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libpng15)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xrender)

%description
An Open Source implementation of the GDI+ API.
This is part of the Mono project.

%package -n %{libname}
Summary:	An Open Source implementation of the GDI+ API
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
An Open Source implementation of the GDI+ API.
This is part of the Mono project.

%package -n %{develname}
Summary:	Libraries for developing with libgdiplus
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package provides the necessary development libraries to allow
you to develop with libgdiplus.

%prep
%setup -q
%patch0 -p0 -b .libpng15
%patch1 -p0 -b .giflib5

%build
export LIBS=' -lm -lX11 -lglib-2.0 '
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING
%{_libdir}/*.so.%{lib_major}*

%files -n %{develname}
%doc src/ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*



%changelog
* Fri Dec 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.10-5
+ Revision: 744713
- fixed typo
- rebuild
- converted BRs to pkgconfig provides
- cleaned up spec

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libtiff.so.5

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.10-3
+ Revision: 702716
- fix build against libpng15 (gentoo)

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.10-2
+ Revision: 662369
- mass rebuild

* Thu Feb 17 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.10-1
+ Revision: 638112
- update to new version 2.10

* Thu Dec 23 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.8.1-1mdv2011.0
+ Revision: 624034
- update build deps
- update to new version 2.8.1

* Thu Oct 07 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.8-1mdv2011.0
+ Revision: 583934
- new version
- drop patch

* Tue Aug 31 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.7-2mdv2011.0
+ Revision: 574878
- P0: security fix for CVE-2010-1526 (upstream)

* Tue Jul 20 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.7-1mdv2011.0
+ Revision: 555670
- update to new version 2.6.7

* Wed Apr 28 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.4-1mdv2010.1
+ Revision: 539980
- update to new version 2.6.4

* Tue Mar 16 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.2-1mdv2010.1
+ Revision: 521495
- update to new version 2.6.2

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6-2mdv2010.1
+ Revision: 488776
- rebuilt against libjpeg v8

* Tue Dec 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.6-1mdv2010.1
+ Revision: 478861
- update to new version 2.6

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 2.4.2-2mdv2010.0
+ Revision: 416620
- rebuilt against libjpeg v7

* Tue Jun 30 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.4.2-1mdv2010.0
+ Revision: 390911
- new version

* Fri Apr 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.4-1mdv2010.0
+ Revision: 368970
- new version

* Wed Jan 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.2-1mdv2009.1
+ Revision: 329389
- update to new version 2.2

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0-2mdv2009.1
+ Revision: 301475
- rebuilt against new libxcb

* Sat Oct 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.0-1mdv2009.1
+ Revision: 291911
- new version

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.9-2mdv2009.0
+ Revision: 264803
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Apr 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.9-1mdv2009.0
+ Revision: 192399
- new version

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.2.6-2mdv2008.1
+ Revision: 148502
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.6-1mdv2008.1
+ Revision: 119270
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - do not package big ChangeLog

* Thu Aug 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.5-1mdv2008.0
+ Revision: 75604
- new version
- new devel name
- fix buildrequires

* Wed May 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.4-1mdv2008.0
+ Revision: 27332
- new version
- fix buildrequires


* Wed Feb 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.3-1mdv2007.0
+ Revision: 116980
- new version

* Tue Dec 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.2-1mdv2007.1
+ Revision: 90712
- new version

* Wed Nov 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.1-1mdv2007.1
+ Revision: 86332
- new version

* Fri Nov 10 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.2-1mdv2007.1
+ Revision: 80515
- new version

* Tue Oct 17 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.18-1mdv2007.1
+ Revision: 65576
- Import libgdiplus

* Tue Oct 17 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.18-1mdv2007.1
- New version 1.1.18

* Thu Aug 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.17-1mdv2007.0
- New release 1.1.17

* Fri Jul 14 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.16.1-1
- New release 1.1.16.1

* Sat Jul 08 2006 Götz Waschk <waschk@mandriva.org> 1.1.16-1mdv2007.0
- drop patch
- New release 1.1.16

* Sat Jul 01 2006 Götz Waschk <waschk@mandriva.org> 1.1.15-2mdv2007.0
- disable -Werror

* Tue Apr 18 2006 Götz Waschk <waschk@mandriva.org> 1.1.15-1mdk
- fix source URL
- new version

* Tue Apr 04 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.14-1mdk
- New release 1.1.14

* Thu Mar 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.13.6-1mdk
- New release 1.1.13.6

* Sun Mar 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.13.4-1mdk
- New release 1.1.13.4

* Mon Jan 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.13.2-1mdk
- New release 1.1.13.2

* Wed Jan 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.13-1mdk
- New release 1.1.13

* Mon Dec 19 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.11-1mdk
- New release 1.1.11
- use mkrel

* Wed Nov 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.10-1mdk
- New release 1.1.10

* Thu Oct 13 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.9.2-1mdk
- New release 1.1.9.2

* Sat Sep 24 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.9.1-1mdk
- New release 1.1.9.1

* Sun Sep 11 2005 Götz Waschk <waschk@mandriva.org> 1.1.9-1mdk
- drop patch
- New release 1.1.9

* Fri Sep 02 2005 Götz Waschk <waschk@mandriva.org> 1.1.8-2mdk
- fix buildrequires

* Sat Jun 18 2005 Götz Waschk <waschk@mandriva.org> 1.1.8-1mdk
- source URL
- New release 1.1.8

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 1.1.7-1mdk
- New release 1.1.7

* Tue Mar 29 2005 Götz Waschk <waschk@linux-mandrake.com> 1.1.5-1mdk
- New release 1.1.5
- patch included for new glitz

* Thu Dec 09 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.0.5-1mdk
- New release 1.0.5

* Fri Nov 05 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.0.4-1mdk
- New release 1.0.4

* Thu Sep 23 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.2-1mdk
- fix source URL
- New release 1.0.2

* Thu Aug 12 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-1mdk
- new version

* Fri Jul 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-1mdk
- new version

* Thu Jun 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9-1mdk
- new version

* Thu Jun 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8-2mdk
- fix buildrequires
- provide libgdiplus in the library package

* Thu Jun 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8-1mdk
- new version

* Thu May 06 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- requires new cairo
- add more buildrequires
- new version

* Thu Apr 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2-3mdk
- fix buildrequires

* Thu Apr 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2-2mdk
- fix buildrequires

* Tue Apr 20 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2-1mdk
- autoconf 2.5 macro
- fix URL
- new version

