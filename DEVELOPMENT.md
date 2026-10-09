# Development Status

## OPS-UDA-001 — Trusted UDA proxy subpath
Status: IN PROGRESS

Flask URL generation respects one controlled UDA/Caddy forwarded prefix. Direct LAN root access remains supported. Tests use an isolated temporary data path and never touch private health records. Backend ingress must be restricted from forwarded-header spoofing; no public proxy access change.

- [ ] CI passed and merged to main
- [ ] User verifies page, input and CSV/data download behind UDA authentication
