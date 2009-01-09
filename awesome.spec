#
Summary:	Awesome Window Manager
Summary(hu.UTF-8):	awesome ablakkezelő
Summary(pl.UTF-8):	Zarządca okien X - Awesome
Name:		awesome
Version:	3.1
Release:	0.1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://awesome.naquadah.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	e687a9c0056437207cbdba2f64412624
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-3.0-lua-files.patch
URL:		http://awesome.naquadah.org/
BuildRequires:	asciidoc
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	gperf
BuildRequires:	imlib2-devel
BuildRequires:	libev-devel
BuildRequires:	lua-doc
BuildRequires:	lua51-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	sed >= 4.0
BuildRequires:	xcb-util-devel >= 0.3
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

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
awesome jest menedżerem okien charakteryzującym się bardzo dużymi
możliwościami konfiguracji i rozszerzania fnkcjonalności, pozostając
przy tym szybki i lekki. Cel ten został osiągnięty dzięki wbudowaniu w
program języka skryptowego lua. Awesome został zaprojektowany z myślą
o bardziej zaawansowanych użytkonikach: programistach oraz innych
ludziach pracujących na codzień z komputerami, którzy chcą mieć dużą
kontrolę nad swoim środowiskiem graficznym.

%package doc
Summary:	awesome window manager API documentation
Summary(hu.UTF-8):	awesome ablakkezelő API dokumentációja
Summary(pl.UTF-8):	Dokumentacja API awesome
Group:		X11/Window Managers

%description doc
awesome window manager API documentation.

%description doc -l hu.UTF-8
awesome ablakkezelő API dokumentációja.

%description doc -l pl.UTF-8
Dokumentacja API menedżera okien awesome.

%package example-config
Summary:	Example config for awesome window manager
Summary(hu.UTF-8):	Egy alap/példa konfig az awesome ablakkezelőhöz
Group:		X11/Window Managers
Requires:	awesome-plugin-awful
Requires:	awesome-plugin-beautiful
Requires:	awesome-plugin-tabulous

%description example-config
Example config for awesome window manager. If you never used before
awesome 3.x window manager, it can be a good starting point.

%description example-config -l hu.UTF-8
Egy alap/példa konfig az awesome ablakkezelőhöz. Ha még sose
használtál awesome 3.x ablakkezelőt, jó kiindulópont lehet.

%package plugin-awful
Summary:	awful plugin for awesome window manager
Summary(hu.UTF-8):	awful plugin az awesome ablakkezelőhöz
Group:		X11/Window Managers

%description plugin-awful
AWesome Functions very UsefuL: awful plugin for awesome window manager

%description plugin-awful -l hu.UTF-8
AWesome Functions very UsefuL: awful plugin az awesome ablakkezelőhöz

%package plugin-beautiful
Summary:	theme library for awesome window manager
Summary(hu.UTF-8):	theme könyvtár az awesome ablakkezelőhöz
Group:		X11/Window Managers
Requires:	Esetroot
Requires:	habak

%description plugin-beautiful
Theme library for awesome window manager

%description plugin-beautiful
Theme könyvtár az awesome ablakkezelőhöz

%package plugin-invaders
Summary:	Awesome Invaders game
Summary(hu.UTF-8):	Awesome Invaders játék
Group:		X11/Window Managers
Requires:	%{name}-plugin-awful
Requires:	%{name}-plugin-beautiful
Requires:	ImageMagick

%description plugin-invaders
Awesome Invaders is, as the name says, an implementation of Space
Invaders using Awesome 3's Lua interface.

%description plugin-invaders -l hu.UTF-8
Awesome Invaders, ahogy a neve is mutatja, a Space Invaders
megvalósítása az awesome 3 lua interfészét használva.

%package plugin-naughty
Summary:	Naughty is a lua library that implements popup notifications for awesome3
Summary(hu.UTF-8):	Naughty egy lua-könyvtár, amely felugró értesítéseket tesz lehetővé awesome3-ban
Group:		X11/Window Managers
Requires:	%{name}-plugin-awful
Requires:	%{name}-plugin-beautiful

%description plugin-naughty
Naughty is a lua library that implements popup notifications for
awesome3.

%description plugin-naughty -l hu.UTF-8
Naughty egy lua-könyvtár, amely felugró értesítéseket tesz lehetővé
awesome3-ban.

%package plugin-revelation
Summary:	Revelation brings up a view of all your open clients
Summary(hu.UTF-8):	Revelation egy nézetet hoz létre az összes megnyitott kliensről
Group:		X11/Window Managers

%description plugin-revelation
Revelation brings up a view of all your open clients; left-clicking a
client pops to the first tag that client is visible on and
raises/focuses the client. In addition, the Enter key pops to the
currently focused client, and Escape aborts.

%description plugin-revelation -l hu.UTF-8
Revelation egy nézetet hoz létre az összes megnyitott kliensről; egy
kliensre bal gombbal kattintva az első olyan cimkére ugorhatsz, ahol a
kliens látható, és fókuszba hozza a klienst. Az Enter billentyűre a
fókuszban levő kliensre ugrik, és az Escape billentyűvel megszakítható
a művelet.

%package plugin-tabulous
Summary:	Fabulous tabs for awesome
Summary(hu.UTF-8):	Tab-ok awesome-hoz
Group:		X11/Window Managers

%description plugin-tabulous
Fabulous tabs for awesome

%description plugin-tabulous -l hu.UTF-8
Tab-ok awesome-hoz

%prep
%setup -q
%patch0 -p1

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
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_docdir}/%{name}-doc-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/luadoc $RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/luadoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-client
%attr(755,root,root) %{_bindir}/awsetbg
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/capi.lua
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/icons
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man1/awsetbg*
%{_mandir}/man5/%{name}*
%doc AUTHORS BUGS README STYLE

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}

%files example-config
%defattr(644,root,root,755)
%dir %{_sysconfdir}/xdg
%dir %{_sysconfdir}/xdg/awesome
%{_sysconfdir}/xdg/awesome/*

%files plugin-awful
%defattr(644,root,root,755)
%dir %{_datadir}/awesome/lib/awful
%{_datadir}/awesome/lib/awful/*.lua

%files plugin-beautiful
%defattr(644,root,root,755)
%dir %{_datadir}/awesome/themes/*
%{_datadir}/awesome/lib/beautiful.lua
%{_datadir}/awesome/themes

%files plugin-invaders
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/invaders.lua
%dir %{_datadir}/awesome/icons/invaders
%{_datadir}/awesome/icons/invaders/*.png

%files plugin-naughty
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/naughty.lua

%files plugin-revelation
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/revelation.lua

%files plugin-tabulous
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/tabulous.lua
