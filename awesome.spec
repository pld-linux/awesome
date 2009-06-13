Summary:	awesome window manager
Summary(hu.UTF-8):	awesome ablakkezelő
Summary(pl.UTF-8):	Zarządca okien X - Awesome
Name:		awesome
Version:	3.3
Release:	5
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://awesome.naquadah.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	0dc5574dc551c6356d8cddc6ce91739c
Source1:	%{name}-xsession.desktop
Patch0:		%{name}-3.0-lua-files.patch
Patch1:		%{name}-client-bashizm.patch
URL:		http://awesome.naquadah.org/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	asciidoc
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	glib-devel
BuildRequires:	glib2-devel
BuildRequires:	gperf
BuildRequires:	imlib2-devel
BuildRequires:	libev-devel
BuildRequires:	libxdg-basedir-devel >= 1.0.1
BuildRequires:	lua-doc
BuildRequires:	lua51-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= 0.10
BuildRequires:	xcb-util-devel >= 0.3.5
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
Requires:	dbus
Requires:	rlwrap
Requires:	startup-notification >= 0.10
Requires:	xcb-util >= 0.3.5
Suggests:	%{name}-plugin-awful = %{version}-%{release}
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
awesome jest zarządcą okien charakteryzującym się bardzo dużymi
możliwościami konfiguracji i rozszerzania funkcjonalności, pozostając
przy tym szybkim i lekkim. Cel ten został osiągnięty dzięki wbudowaniu
w program języka skryptowego lua. Awesome został zaprojektowany z
myślą o bardziej zaawansowanych użytkownikach: programistach oraz
innych pracujących na codzień z komputerami, którzy chcą mieć dużą
kontrolę nad swoim środowiskiem graficznym.

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
Requires:	%{name}-plugin-awful = %{version}-%{release}
Requires:	%{name}-plugin-beautiful = %{version}-%{release}
Requires:	%{name}-plugin-tabulous = %{version}-%{release}
Requires:	%{name}-themes = %{version}-%{release}

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

%package plugin-awful
Summary:	awful plugin for awesome window manager
Summary(hu.UTF-8):	awful plugin az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Wtyczka awful dla zarządcy okien awesome
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}

%description plugin-awful
AWesome Functions very UsefuL: awful plugin for awesome window
manager.

%description plugin-awful -l hu.UTF-8
AWesome Functions very UsefuL: awful plugin az awesome ablakkezelőhöz.

%description plugin-awful -l pl.UTF-8
AWesome Functions very UsefuL: wtyczka awful dla zarządcy okien
awesome.

%package plugin-beautiful
Summary:	Theme library for awesome window manager
Summary(hu.UTF-8):	Theme könyvtár az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Biblioteka styli dla zarządcy okien awesome
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}
Suggests:	WallpaperChanger

%description plugin-beautiful
Theme library for awesome window manager.

%description plugin-beautiful -l hu.UTF-8
Theme könyvtár az awesome ablakkezelőhöz.

%description plugin-beautiful -l pl.UTF-8
Biblioteka styli dla zarządcy okien awesome.

%package plugin-invaders
Summary:	Awesome Invaders game
Summary(hu.UTF-8):	Awesome Invaders játék
Summary(pl.UTF-8):	Gra Awesome Invaders
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugin-awful = %{version}-%{release}
Requires:	%{name}-plugin-beautiful = %{version}-%{release}
Requires:	ImageMagick

%description plugin-invaders
Awesome Invaders is, as the name says, an implementation of Space
Invaders using awesome 3's Lua interface.

%description plugin-invaders -l hu.UTF-8
Awesome Invaders, ahogy a neve is mutatja, a Space Invaders
megvalósítása az awesome 3 lua interfészét használva.

%description plugin-invaders -l pl.UTF-8
Awesome Invaders jest grą Space Invaders zaimplementowaną w intefejsie
Lua zarządcy okien awesome 3.

%package plugin-naughty
Summary:	Naughty is a lua library that implements popup notifications for awesome 3
Summary(hu.UTF-8):	Naughty egy lua-könyvtár, amely felugró értesítéseket tesz lehetővé awesome3-ban
Summary(pl.UTF-8):	Powiadomienia w postaci wyskakujących okienek dla awesome 3
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugin-awful = %{version}-%{release}
Requires:	%{name}-plugin-beautiful = %{version}-%{release}

