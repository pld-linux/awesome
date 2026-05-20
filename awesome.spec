
Summary:	awesome window manager
Summary(hu.UTF-8):	awesome ablakkezelő
Summary(pl.UTF-8):	Zarządca okien X - Awesome
Name:		awesome
Version:	4.3
Release:	1
License:	GPL v2
Group:		X11/Window Managers
Source0:	https://github.com/awesomeWM/awesome/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	4d75cce54a86b6bbaa6e88a926cab5a7
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-lua51-docgen.patch
Patch1:		%{name}-fno-common.patch
URL:		https://awesomewm.org/
BuildRequires:	ImageMagick
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 3.0.0
BuildRequires:	dbus-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	glib2-devel >= 2.40
BuildRequires:	gobject-introspection-devel
BuildRequires:	ldoc
BuildRequires:	libxdg-basedir-devel >= 1.0.0
BuildRequires:	lua-lgi >= 0.8.0
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	ruby-asciidoctor
BuildRequires:	startup-notification-devel >= 0.10
BuildRequires:	tar >= 1:1.22
BuildRequires:	which
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-devel >= 0.3.8
BuildRequires:	xcb-util-keysyms-devel >= 0.3.4
BuildRequires:	xcb-util-wm-devel >= 0.3.8
BuildRequires:	xcb-util-xrm-devel >= 1.0
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.15
Requires:	dbus
Requires:	lua-lgi >= 0.8.0
Requires:	pango
Requires:	startup-notification >= 0.10
Provides:	awesome-plugin-awful
Provides:	awesome-plugin-beautiful
Provides:	awesome-plugin-naughty
Obsoletes:	awesome-doc < 4
Obsoletes:	awesome-plugin-awful
Obsoletes:	awesome-plugin-beautiful
Obsoletes:	awesome-plugin-invaders
Obsoletes:	awesome-plugin-naughty < 4
Obsoletes:	awesome-plugin-revelation
Obsoletes:	awesome-plugin-tabulous
Obsoletes:	awesome-plugin-telak
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
awesome is a highly configurable, next generation framework window
manager for X. It is very fast, light and extensible. It is primarly
targeted at power user, developer and any people dealing with every
day computing tasks and want to have fine-grained control on its
graphical environment.

%description -l hu.UTF-8
awesome egy végletekig beállítható, következő generációs ablakkezelő
az X-hez. Nagyon gyors, könnyed és bővíthető. Az elsődleges
célközönség a "power user"-ek, fejlesztők és bárki, aki minden nap
számítógéppel dolgozik és teljeskörű irányítást akar a grafikus
felületén.

%description -l pl.UTF-8
awesome jest zarządcą okien charakteryzującym się bardzo dużymi
możliwościami konfiguracji i rozszerzania funkcjonalności, pozostając
przy tym szybkim i lekkim. Cel ten został osiągnięty dzięki wbudowaniu
w program języka skryptowego lua. Awesome został zaprojektowany z
myślą o bardziej zaawansowanych użytkownikach: programistach oraz
innych pracujących na co dzień z komputerami, którzy chcą mieć dużą
kontrolę nad swoim środowiskiem graficznym.

%package client
Summary:	awesome window manager command line client
Summary(hu.UTF-8):	Parancssoros kliens az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Klient zarządcy okien awesome
Group:		X11/Window Managers/Tools
Requires:	dbus

%description client
awesome-client is command line utility (in fact shell script) for
executing an arbitrary lua code in working awesome window manager
instance.

%description client -l hu.UTF-8
awesome-client egy parancssoros eszköz (lényegében egy shell script)
tetszőleges lua kód futtatásához egy működő awesome ablakkezelőben.

%description client -l pl.UTF-8
awesome-client to skrypt powłoki pozwalający wykonać dowolny kod lua w
działającej instancji zarządcy okien awesome.

%package doc
Summary:	awesome window manager API documentation
Summary(hu.UTF-8):	awesome ablakkezelő API dokumentációja
Summary(pl.UTF-8):	Dokumentacja API zarządcy okien awesome
Group:		Documentation

%description doc
awesome window manager API documentation.

%description doc -l hu.UTF-8
awesome ablakkezelő API dokumentációja.

%description doc -l pl.UTF-8
Dokumentacja API zarządcy okien awesome.

%package example-config
Summary:	Example config for awesome window manager
Summary(hu.UTF-8):	Egy alap/példa konfig az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Przykładowy plik konfiguracyjny dla zarządcy okien awesome
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-themes-default = %{version}-%{release}

%description example-config
Example config for awesome window manager. It can be a good starting
point for those people, who have never used awesome window manager
before.

%description example-config -l hu.UTF-8
Egy alap/példa konfig az awesome ablakkezelőhöz. Ha még sose
használtál awesome 3.x ablakkezelőt, jó kiindulópont lehet.

%description example-config -l pl.UTF-8
Przykładowy plik konfiguracyjny dla zarządcy okien awesome. Ten plik
jest dobrym punktem wyjścia dla osób nie używających wcześniej awesome
3.x.

%package themes
Summary:	Themes for awesome window manager (metapackage)
Summary(hu.UTF-8):	Témák az awesome ablakkezelőhöz (metacsomag)
Summary(pl.UTF-8):	Motywy dla zarządcy okien awesome
Group:		X11/Window Managers/Tools
Requires:	%{name}-themes-default = %{version}-%{release}
Requires:	%{name}-themes-gtk = %{version}-%{release}
Requires:	%{name}-themes-sky = %{version}-%{release}
Requires:	%{name}-themes-xresources = %{version}-%{release}
Requires:	%{name}-themes-zenburn = %{version}-%{release}

