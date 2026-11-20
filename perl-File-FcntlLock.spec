#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	File
%define		pnam	FcntlLock
Summary:	File::FcntlLock - File locking with fcntl(2)
Name:		perl-File-FcntlLock
Version:	0.22
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	579698d735d864ee403674f1175f789d
URL:		https://metacpan.org/dist/File-FcntlLock
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File locking in Perl is usually done using the flock() function.
Unfortunately, this only allows locks on whole files and is often
implemented in terms of flock(2), which has some shortcomings.

Using this module file locking via fcntl(2) can be done (obviously,
this restricts the use of the module to systems that have a fcntl(2)
system call). Before a file (or parts of a file) can be locked, an
object simulating a flock structure must be created and its properties
set. Afterwards, by calling the lock() method a lock can be set or it
can be determined if and which process currently holds the lock.

To create a new object representing a flock structure call new():

  $fs = new File::FcntlLock;

You also can pass the new() method a set of key-value pairs to
initialize the objects properties, e.g. use

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/File/*.pm
%{perl_vendorarch}/File/FcntlLock
%dir %{perl_vendorarch}/auto/File/FcntlLock
%attr(755,root,root) %{perl_vendorarch}/auto/File/FcntlLock/*.so
%{_mandir}/man3/*
