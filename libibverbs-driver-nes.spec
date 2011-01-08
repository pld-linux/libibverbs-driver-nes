Summary:	Userspace driver for the NetEffect Ethernet Server Cluster adapters
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart NetEffect Ethernet Server Cluster
Name:		libibverbs-driver-nes
Version:	1.1.1
Release:	0.1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/nes/libnes-%{version}.tar.gz
# Source0-md5:	32a904a4fd7589223906a078ae84e419
URL:		http://openib.org/
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnes is a userspace driver for NetEffect Ethernet Server Cluster
adapters. It works as a plug-in module for libibverbs that allows
programs to use NetEffect hardware directly from userspace.

%description -l pl.UTF-8
libnes to sterownik przestrzeni użytkownika dla kart NetEffect
Ethernet Server Cluster. Działa jako moduł ładowany przez libibverbs,
pozwalający programom na dostęp z przestrzeni użytkownika do sprzętu
NetEffect.

%package static
Summary:	Static version of nes driver
Summary(pl.UTF-8):	Statyczna wersja sterownika nes
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of nes driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika nes, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libnes-%{version}

%build
# define IBV_QPT_RAW_ETH until it's in libibverbs
%configure \
	CPPFLAGS="%{rpmcppflags} -DIBV_QPT_RAW_ETH=7"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnes.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_libdir}/libnes-rdmav2.so
%{_sysconfdir}/libibverbs.d/nes.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libnes.a
