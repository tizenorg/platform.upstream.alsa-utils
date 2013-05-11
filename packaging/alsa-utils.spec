Name:           alsa-utils
Version:        1.0.26
Release:        1
License:        GPL-2.0+
Summary:        Advanced Linux Sound Architecture (ALSA) utilities
Url:            http://www.alsa-project.org/
Group:          Applications/Multimedia
Source0:        ftp://ftp.alsa-project.org/pub/utils/alsa-utils-%{version}.tar.bz2
BuildRequires:  libasound-devel

%description
This package contains command line utilities for the Advanced Linux Sound
Architecture (ALSA).

%package doc
Summary:        Man pages for alsa-utils
Group:          Documentation
Requires:       %{name} = %{version}

%description doc
Man pages for alsa-utils

%prep
%setup -q


%build

%configure --disable-static \
    --disable-nls \
    --disable-xmlto \
    --disable-alsamixer \
    --disable-alsatest

make %{?_smp_mflags}

%install
%make_install

%remove_docs

%files
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/alsa/*
%{_datadir}/sounds/*
/lib/udev/rules.d/90-alsa-restore.rules
