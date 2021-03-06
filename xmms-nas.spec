%define name xmms-nas
%define version 0.2
%define release %mkrel 10

Summary: NAS Output plugin for XMMS
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+
Group: Sound
URL: ftp://ftp.stack.nl/pub/users/willem/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: xmms
BuildRequires: xmms-devel
BuildRequires: nas-devel

%description
This is an audio output plugin for XMMS for the NAS sound system.

%prep
%setup -q
autoreconf -fi

%build
%define _disable_ld_no_undefined 1
%configure2_5x
touch config.h
%make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 .libs/libnas.so %buildroot%_libdir/xmms/Output/libnas.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/xmms/Output/libnas.so


