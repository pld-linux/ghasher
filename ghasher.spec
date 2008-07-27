Summary:	MD5 sum utility
Summary(pl.UTF-8):	Narzędzie do obliczania sum MD5
Name:		ghasher
Version:	1.2.1
Release:	3
License:	BSD
Group:		X11/Applications
Source0:	http://asgaard.homelinux.org/code/ghasher/%{name}-%{version}.tar.gz
# Source0-md5:	36edeaf03bd8827d2a96db86735532fb
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://asgaard.homelinux.org/code/ghasher/
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libglade2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ghasher is a small GUI utility that calculates MD5/SHA-1 and many
other sums.

%description -l pl.UTF-8
ghasher to małe narzędzie do obliczania sum MD5/SHA-1 i wielu innych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE `pkg-config gtk+-2.0 libglade-2.0 --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
