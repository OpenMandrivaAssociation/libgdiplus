%define major	0
%define libname	%mklibname gdiplus %{major}
%define devname	%mklibname -d gdiplus
%define _disable_rebuild_configure 1

Summary:	An Open Source implementation of the GDI+ API
Name:		libgdiplus
Version:	6.0.5
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://go-mono.com
Source0:	http://download.mono-project.com/sources/libgdiplus/%{name}0-%{version}.tar.gz
Patch0:		libgdiplus-2.10.9-gold.patch
#Patch1:		libgdiplus-5.6-x11linkage.patch
BuildRequires:	jpeg-devel
BuildRequires:	ungif-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(x11)

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

%package -n %{devname}
Summary:	Libraries for developing with libgdiplus
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the necessary development libraries to allow
you to develop with libgdiplus.

%prep
%setup -q
%autopatch -p1

aclocal
libtoolize -fic
autoheader
automake -acf
autoconf

%build
export LIBS='-lm'
%configure \
	--disable-static
%make_build

%install
%make_install

# make sure pkgconfig(libgdiplus) is provided, fix this in 2.10.9:
sed -i -e 's|-L${libjpeg_prefix}/lib||g' %{buildroot}%{_libdir}/pkgconfig/libgdiplus.pc

%files -n %{libname}
%{_libdir}/libgdiplus.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

