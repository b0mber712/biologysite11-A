# Biology Mini‑Site — GitHub Pages Ready

This folder is ready to deploy to **GitHub Pages**.

## Deploy (5 steps)
1. Create a repo **biology-site** on GitHub.
2. Upload all files from this folder to the repo root.
3. Open **Settings → Pages → Build and deployment**:
   - Source: **Deploy from a branch**
   - Branch: **main** / **root**
4. Wait ~1 minute. Your site will be live at:
   `https://<username>.github.io/biology-site/`
5. Regenerate QR codes with your real URL (below).

## Regenerate QR for your real URL
- Replace `<username>` in `regen_qr.py` with your GitHub username.
- Run:
```bash
python3 regen_qr.py
```
- New QR PNGs will appear in **qr/**, pointing to your live pages.

Footer signature is set to: **made by Nikita Bober & Ilya Kovalevych**.