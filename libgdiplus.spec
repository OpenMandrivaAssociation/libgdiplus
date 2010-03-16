%define lib_major       0
%define libname        %mklibname gdiplus %{lib_major}
%define libnamedev     %mklibname -d gdiplus

Name:		libgdiplus
Summary:	An Open Source implementation of the GDI+ API
Version: 2.6.2
Release: %mkrel 1
License:	MIT
Group:		System/Libraries
URL:		http://go-mono.com
Source:		http://www.go-mono.com/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
#BuildRequires:	cairo-devel >= 0.1.22
#BuildRequires:	glitz-devel
BuildRequires:	glib2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libexif-devel
BuildRequires:	libungif-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	libxrender-devel
BuildRequires:	libxml2-devel
BuildRequires:	libfontconfig-devel
BuildRequires:	automake1.8

%description
An Open Source implementation of the GDI+ API.
This is part of the Mono project.

%package -n %{libname}
Summary:	An Open Source implementation of the GDI+ API
Group:		System/Libraries
Provides:	%name = %version-%release

%description -n %{libname}
An Open Source implementation of the GDI+ API.
This is part of the Mono project.

%package -n %{libnamedev}
Summary:	Libraries for developing with libgdiplus
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d gdiplus 0

%description -n %{libnamedev}
This package provides the necessary development libraries to allow
you to develop with libgdiplus.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}


%files -n %{libname}
%defattr(0644, root, root, 0755)
%doc AUTHORS COPYING
%{_libdir}/*.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(0644, root, root, 0755)
%doc src/ChangeLog
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.*a
%{_libdir}/pkgconfig/*


