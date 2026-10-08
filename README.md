# oocron: Sovereign Systemd Timer Scheduler & Transpiler

<div align="center">

```
================================================================================
                                 oocron
              Sovereign openOODA Systemd Timer Scheduler
================================================================================
```

**Sovereign Systemd Timer Scheduler & Transpiler**  
*Pure systemd timer scheduler replacing legacy cron with journald integration.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Streaming MCP stdio for AI agents  
Written in 100% pure native [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocron/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocron-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocron/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocron/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocron-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocron/uninstall.sh | bash
```

---

## 2. CLI Usage

```
Usage: oocron [OPTIONS] [CRON_EXPR] [COMMAND]

Pure systemd timer scheduler replacing legacy cron with journald integration.

Options:
  -e, -s, --expr, --schedule <EXPR>  Specify cron schedule expression (e.g. '*/5 * * * *', '@daily')
  -c, --cmd, --command <COMMAND>     Executable command line to run in synthesized oneshot service
  -u, --unit, --name <NAME>          Base name for systemd unit pair (default: 'oocron-job')
  -V, --validate                     Validate cron syntax and display systemd OnCalendar spec
  -d, --demo                         Showcase production cron conversions across 4 sample jobs
  -j, --json                         Output structured JSON
      --theme <THEME>                Select terminal color theme (ember, ocean, matrix, cyber, monochrome)
      --mcp                          Run streaming MCP JSON-RPC 2.0 server on stdio
  -h, --help                         Show this help message and exit
  -v, --version                      Show version information and exit
```

---

## 3. Pure Systemd-Native Philosophy

Adhering strictly to modern Linux infrastructure guidelines:
* **Declarative System Units**: Transpiles 5-field cron schedules and macros (`@reboot`, `@hourly`, `@daily`, `@weekly`, `@monthly`, `@yearly`) to native `.timer` and `.service` unit files in `/etc/systemd/system/`.
* **Zero Legacy Crond**: Eliminates background cron daemons, mail spoolers, and unconfined crontabs.
* **Service Hardening & Confinement**: Every generated oneshot service enforces `ProtectSystem=strict`, `ProtectHome=read-only`, `PrivateTmp=true`, and `NoNewPrivileges=true`.
* **Journald Logging**: Logging routes exclusively to `systemd-journald` (`StandardOutput=journal`, `StandardError=journal`).

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocron` runs a JSON-RPC 2.0 stdio server providing four sovereign scheduling tools:

* `cron_to_systemd`: Transpile a cron schedule and command into declarative systemd timer and service units.
* `cron_validate`: Validate cron schedule syntax and compute the systemd `OnCalendar` equivalent.
* `cron_macros`: List standard cron macros and their systemd calendar mappings.
* `cron_demo`: Return synthetic multi-schedule cron to systemd unit showcase.

```bash
oocron --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded**: Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient authority.
* **Negative-Trust Architecture**: Complete syntax validation and bounds checking on minute, hour, day-of-month, month, and day-of-week fields.
* **Hermetic Binary**: Standalone zero-dependency executable compiled via `oodac`.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
