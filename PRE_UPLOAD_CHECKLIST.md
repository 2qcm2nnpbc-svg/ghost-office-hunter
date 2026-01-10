# Pre-Upload Checklist for GitHub

## ⚠️ CRITICAL: Remove .env from Git Tracking

Before uploading to GitHub, you **MUST** remove the `.env` file from git tracking:

```bash
# Remove .env from git (but keep the file locally)
git rm --cached .env

# Verify it's no longer tracked
git status
```

## ✅ Security Verification Steps

### 1. Check what will be committed:
```bash
git status
```

**Should NOT see:**
- ❌ `.env`
- ❌ `venv/`
- ❌ `*.log`
- ❌ `reports/`
- ❌ `__pycache__/`

**Should see:**
- ✅ `env.example` (safe template)
- ✅ All `.py` files
- ✅ Documentation files
- ✅ Configuration files

### 2. Verify .env is ignored:
```bash
git check-ignore .env
# Should output: .env
```

### 3. Review sensitive files:
```bash
# Check for any API keys in code
grep -r "sk-" --include="*.py" --include="*.md" . | grep -v "your" | grep -v "example"
# Should return nothing (or only documentation examples)
```

## 📋 Files Safe to Commit

✅ **Safe files:**
- All Python source files
- `env.example` (template only)
- Documentation (`.md` files)
- Setup scripts
- Configuration templates
- `.gitignore`
- `.pre-commit-config.yaml`

## 🚫 Files That Must NOT Be Committed

❌ **Never commit:**
- `.env` (contains real API keys)
- `venv/` (virtual environment)
- `*.log` (log files)
- `reports/` (generated reports)
- `__pycache__/` (Python cache)
- `.DS_Store` (OS files)

## 🔒 Final Security Check

Run this before your first commit:

```bash
# 1. Remove .env from tracking (if it was previously tracked)
git rm --cached .env

# 2. Verify .env is ignored
git check-ignore .env && echo "✅ .env is ignored" || echo "❌ .env is NOT ignored - FIX THIS!"

# 3. Check what will be committed
git status

# 4. Review the diff (if updating existing repo)
git diff

# 5. If everything looks good, proceed with commit
```

## 📝 Recommended First Commit

```bash
# Stage all safe files
git add .

# Review what's staged
git status

# Commit
git commit -m "Initial commit: Ghost Office Hunter - Production ready"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/your-username/ghost-office-hunter.git

# Push
git push -u origin main
```

## ✅ After Upload

1. Verify `.env` is NOT in the GitHub repository
2. Check that `env.example` is visible (this is the template)
3. Update README with your actual GitHub URL
4. Consider adding a LICENSE file
5. Consider enabling GitHub Actions for CI/CD (optional)

---

**Status:** Ready for upload after removing .env from tracking
