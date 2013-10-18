Summary:	Stopwatch and timer for GNOME 3
Name:		gnome-clocks
Version:	3.10.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-clocks/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	f2994d78aff438a51f0d13b0d1ecdaac
URL:		https://live.gnome.org/Design/Apps/Documents
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	geocode-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	intltool
BuildRequires:	libgweather-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	hicolor-icon-theme
Requires:	libgweather-data
Requires:	geoclue2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnome-clocks

%description
A simple and elegant clock application. It includes world clocks,
alarms, a stopwatch and a timer.

%prep
%setup -q

# kill gnome common deps
%{__sed} -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-clocks
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-clocks
%{_desktopdir}/gnome-clocks.desktop
%{_iconsdir}/hicolor/*/*/*.png

