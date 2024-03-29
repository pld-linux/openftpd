%define	snap	20041120
Summary:	Free, open source FTP server implementation
Summary(pl.UTF-8):	Implementacja serwera FTP
Name:		openftpd
Version:	0.31
Release:	0.%{snap}.3
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.openftpd.org/%{name}-daily.tar.gz
# Source0-md5:	26a9de1794b5137d283607c81ed44a14
Patch0:		%{name}-x86_64-endian.patch
URL:		http://www.openftpd.org/
BuildRequires:	glib-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-Bit-Vector
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# this isn't ,,standard FTP''. Don't treat it as system FTP server
# and don't put Provides:ftpserver etc here ! --misiek

%description
OpenFTPD is a free, open source FTP server implementation for the UNIX
platform. It is based on FTP4ALL (Version 3.012) by Crescent and
started as an alternative version by primemover with some fixes and
patches because the official development of FTP4ALL stalled.

%description -l pl.UTF-8
OpenFTPD jest darmową, open source implementacją serwera FTP dla
platformy UNIX. Bazuje on na FTP4ALL (wersji 3.012), a rozpoczynał
jako alternatywna wersja ftp4all z wieloma poprawkami i łatkami.

%prep
%setup -q -n %{name}-daily
%patch0 -p1

%build
./cons-*/cons \
	DEBUG=no \
	WARNINGS=yes \
	TRCHECK=yes \
	TRBIN=%{_sbindir}/traceroute \
	DIRCOMPLETION=no \
	SITEEXEC=no \
	LOGIPS=yes \
	ENCRYPT=yes \
	DELINCOMPLETE=yes \
	TLS=yes \
	.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}

cp -R standard/* $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -f build/ftpd/ftpd $RPM_BUILD_ROOT%{_libdir}/%{name}/sbin/
cp -f build/ftps/ftps $RPM_BUILD_ROOT%{_libdir}/%{name}/sbin/
cp -f build/ftpa/ftpa $RPM_BUILD_ROOT%{_libdir}/%{name}/sbin/
cp -f build/misc/checksum $RPM_BUILD_ROOT%{_libdir}/%{name}/bin/
cp -f build/misc/getpw $RPM_BUILD_ROOT%{_libdir}/%{name}/bin/
cp -f build/misc/glconv $RPM_BUILD_ROOT%{_libdir}/%{name}/bin/
cp -f build/misc/msg $RPM_BUILD_ROOT%{_libdir}/%{name}/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES ChangeLog README TODO UPDATE doc
%attr(-,root,root) %{_libdir}/%{name}
