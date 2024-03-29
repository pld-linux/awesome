
Summary:	awesome window manager
Summary(hu.UTF-8):	awesome ablakkezelő
Summary(pl.UTF-8):	Zarządca okien X - Awesome
Name:		awesome
Version:	3.4.12
Release:	4
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://awesome.naquadah.org/download/%{name}-%{version}.tar.xz
# Source0-md5:	2c3490b820a19c044290027e6f2eb6c8
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-3.0-lua-files.patch
Patch1:		%{name}-magnifier.patch
Patch2:		normalize-icon-path-names.patch
Patch3:		xcb-util.patch
URL:		http://awesome.naquadah.org/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	asciidoc
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	dbus-devel
BuildRequires:	docbook-dtd45-xml
BuildRequires:	glib2-devel
BuildRequires:	gperf
BuildRequires:	imlib2-devel
BuildRequires:	libev-devel >= 4.0
BuildRequires:	libxdg-basedir-devel >= 1.0.1
BuildRequires:	lua-doc
BuildRequires:	lua51-devel
BuildRequires:	pango-devel >= 1:1.19.3
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.10
BuildRequires:	tar >= 1:1.22
BuildRequires:	which
BuildRequires:	xcb-util-image-devel >= 0.3.8
BuildRequires:	xcb-util-keysyms-devel >= 0.3.8
BuildRequires:	xcb-util-wm-devel >= 0.3.8
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.15
Requires:	pango >= 1:1.19.3
Requires:	startup-notification >= 0.10
Requires:	xcb-util >= 0.3.6
Provides:	awesome-plugin-awful
Provides:	awesome-plugin-beautiful
Obsoletes:	awesome-plugin-awful
Obsoletes:	awesome-plugin-beautiful
Obsoletes:	awesome-plugin-invaders
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
Requires:	rlwrap

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
Summary(pl.UTF-8):	Dokumentacja API awesome
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

%package plugin-naughty
Summary:	Naughty is a lua library that implements popup notifications for awesome 3
Summary(hu.UTF-8):	Naughty egy lua-könyvtár, amely felugró értesítéseket tesz lehetővé awesome3-ban
Summary(pl.UTF-8):	Powiadomienia w postaci wyskakujących okienek dla awesome 3
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{version}-%{release}
Provides:	dbus(org.freedesktop.Notifications)

%description plugin-naughty
Naughty is a lua library that implements popup notifications for
awesome3.

%description plugin-naughty -l hu.UTF-8
Naughty egy lua-könyvtár, amely felugró értesítéseket tesz lehetővé
awesome3-ban.

%description plugin-naughty -l pl.UTF-8
Biblioteka lua dla zarządcy okien awesome 3 implementująca
powiadomienia w formie wyskakujących okienek.

%package themes
Summary:	Themes for awesome window manager (metapackage)
Summary(hu.UTF-8):	Témák az awesome ablakkezelőhöz (metacsomag)
Summary(pl.UTF-8):	Motywy dla zarządcy okien awesome
Group:		X11/Window Managers/Tools
Requires:	%{name}-themes-default = %{version}-%{release}
Requires:	%{name}-themes-sky = %{version}-%{release}
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
%patch0 -p1
%patch1 -p1
# %patch2 -p1
# %patch3 -p1

%build
%cmake \
	-DLUA_INC_DIR=%{_includedir}/lua51 \
	-DPREFIX=%{_prefix} \
	-DAWESOME_DOC_PATH=%{_docdir}/%{name}-%{version} \
	-DAWESOME_DATA_PATH=%{_datadir}/%{name} \
	-DSYSCONFDIR=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_docdir}/%{name}-%{version}}
install AUTHORS BUGS README STYLE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

for file in $(%{__find} $RPM_BUILD_ROOT%{_datadir}/%{name} -iname "*.in"); do
	%{__rm} ${file}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%exclude %{_docdir}/%{name}-%{version}/luadoc
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/awsetbg
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/icons
%{_datadir}/xsessions/%{name}.desktop

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/awsetbg.1*
%{_mandir}/man5/awesomerc.5*
# de
%lang(de) %{_mandir}/de/man1/awesome.1*
%lang(de) %{_mandir}/de/man1/awsetbg.1*
%lang(de) %{_mandir}/de/man5/awesomerc.5*
# es
%lang(es) %{_mandir}/es/man1/awesome.1*
%lang(es) %{_mandir}/es/man1/awsetbg.1*
%lang(es) %{_mandir}/es/man5/awesomerc.5*
# fr
%lang(fr) %{_mandir}/fr/man1/awesome.1*
%lang(fr) %{_mandir}/fr/man1/awsetbg.1*
%lang(fr) %{_mandir}/fr/man5/awesomerc.5*
# it
%lang(it) %{_mandir}/it/man1/awesome.1*
%lang(it) %{_mandir}/it/man1/awsetbg.1*
%lang(it) %{_mandir}/it/man5/awesomerc.5*
# ru
%lang(ru) %{_mandir}/ru/man1/awesome.1*
%lang(ru) %{_mandir}/ru/man1/awsetbg.1*
%lang(ru) %{_mandir}/ru/man5/awesomerc.5*

# plugin-awful
%dir %{_datadir}/awesome/lib/awful
%{_datadir}/awesome/lib/awful/*.lua
%{_datadir}/awesome/lib/awful/layout
%{_datadir}/awesome/lib/awful/mouse
%{_datadir}/awesome/lib/awful/widget

# plugin-beautiful
%dir %{_datadir}/awesome/themes
%{_datadir}/awesome/lib/beautiful.lua

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
%doc %{_docdir}/%{name}-%{version}/luadoc

%files example-config
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/awesome

%files themes
%defattr(644,root,root,755)

%files themes-default
%defattr(644,root,root,755)
%{_datadir}/awesome/themes/default

%files themes-sky
%defattr(644,root,root,755)
%{_datadir}/awesome/themes/sky

%files themes-zenburn
%defattr(644,root,root,755)
%{_datadir}/awesome/themes/zenburn

%files plugin-naughty
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/naughty.lua
