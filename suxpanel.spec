#
#TODO	FHS
#
Summary:	suxpanel - MacOS-style panel
Summary(pl):	suxpanel - panel w stylu MacOS
Name:		suxpanel
Version:	0.3
Release:	0.1
License:	GPL
Group:		-
Source0:	http://www.linuxmag.com.br/~leandro/suxpanel/%{name}-%{version}.tar.bz2
# Source0-md5:	1fa0bc9d8ea0f782826f4f93da6406c3
URL:		http://www.linuxmag.com.br/~leandro/suxpanel/
BuildRequires:	FHS-fixes
BuildRequires:	libwnck-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuxPanel is a complete rewrite of my old "MacOS Style Panel" project.
It's now a lot easier to maintain (as everything is a plugin) and
extend. Since it's still in early development stages, it's not
intended for non-developers (however, if configured properly, it can
be used even by your cat).

%description -l pl
SuxPanel to ca�kowicie przepisany wcze�niejszy projekt "MacOS Style
Panel". Jest teraz �atwiejszy do utrzymania (jako �e wszystko jest
wtyczk�) i rozszerzania. Poniewa� jest nadal we wczesnym stadium
rozwoju, nie jest przeznaczony do u�ywania przez nieprogramist�w
(jednak po odpowiedniej konfiguracji m�g�by by� u�ywany nawet przez
kota).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install suxpanel-install.sh $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/pixmaps
%dir %{_datadir}/%{name}/plugins
%attr(755,root,root) %{_datadir}/%{name}/plugins/*.so
