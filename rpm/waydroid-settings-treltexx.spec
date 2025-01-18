Name:           waydroid-settings-treltexx
Version:        1.0.0
Release:        1
Summary:        Waydroid-settings-treltexx installs System Settings module and Top Menu button for Waydroid.
License:        GPLv3
URL:            https://github.com/waydroid
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  systemd
Requires:       lxc
Requires:       dnsmasq
Requires:       python3-gbinder
Requires:       python3-gobject
Requires:       waydroid-sensors
Requires:       waydroid-gbinder-config-hybris-treltexx
Requires:       waydroid-1.2-treltexx
Requires:       waydroid-vendor17.1-treltexx

%description
Waydroid uses Linux namespaces (user, pid, uts, net, mount, ipc) to run a full Android system in a container and provide Android applications on any GNU/Linux-based platform.

The Android system inside the container has direct access to any needed hardware.

The Android runtime environment ships with a minimal customized Android system image based on LineageOS. The image is currently based on Android 10.

Custom:
  Repo: https://github.com/edp17/waydroid-settings-treltexx
Icon: https://raw.githubusercontent.com/waydroid/waydroid/bullseye/data/AppIcon.png
Categories:
  - System

%prep
%setup

%install
mkdir -p %{buildroot}/usr/share/waydroid/settings

# Settings files
install -D -m644 settings/waydroid.json %{buildroot}/usr/share/jolla-settings/entries/waydroid.json
install -D -m644 settings/Waydroid.qml %{buildroot}/usr/share/waydroid/settings/Waydroid.qml
install -D -m644 settings/EnableSwitch.qml %{buildroot}/usr/share/waydroid/settings/EnableSwitch.qml

%clean
rm -rf $RPM_BUILD_ROOT

%post
systemctl daemon-reload
systemctl-user daemon-reload
systemctl enable waydroid-container
chmod 777 /home/waydroid

%files
%defattr(-,root,root,-)
%{_datadir}/jolla-settings/entries/waydroid.json
%{_datadir}/waydroid/settings/Waydroid.qml
%{_datadir}/waydroid/settings/EnableSwitch.qml
