Summary:	MD5 sum utility
Summary(pl):	Narzêdzie do obliczania sum MD5
Name:		ghasher
Version:	1.1.1
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://asgaard.homelinux.org/code/ghasher/%{name}-%{version}.tar.gz
# Source0-md5:	bf75a943f60973a07dd2a51517407fa5
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://asgaard.homelinux.org/code/ghasher/
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ghasher is a small GUI utility that calculates MD5/SHA-1 and many
other sums.

%description -l pl
ghasher to ma³e narzêdzie do obliczania sum MD5/SHA-1 i wielu innych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} `pkg-config gtk+-2.0 --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
