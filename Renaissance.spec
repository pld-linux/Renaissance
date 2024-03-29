Summary:	GNUstep Renaissance library
Summary(pl.UTF-8):	Biblioteka GNUstep Renaissance
Name:		Renaissance
Version:	0.8.0
Release:	5
License:	GPL
Group:		Libraries
Source0:	http://www.gnustep.it/Renaissance/Download/%{name}-%{version}.tar.gz
# Source0-md5:	520d8fe210491b5646bb4743a72560b1
URL:		http://www.gnustep.it/Renaissance/
BuildRequires:	gnustep-gui-devel >= 0.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
GNUstep Renaissance is free software (GNU LGPL), and part of the
GNUstep project. It is a development framework which runs on top of
the GNUstep libraries. It also works on top of the Apple OSX Cocoa
libraries, providing an opaque layer to write portable applications.

%description -l pl.UTF-8
GNUstep Renaissance to wolnodostępne oprogramowanie (GNU LGPL) i część
projektu GNUstep. Jest to szkielet programistyczny działający w
oparciu o biblioteki GNUstepa. Może działać także w oparciu o Cocoa
z OSX Apple'a, co daje nieprzezroczystą warstwę do pisania przenośnych
aplikacji.

%package devel
Summary:	Header files for GNUstep Renaissance library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GNUstep Renaissance
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-gui-devel >= 0.9.1

%description devel
Header files required to build applications against the GNUstep
Renaissance library.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania aplikacji z użyciem biblioteki
GNUstep Renaissance.

%prep
%setup -q 

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog ANNOUNCE Documentation README TODO AUTHORS NOTES.OSX 

%dir %{_prefix}/System/Applications/GSMarkupBrowser.app
%attr(755,root,root) %{_prefix}/System/Applications/GSMarkupBrowser.app/GSMarkupBrowser
%dir %{_prefix}/System/Applications/GSMarkupBrowser.app/Resources
%{_prefix}/System/Applications/GSMarkupBrowser.app/Resources/*.desktop
%{_prefix}/System/Applications/GSMarkupBrowser.app/Resources/*.plist
%dir %{_prefix}/System/Applications/GSMarkupBrowser.app/%{gscpu}
%dir %{_prefix}/System/Applications/GSMarkupBrowser.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GSMarkupBrowser.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/GSMarkupBrowser.app/%{gscpu}/%{gsos}/%{libcombo}/GSMarkupBrowser
%{_prefix}/System/Applications/GSMarkupBrowser.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%dir %{_prefix}/System/Applications/GSMarkupLocalizableStrings.app
%attr(755,root,root) %{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/GSMarkupLocalizableStrings
%dir %{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/Resources
%{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/Resources/*.desktop
%{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/Resources/*.plist

%dir %{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/%{gscpu}
%dir %{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/%{gscpu}/%{gsos}/%{libcombo}/GSMarkupLocalizableStrings
%{_prefix}/System/Applications/GSMarkupLocalizableStrings.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%docdir %{_prefix}/System/Library/Documentation/*

%{_prefix}/System/Library/Headers/%{libcombo}/Renaissance
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
