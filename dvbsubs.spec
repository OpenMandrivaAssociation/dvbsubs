%define _empty_manifest_terminate_build 0

Summary:	Dvbsubtitle tools	
Name:		dvbsubs
Version:	0.3
Release:	18
License:	GPLv2
Group:		Video
Url:		http://linuxtv.org/dvb/
Source0:	http://linuxtv.org/download/dvb/%{name}-%{version}.tar.bz2
Patch0:		dvbsubs-0.3-png-zlib.patch

BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libxml-2.0)

%description
DVB subtitles utilities.

%prep
%setup -q
%autopatch -p1

%build
%make_build

%install
#make_install
install -d -m755 %{buildroot}/%{_bindir}
install -m755 dvbsubs %{buildroot}/%{_bindir}/
install -m755 dvbtextsubs %{buildroot}/%{_bindir}/
install -m755 xml2spumux %{buildroot}/%{_bindir}/
install -m755 xml2srt %{buildroot}/%{_bindir}/

install -d -m755 %{buildroot}/%{_mandir}/man1
install -m755 dvbtextsubs.1 %{buildroot}/%{_mandir}/man1/


%files
%doc CHANGES COPYING README 
%{_bindir}/*
%{_mandir}/man1/*

