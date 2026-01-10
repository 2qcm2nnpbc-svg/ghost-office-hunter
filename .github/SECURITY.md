# Security Policy

## Supported Versions

We actively support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.1.x   | :white_check_mark: |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please **DO NOT** open a public issue. Instead, please report it via one of the following methods:

1. **Email**: Contact the repository maintainer directly
2. **Private Security Advisory**: Use GitHub's private security advisory feature
3. **Direct Message**: Reach out through appropriate channels

Please include the following information:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Security Best Practices

### For Users

1. **Never commit `.env` files** - Always use `env.example` as a template
2. **Rotate API keys regularly** - Especially if you suspect they may have been exposed
3. **Use environment variables** - Never hardcode credentials in code
4. **Review dependencies** - Keep packages updated to avoid known vulnerabilities

### For Contributors

1. **No hardcoded secrets** - All sensitive data must come from environment variables
2. **Review before committing** - Always check `git status` before committing
3. **Use `.gitignore`** - Ensure all sensitive files are properly ignored
4. **Test locally** - Never use production credentials in development

## Known Security Considerations

- **API Keys**: The application requires OpenAI API keys. These must be kept secure and never committed to the repository.
- **Network Access**: The application makes external API calls to DuckDuckGo and OpenAI. Ensure network security is properly configured.
- **Input Validation**: User input is sanitized for file paths, but always validate external inputs.

## Security Updates

Security updates will be released as patch versions (e.g., 1.1.1 → 1.1.2). Critical security fixes may be backported to previous major versions.

---

**Last Updated:** 2025-01-10