%description themes
Themes for awesome window manager (metapackage).

%description themes -l hu.UTF-8
Témák az awesome ablakkezelőhöz (metacsomag).

%description themes -l pl.UTF-8
Dodatkowe motywy (definicje wyglądu) zarządcy okien awesome.

%package themes-default
Summary:	Default theme for awesome window manager
Summary(hu.UTF-8):	Alapértelmezett téma az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Domyślny motyw dla zarządcy okien awesome
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}

%description themes-default
Default theme for awesome window manager.

%description themes-default -l hu.UTF-8
Alapértelmezett téma az awesome ablakkezelőhöz.

%description themes-default -l pl.UTF-8
Domyślny motyw dla zarządcy okien awesome.

%package themes-gtk
Summary:	GTK theme for awesome window manager
Summary(pl.UTF-8):	Motyw GTK dla zarządcy okien awesome
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}

%description themes-gtk
GTK theme for awesome window manager.

%description themes-gtk -l pl.UTF-8
Motyw GTK dla zarządcy okien awesome.

%package themes-sky
Summary:	Sky theme for awesome window manager
Summary(hu.UTF-8):	Sky téma az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Motyw Sky dla zarządcy okien awesome
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}

%description themes-sky
Sky theme for awesome window manager.

%description themes-sky -l hu.UTF-8
Sky téma az awesome ablakkezelőhöz.

%description themes-sky -l pl.UTF-8
Motyw Sky dla zarządcy okien awesome.

%package themes-xresources
Summary:	Xresources theme for awesome window manager
Summary(pl.UTF-8):	Motyw Xresources dla zarządcy okien awesome
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}

%description themes-xresources
Xresources theme for awesome window manager.

%description themes-xresources -l pl.UTF-8
Motyw Xresources dla zarządcy okien awesome.

%package themes-zenburn
Summary:	Zenburn theme for awesome window manager
Summary(hu.UTF-8):	Zenburn téma az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Motyw Zenburn dla zarządcy okien awesome
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}

%description themes-zenburn
Zenburn theme for awesome window manager.

%description themes-zenburn -l hu.UTF-8
Zenburn téma az awesome ablakkezelőhöz.

%description themes-zenburn -l pl.UTF-8
Motyw Zenburn dla zarządcy okien awesome.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%cmake -B build \
	-DLUA_INCLUDE_DIR=%{_includedir}/lua5.1 \
	-DLUA_LIBRARY=%{_libdir}/liblua51.so \
	-DAWESOME_DOC_PATH=%{_docdir}/%{name}-%{version} \
	-DAWESOME_DATA_PATH=%{_datadir}/%{name} \
	-DSYSCONFDIR=%{_sysconfdir}
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_docdir}/%{name}-%{version}}
cp -p LICENSE docs/01-readme.md $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%{__sed} -i -e '1s,^#!.*env bash$,#!/bin/bash,' $RPM_BUILD_ROOT%{_bindir}/awesome-client

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%exclude %{_docdir}/%{name}-%{version}/doc
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/icons
%{_datadir}/xsessions/%{name}.desktop

%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/awesomerc.5*
%lang(de) %{_mandir}/de/man1/awesome.1*
%lang(de) %{_mandir}/de/man5/awesomerc.5*
%lang(es) %{_mandir}/es/man1/awesome.1*
%lang(es) %{_mandir}/es/man5/awesomerc.5*
%lang(fr) %{_mandir}/fr/man1/awesome.1*
%lang(fr) %{_mandir}/fr/man5/awesomerc.5*
%lang(it) %{_mandir}/it/man1/awesome.1*
%lang(it) %{_mandir}/it/man5/awesomerc.5*
%lang(ru) %{_mandir}/ru/man1/awesome.1*
%lang(ru) %{_mandir}/ru/man5/awesomerc.5*

# library modules
%dir %{_datadir}/%{name}/themes
%{_datadir}/%{name}/lib/awful
%{_datadir}/%{name}/lib/beautiful
%{_datadir}/%{name}/lib/beautiful.lua
%{_datadir}/%{name}/lib/gears
%{_datadir}/%{name}/lib/menubar
%{_datadir}/%{name}/lib/naughty
%{_datadir}/%{name}/lib/naughty.lua
%{_datadir}/%{name}/lib/wibox

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-client
%{_mandir}/man1/%{name}-client.1*
%lang(de) %{_mandir}/de/man1/awesome-client.1*
%lang(es) %{_mandir}/es/man1/awesome-client.1*
%lang(fr) %{_mandir}/fr/man1/awesome-client.1*
%lang(it) %{_mandir}/it/man1/awesome-client.1*
%lang(ru) %{_mandir}/ru/man1/awesome-client.1*

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/doc

%files example-config
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/awesome

%files themes
%defattr(644,root,root,755)

%files themes-default
%defattr(644,root,root,755)
%{_datadir}/awesome/themes/default

%files themes-gtk
%defattr(644,root,root,755)
%{_datadir}/awesome/themes/gtk

%files themes-sky
%defattr(644,root,root,755)
%{_datadir}/awesome/themes/sky

%files themes-xresources
%defattr(644,root,root,755)
%{_datadir}/awesome/themes/xresources

%files themes-zenburn
%defattr(644,root,root,755)
%{_datadir}/awesome/themes/zenburn
