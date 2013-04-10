%define lib_major       0
%define libname        %mklibname gdiplus %{lib_major}
%define develname     %mklibname -d gdiplus

Name:		libgdiplus
Summary:	An Open Source implementation of the GDI+ API
Version:	2.10.9
Release:	2
License:	MIT
Group:		System/Libraries
URL:		http://go-mono.com
Source0:	http://www.go-mono.com/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		libgdiplus-2.10-libpng15.diff
Patch1:		libgdiplus-2.10.9-giflib5.patch
Patch2:		libgdiplus-2.10.9-gold.patch
Patch3:		libgdiplus-2.10.9-automake-1.13.patch
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
BuildRequires:	automake
BuildRequires:	cairo-devel

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
%patch2 -p1 -b .gold
%patch3 -p1 -b .automake113

aclocal
libtoolize -fic
autoheader
automake -acf
autoconf

%build
export LIBS='-lm'
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
%{_libdir}/pkgconfig/*.pc


