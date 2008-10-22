#
Summary:	Awesome Window Manager
Summary(hu.UTF-8):	awesome ablakkezelő
Summary(pl.UTF-8):	Zarządca okien X - Awesome
Name:		awesome
Version:	3.0
Release:	3
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://awesome.naquadah.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	32bb9e94a63f421a7a8500f1041b6add
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-3.0-lua-files.patch
URL:		http://awesome.naquadah.org
BuildRequires:	asciidoc
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	gdk-pixbuf-devel
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
Suggests:	WallpaperChanger
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

%description plugin-beautiful
Theme library for awesome window manager

%description plugin-beautiful
Theme könyvtár az awesome ablakkezelőhöz


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
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}*
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
%dir %{_datadir}/awesome/lib
%{_datadir}/awesome/lib/awful.lua


%files plugin-beautiful
%defattr(644,root,root,755)
%dir %{_datadir}/awesome/lib
%dir %{_datadir}/awesome/themes/*
%{_datadir}/awesome/lib/beautiful.lua
%{_datadir}/awesome/themes


%files plugin-tabulous
%defattr(644,root,root,755)
%dir %{_datadir}/awesome/lib
%{_datadir}/awesome/lib/tabulous.lua
