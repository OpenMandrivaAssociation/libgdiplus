%define lib_major       0
%define lib_name        %mklibname gdiplus %{lib_major}

Name:		libgdiplus
Summary:	An Open Source implementation of the GDI+ API
Version: 1.2.4
Release: %mkrel 1
License:	MIT
Group:		System/Libraries
URL:		http://go-mono.com
Source:		http://www.go-mono.com/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	cairo-devel >= 0.1.22
BuildRequires:	glitz-devel
BuildRequires:	glib2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libexif-devel
BuildRequires:	libungif-devel
BuildRequires:	libtiff-devel
BuildRequires:	automake1.8

%description
An Open Source implementation of the GDI+ API.
This is part of the Mono project.

%package -n %{lib_name}
Summary:	An Open Source implementation of the GDI+ API
Group:		System/Libraries
Provides:	%name = %version-%release

%description -n %{lib_name}
An Open Source implementation of the GDI+ API.
This is part of the Mono project.

%package -n %{lib_name}-devel
Summary:	Libraries for developing with libgdiplus
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{lib_name}-devel
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


%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}


%files -n %{lib_name}
%defattr(0644, root, root, 0755)
%doc AUTHORS COPYING src/ChangeLog
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(0644, root, root, 0755)
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.*a
%{_libdir}/pkgconfig/*


