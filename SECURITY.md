# Security Policy

## Reporting a Vulnerability

If you discover a security issue in post-kit, please report it responsibly.

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, email: **huzaifaali4013399@gmail.com**

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Response Timeline

- **Acknowledgment:** Within 48 hours
- **Assessment:** Within 1 week
- **Fix/Resolution:** Depends on severity, but we aim for 2 weeks for critical issues

## Scope

post-kit is a collection of markdown instruction files — it contains no executable code, no APIs, no databases, and no authentication. Security concerns are limited to:

- Accidental exposure of user data in shared niche packs (API keys, personal info in example configs)
- Malicious instructions in contributed module files that could cause an AI tool to behave unsafely
- Supply chain concerns if distributed through plugin registries

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | Yes       |

## Attribution

We follow [responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure) practices. Reporters will be credited in the CHANGELOG unless they prefer to remain anonymous.
