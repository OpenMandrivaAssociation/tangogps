%define name tangogps
%define version 0.99.4
%define release %mkrel 2

Summary: User friendly map and GPS software
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.tangogps.org/downloads/%{name}-%{version}.tar.gz
Patch1: tangogps-0.9.6-docdir.patch
License: GPLv2
Group: Networking/Other
Url: http://www.tangogps.org/gps/cat/About
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: curl-devel
BuildRequires: dbus-glib-devel
BuildRequires: gtk2-devel
BuildRequires: libexif-devel
BuildRequires: libGConf2-devel
BuildRequires: sqlite3-devel
BuildRequires: libsoup-devel
BuildRequires: bluez-devel

%description
tangogps is an easy to use, fast and lightweight mapping application
for use with or without GPS.
By default tangoGPS uses map data from the Openstreetmap
project. Additionally a variety of other repositories can be easily
added.
The maps are automagically downloaded and cached for offline use while
you drag or zoom the map. Furthermore you can conveniently pre-cache
areas with tangoGPS.

%prep
%setup -q
%patch1 -p1 -b .docdir

%build
autoreconf
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%docdir %{_docdir}/%{name}
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.png
