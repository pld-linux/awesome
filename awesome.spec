# $Revision $, $Date: 2008-03-15 16:08:03 $
#
Summary:	Awesome Window Manager
Summary(pl.UTF-8):	Zarządca okien X - Awesome
Name:		awesome
Version:	2.1
Release:	0.1
License:	GPL v2
Group:		X11/Window Managers
Source0:	http://awesome.naquadah.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	def20d92c1af0352fd027889890e5844
Source1:	%{name}-xsession.desktop
URL:		http://awesome.naquadah.org/
BuildRequires:	asciidoc
#BuildRequires:	autoconf >= 2.59-9
#BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	doxygen
BuildRequires:	libconfuse-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
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
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}*
