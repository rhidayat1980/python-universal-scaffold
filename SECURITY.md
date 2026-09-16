# Security Policy

## Supported Versions

We actively maintain and provide security updates for the latest template release.

| Version | Supported          |
| :------ | :----------------- |
| `main`  | :white_check_mark: |
| `>= 0.1.0` | :white_check_mark: |
| `< 0.1.0`  | :x:                |

---

## Security Philosophy (Shift-Left DevSecOps)

This scaffolder is designed with security as a primary citizen:
- **Non-root OCI Containers**: All generated Dockerfiles run under unprivileged UID `10001:10001` (`appuser`).
- **Automated SAST**: Bandit is configured to scan all generated code for security vulnerabilities.
- **Dependency Auditing**: `pip-audit` validates the supply chain and third-party packages against the Python Packaging Advisory Database (PyPA) and OSV.
- **Zero Secrets in Code**: Environment configurations rely strictly on `.env` and Pydantic `BaseSettings`.

---

## Reporting a Vulnerability

If you discover a security vulnerability or supply chain weakness within this template generator or any of its generated archetypes:

1. **Do NOT open a public GitHub issue.**
2. Please privately report the vulnerability by emailing **rhidayat@ptcpi.cloud** with:
   - Description of the vulnerability and its potential impact.
   - Affected archetype(s) or template files.
   - Step-by-step reproduction instructions or a minimal proof of concept (PoC).
3. We will acknowledge receipt of your report within **48 hours** and provide a timeline for remediation.
4. Once a fix is verified, we will release a security advisory and credit the reporter.

Thank you for helping keep our software secure!
