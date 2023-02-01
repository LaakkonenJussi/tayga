Name:		tayga
Version:	0.9.2
Release:	1
Summary:	Simple, no-fuss NAT64
License:	GPLv2+
URL:		http://www.litech.org/%{name}/
Source0:	http://www.litech.org/%{name}/%{name}-%{version}.tar.bz2
Patch0:		tayga-0.9.2_cflags_override.patch
Patch1:		tayga-c99.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Requires:	iproute

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	coreutils

%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux that uses
the TUN driver to exchange IPv4 and IPv6 packets with the kernel. It is
intended to provide production-quality NAT64 service for networks where
dedicated NAT64 hardware would be overkill.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p1


%build
CFLAGS="%{optflags} -fPIE"
LDFLAGS="$LDFLAGS -Wl,-z,now" 
export CFLAGS
export LDFLAGS

%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
echo %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

%files
%doc README
%license COPYING
%{_sbindir}/%{name}
%{_sharedstatedir}/%{name}
%exclude %{_sysconfdir}/%{name}.conf.example
%exclude %{_mandir}/man*/%{name}.*.gz