%description plugin-naughty
Naughty is a lua library that implements popup notifications for
awesome3.

%description plugin-naughty -l hu.UTF-8
Naughty egy lua-könyvtár, amely felugró értesítéseket tesz lehetővé
awesome3-ban.

%description plugin-naughty -l pl.UTF-8
Biblioteka lua dla zarządcy okien awesome 3 implementująca
powiadomienia w formie wyskakujących okienek.

%package plugin-revelation
Summary:	Plugin that allows to bring a view of all your open clients
Summary(hu.UTF-8):	Revelation egy nézetet hoz létre az összes megnyitott kliensről
Summary(pl.UTF-8):	Wtyczka do awesome 3 dająca widok wszystkich otwartych okien
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}

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

%description plugin-revelation -l pl.UTF-8
Revelation umożliwia podgląd wszystkich otwartych okien. Kliknięcie
prawym przyciskiem myszy na okienko przełącza na pierwszy znacznik, na
którym okno jest widoczne i przywołuje okno na pierwszy plan.
Dodatkowo klawisz Enter przełącza fokus mięszy oknami a klawisz Esc
przerywa podgląd okien.

%package plugin-tabulous
Summary:	Fabulous tabs for awesome window manager
Summary(hu.UTF-8):	Tab-ok awesome-hoz
Summary(pl.UTF-8):	Zakładki dla zarządcy okien awesome
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}

%description plugin-tabulous
Fabulous tabs for awesome.

%description plugin-tabulous -l hu.UTF-8
Tab-ok awesome-hoz.

%description plugin-tabulous -l pl.UTF-8
Zakładki dla zarządcy okien awesome.

%package plugin-telak
Summary:	Root window image display library
Summary(hu.UTF-8):	Root ablak kezeléséhez könyvtár
Summary(pl.UTF-8):	Biblioteka pozwlająca ustawić tapetę w głównym oknie
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}
Requires:	lua-socket

%description plugin-telak
Root window image display library.

%description plugin-telak -l hu.UTF-8
Root ablak kezeléséhez könyvtár.

%description plugin-telak -l pl.UTF-8
Biblioteka pozwalająca ustawić tapetę wyświetlaną na głównym oknie.

%package themes
Summary:	Themes for awesome window manager
Summary(hu.UTF-8):	Témák az awesome ablakkezelőhöz
Summary(pl.UTF-8):	Tematy dla zarządcy okien awesome
Group:		X11/Window Managers
Requires:	%{name} = %{version}-%{release}

%description themes
Themes for awesome window manager.

%description themes -l hu.UTF-8
Témák az awesome ablakkezelőhöz.

%description themes -l pl.UTF-8
Dodatkowe "tematy" (definicje wyglądu) zarządcy okien awesome.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%attr(755,root,root) %{_bindir}/%{name}-client
%attr(755,root,root) %{_bindir}/awsetbg
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/capi.lua
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icons
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man1/awsetbg*
%{_mandir}/man5/%{name}*

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/luadoc

%files example-config
%defattr(644,root,root,755)
%dir %{_sysconfdir}/xdg
%dir %{_sysconfdir}/xdg/awesome
%{_sysconfdir}/xdg/awesome/*

%files plugin-awful
%defattr(644,root,root,755)
%dir %{_datadir}/awesome/lib/awful
%{_datadir}/awesome/lib/awful/*.lua
%{_datadir}/awesome/lib/awful/layout
%{_datadir}/awesome/lib/awful/widget

%files plugin-beautiful
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/beautiful.lua
%{_datadir}/awesome/themes

%files themes
%defattr(644,root,root,755)
%dir %{_datadir}/awesome/themes
%{_datadir}/awesome/themes/default
%{_datadir}/awesome/themes/sky

%files plugin-invaders
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/invaders.lua
%dir %{_datadir}/awesome/icons/invaders
%{_datadir}/awesome/icons/invaders/*.png

%files plugin-naughty
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/naughty.lua

# %files plugin-revelation
# %defattr(644,root,root,755)
# %{_datadir}/awesome/lib/revelation.lua

%files plugin-tabulous
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/tabulous.lua

%files plugin-telak
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/telak.lua
