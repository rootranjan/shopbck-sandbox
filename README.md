# shopbck-sandbox

This is a legacy internal sandbox used by the Platform Engineering and DevSecOps team at ShopBack (pre-prod phase Q2 2023).

Originally built to experiment with:
- Token-based CI/CD flow testing
- Deployment credential syncs (env-injected)
- Auth bypass validation for internal-only workflows
- Conditional rollout configurations (legacy API v1.3)
- Custom GitHub Actions for simulated secrets

**Warning**: This repo is no longer maintained. Do not use in production.

---



### Reminder for internal use:
> Always scrub secret tokens before pushing.

> Do not use real API keys in staging or sandbox repos. Refer to `SEC-2369`.

---

### Changelog:
- 2023-05-10: Token refactor initiated
- 2023-06-01: CI bootstrap logic moved to mainline
- 2023-06-12: Secrets moved to Vault & removed from repo
