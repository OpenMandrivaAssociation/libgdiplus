%define lib_major       0
%define libname        %mklibname gdiplus %{lib_major}
%define develname     %mklibname -d gdiplus

Name:		libgdiplus
Summary:	An Open Source implementation of the GDI+ API
Version:	2.10
Release:	5
License:	MIT
Group:		System/Libraries
URL:		http://go-mono.com
Source0:	http://www.go-mono.com/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		libgdiplus-2.10-libpng15.diff

BuildRequires:	jpeg-devel
BuildRequires:	libungif-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libexif
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
Obsoletes:	%mklibname -d gdiplus 0

%description -n %{develname}
This package provides the necessary development libraries to allow
you to develop with libgdiplus.

%prep
%setup -q
%patch0 -p0 -b .libpng15

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall

%files -n %{libname}
%doc AUTHORS COPYING
%{_libdir}/*.so.%{lib_major}*

%files -n %{develname}
%doc src/ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

