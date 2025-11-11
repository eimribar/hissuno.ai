# Visual Baseline Documentation
**Created**: November 11, 2025 18:20
**Commit**: 01cbdff Fix server.py to serve /img/home/ directory directly
**Purpose**: Reference document for pixel-perfect visual preservation

## ⚠️ CRITICAL RULE
**ANY change that affects visual appearance MUST be verified against this baseline.**

## Testing Protocol

### After EVERY change:
1. ✅ Open http://localhost:3000/ in browser
2. ✅ Compare visually against screenshots in `/visual-reference/`
3. ✅ Check responsive views (mobile, tablet, desktop)
4. ✅ Test all interactive elements (buttons, videos, forms, menus)
5. ✅ Verify all images/videos load correctly
6. ✅ Check console for errors
7. ✅ Test in Chrome, Firefox, Safari

### If ANY visual difference detected:
1. 🛑 STOP immediately
2. 📸 Take screenshot of the difference
3. 🔍 Identify what changed
4. ⏪ Rollback: `git checkout .` or restore from backup
5. 🔧 Fix the approach
6. 🔄 Try again

---

## Current State Measurements

### Colors
- **Primary Orange**: #FF5600
- **Dark Blue Background**: #020917
- **Text Primary**: #050505 (near-black)
- **Text Secondary**: rgba(0, 0, 0, 0.6)
- **Border/Divider**: #C0BEBE, #C3C2BD

### Typography
- **Primary Font**: Custom Next.js font system
- **Headings**: Large serif-style font
- **Body**: Sans-serif, ~16px base
- **Line Height**: Standard 1.5-1.6

### Layout
- **Max Width**: Container-based (Tailwind max-w-*)
- **Navigation Height**: Fixed at top
- **Section Spacing**: Consistent vertical rhythm
- **Grid**: Responsive Tailwind grid system

### Key Sections (Visual Checkpoints)
1. **Hero Section**:
   - Canvas animation with video texture
   - Main headline with large typography
   - CTA buttons (white and outlined)

2. **Performance Section**:
   - FIG 2.A: Orange area chart
   - FIG 2.B: Horizontal bar chart
   - FIG 2.C: Customer testimonial card
   - All charts must render identically

3. **Team Section**:
   - Team member photos (10 people)
   - Grid layout with hover effects

4. **Footer**:
   - Links, logos, compliance badges
   - Dark background with light text

---

## File Integrity Checklist

### Critical Files (DO NOT modify directly)
- ❌ `index.html` - Only edit after un-minification and testing
- ❌ `/assets/js/*.js` - Minified bundles, do not touch
- ✅ `/assets/css/*.css` - Safe to edit colors/styles carefully
- ✅ `/assets/images/*` - Safe to replace (maintain dimensions)
- ✅ `/fonts/*` - Safe to replace
- ✅ `/img/home/*` - Safe to replace videos

### Asset Dimensions (MUST match exactly)
- Hero video: 1536×1148px (displayed size)
- Team photos: Various, maintain aspect ratios
- Logos: Various SVGs, maintain viewBox
- Favicons: 32×32px

---

## Rollback Procedures

### If something breaks:

#### Quick Rollback (Git):
```bash
# Undo uncommitted changes
git checkout .

# Go back one commit
git reset --hard HEAD~1

# Go back to specific commit
git checkout 01cbdff

# Return to main branch
git checkout main
```

#### Full Restoration (Backup):
```bash
# List available backups
ls -lh /Users/eimribar/Desktop/ | grep fin-replica-backup

# Restore from backup (replace TIMESTAMP)
rm -rf /Users/eimribar/Desktop/fin-replica
cp -r /Users/eimribar/Desktop/fin-replica-backup-TIMESTAMP \
      /Users/eimribar/Desktop/fin-replica
```

#### Current Backup:
- **Location**: `/Users/eimribar/Desktop/fin-replica-backup-20251111-182056`
- **Size**: Complete copy of entire project
- **Created**: Nov 11, 2025 18:20:56

---

## Visual Reference Images

### TODO: Capture reference screenshots
Create `/visual-reference/` directory with screenshots of:
- [ ] Hero section (full width)
- [ ] Navigation menu (all states)
- [ ] Performance section (FIG 2.A, 2.B, 2.C)
- [ ] Capabilities section
- [ ] Team section
- [ ] Footer
- [ ] Mobile view (375px)
- [ ] Tablet view (768px)
- [ ] Desktop view (1920px)

### Screenshot Command:
```bash
# macOS built-in screenshot tool
# Cmd+Shift+4, then press Space, click window

# Or use browser dev tools:
# Chrome: Cmd+Shift+P → "Capture full size screenshot"
```

---

## Phase Tracking

### Phase 0: ✅ COMPLETE
- [x] Timestamped backup created
- [x] Git initialized and branch created
- [x] Visual baseline documented

### Phase 1: 🔄 IN PROGRESS
- [ ] Asset inventory
- [ ] Color palette extraction
- [ ] Asset replacement guide

### Next Steps:
1. Capture comprehensive screenshots
2. Create asset inventory
3. Begin Phase 1 work

---

## Emergency Contacts
- **Backup Location**: `/Users/eimribar/Desktop/fin-replica-backup-20251111-182056`
- **Git Branch**: `editability-improvements`
- **Main Branch**: `main` (commit 01cbdff)
- **This Document**: Updated with each phase

**Remember**: It's better to take 2x the time to preserve perfection than to rush and break the visual accuracy!
