%define major	0
%define libname	%mklibname gdiplus %{major}
%define devname	%mklibname -d gdiplus

Summary:	An Open Source implementation of the GDI+ API
Name:		libgdiplus
Version:	2.10.9
Release:	4
License:	MIT
Group:		System/Libraries
Url:		http://go-mono.com
Source0:	http://www.go-mono.com/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		libgdiplus-2.10-libpng15.diff
Patch1:		libgdiplus-2.10.9-giflib5.patch
Patch2:		libgdiplus-2.10.9-gold.patch
Patch3:		libgdiplus-2.10.9-automake-1.13.patch
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
%apply_patches

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
%makeinstall_std

# make sure pkgconfig(libgdiplus) is provided, fix this in 2.10.9:
sed -i -e 's|-L${libjpeg_prefix}/lib||g' %{buildroot}%{_libdir}/pkgconfig/libgdiplus.pc

%files -n %{libname}
%{_libdir}/libgdiplus.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING src/ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

