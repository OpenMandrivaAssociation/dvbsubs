# Define Mandrake Linux version we are building for
%define mdkversion %(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandrake-release)

%define name	dvbsubs
%define version	0.3
%define beta	0


%if %beta
%define release 0.%{beta}.%{mdkrel}
%else
%define release %{mdkrel}
%endif
%define debug_package %{nil}
Summary:	Dvbsubtitle tools	
Name:		%{name}
Version:	%{version}
Release: 7
Source0:	http://linuxtv.org/download/dvb/%{name}-%{version}.tar.bz2
Patch0:	dvbsubs-0.3-png-zlib.patch
License:	GPLv2
Group:		Video
URL:		http://linuxtv.org/dvb/

BuildRequires:	libxml2-devel 
BuildRequires:	freetype2-devel
BuildRequires:	png-devel

%description
DVB subtitles utilities.

%prep
%setup -q
%patch0 -p0

%build
%make

%install
#makeinstall_std
install -d -m755 %buildroot/%{_bindir}
install -m755 dvbsubs %buildroot/%{_bindir}/
install -m755 dvbtextsubs %buildroot/%{_bindir}/
install -m755 xml2spumux %buildroot/%{_bindir}/
install -m755 xml2srt %buildroot/%{_bindir}/

install -d -m755 %buildroot/%{_mandir}/man1
install -m755 dvbtextsubs.1 %buildroot/%{_mandir}/man1/


%files
%doc CHANGES COPYING README 
%{_bindir}/*
%{_mandir}/man1/*




