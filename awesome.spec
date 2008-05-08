# $Revision $, $Date: 2008-05-08 08:20:38 $
#
Summary:	Awesome Window Manager
Summary(pl.UTF-8):	Zarządca okien X - Awesome
Name:		awesome
Version:	2.3
Release:	0.1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://awesome.naquadah.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	9824bd7b150c991f5bac396102a9aea7
Source1:	%{name}-xsession.desktop
URL:		http://awesome.naquadah.org/
BuildRequires:	asciidoc
#BuildRequires:	autoconf >= 2.59-9
#BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	doxygen
BuildRequires:	imlib2-devel
BuildRequires:	libconfuse-devel
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{expand:%%define	_sysconfdir	%{_sysconfdir}/X11}
#%undefine	__cxx

%description
awesome is a floating and tiling window manager initialy based on a
dwm code rewriting. It's extremely fast, small, dynamic and awesome.

#%description -l pl.UTF-8

%prep
%setup -q
#%patch0 -p1

%build
#%{__libtoolize}
#%{__aclocal} -I m4
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure \
	--disable-static


%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README STYLE awesomerc
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-client
%attr(755,root,root) %{_bindir}/%{name}-menu
%attr(755,root,root) %{_bindir}/%{name}-message
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*
