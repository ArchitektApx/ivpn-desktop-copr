%global         debug_package %{nil}

Name:           ivpn-ui
Version:        3.14.17
Release:        1%{?dist}
Summary:        IVPN - Secure VPN for Privacy (CLI)

License:        GPL-3.0
URL:            https://www.ivpn.net
Source0:        https://github.com/ArchitektApx/ivpn-desktop-copr/releases/download/v%{version}/ivpn.tar.gz

Requires:       ivpn >= %{version}

%description
IVPN is a secure VPN focused on privacy. This package provides the desktop UI.

%prep
%autosetup -n ivpn

%install
%__install -d %{buildroot}/opt/%{name}/ui
%__install -d %{buildroot}%{_datadir}/applications
%__install -d %{buildroot}%{_sysconfdir}/opt/%{name}

# Install the compiled UI to the proper locations
mkdir -p %{buildroot}/opt/%{name}/ui/bin
%__cp -fr ui/bin %{buildroot}/opt/%{name}/ui/bin

%__install -D ui/IVPN.desktop %{buildroot}%{_datadir}/applications/IVPN.desktop
%__install -D ui/IVPN.desktop %{buildroot}/opt/%{name}/ui/IVPN.desktop
%__install -D ui/ivpnicon.svg %{buildroot}/opt/%{name}/ui/ivpnicon.svg

%files
/opt/%{name}/ui/bin/*
%{_datadir}/applications/IVPN.desktop
/opt/%{name}/ui/IVPN.desktop
/opt/%{name}/ui/ivpnicon.svg

%changelog