%include        /usr/lib/rpm/macros.perl
%define	snap	20030501
Summary:	Free, open source FTP server implementation
Summary(pl):	Implementacja serwera FTP
Name:		openftpd
Version:	0.31
Release:	0.%{snap}
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.openftpd.org/%{name}-daily.tar.gz
# Source0-md5:	ea7cbf57dca6ff0e50c051bfe6801790
URL:		http://www.openftpd.org/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl >= 5.6
BuildRequires:	perl-modules
BuildRequires:	perl-Bit-Vector
BuildRequires:	perl-libwww
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# this isn't ,,standard ftp''. Don't treat it as system ftp server
# and don't put Provides:ftpserver etc here ! --misiek

%description
OpenFTPD is a free, open source FTP server implementation for the UNIX
platform. It is based on FTP4ALL (Version 3.012) by Crescent and
started as an alternative version by primemover with some fixes and
patches because the official development of FTP4ALL stalled.

%description -l pl
OpenFTPD jest darmow±, open source implementacj± serwera FTP dla
platformy UNIX. Bazuje on na FTP4ALL (wersji 3.012), a rozpoczyna³
jako alternatywna wersja ftp4all z wieloma poprawkami i ³atkami.

%prep
%setup -q -n %{name}-daily

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
