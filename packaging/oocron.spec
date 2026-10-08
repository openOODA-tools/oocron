Name:           oocron
Version:        0.2.0
Release:        1%{?dist}
Summary:        Pure systemd timer scheduler replacing legacy cron with journald integration.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocron
Source0:        oocron-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocron is a sovereign, capability-bounded CRON TRANSPILER & SYSTEMD TIMER SCHEDULER
written in pure openOODA, featuring zero ambient authority, systemd unit generation,
journald integration, cron validation, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocron
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocron-uninstall

%files
/usr/bin/oocron
/usr/bin/oocron-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign pure openOODA release with systemd-native timer synthesis and MCP server
