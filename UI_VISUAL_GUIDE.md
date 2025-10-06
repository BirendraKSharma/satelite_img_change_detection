# 🎨 UI VISUAL GUIDE

## Application Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   🛰️ Satellite Image Change Detection System                          │
│      Real-Time Business Intelligence Dashboard                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────┬────────────────────────────────────────────────────────┐
│              │                                                        │
│  SIDEBAR     │                    MAIN CONTENT                        │
│              │                                                        │
│ ┌──────────┐ │  ┌──────────┬──────────┬──────────┐                  │
│ │ 🔧 Config│ │  │ Analysis │ Gallery  │Statistics│  ← TABS          │
│ └──────────┘ │  └──────────┴──────────┴──────────┘                  │
│              │                                                        │
│ Image Source │  ┌─────────────────────────────────────────┐          │
│ ○ Upload     │  │                                         │          │
│ ○ Existing   │  │                                         │          │
│              │  │        TAB CONTENT AREA                 │          │
│ ┌──────────┐ │  │                                         │          │
│ │  Upload  │ │  │                                         │          │
│ │  Files   │ │  │                                         │          │
│ └──────────┘ │  │                                         │          │
│              │  │                                         │          │
│ Loaded: 5    │  └─────────────────────────────────────────┘          │
│              │                                                        │
│ Earlier: #1  │                                                        │
│ Later: #2    │                                                        │
│              │                                                        │
│ Method:      │                                                        │
│ [Otsu...  ▼] │                                                        │
│              │                                                        │
│ Threshold    │                                                        │
│ ├─────●─────┤│                                                        │
│              │                                                        │
│ ☑ Overlay    │                                                        │
│ ☑ Heatmap    │                                                        │
│ ☑ Statistics │                                                        │
│              │                                                        │
│ ┌──────────┐ │                                                        │
│ │🚀 Run    │ │                                                        │
│ │ Analysis │ │                                                        │
│ └──────────┘ │                                                        │
│ ┌──────────┐ │                                                        │
│ │🗑️ Clear  │ │                                                        │
│ │   All    │ │                                                        │
│ └──────────┘ │                                                        │
│              │                                                        │
└──────────────┴────────────────────────────────────────────────────────┘
```

---

## Tab 1: Analysis View (Detailed)

```
┌─────────────────────────────────────────────────────────────────────┐
│                          📊 Analysis Tab                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  📊 Key Performance Indicators                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │  Total   │ │ Changed  │ │  Change  │ │   Avg    │            │
│  │   Area   │ │   Area   │ │ Regions  │ │  Region  │            │
│  │          │ │          │ │          │ │   Size   │            │
│  │ 1,048,576│ │  159,234 │ │    47    │ │   3,387  │            │
│  │  pixels  │ │  15.2%   │ │ detected │ │  pixels  │            │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘            │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  🗺️ Change Detection Visualizations                               │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │ 📅 Earlier   │  │ 📅 Later     │  │ 🔴 Changes   │            │
│  │              │  │              │  │              │            │
│  │  [IMAGE 1]   │  │  [IMAGE 2]   │  │  [OVERLAY]   │            │
│  │              │  │              │  │              │            │
│  │ Oct 1, 2025  │  │ Oct 6, 2025  │  │ Red = Change │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│                                                                     │
│  ┌──────────────────────────┐  ┌──────────────────────────┐       │
│  │ 🗺️ Binary Change Map    │  │ 📈 Intensity Heatmap     │       │
│  │                          │  │                          │       │
│  │    [BLACK & WHITE]       │  │      [HOT COLORS]        │       │
│  │                          │  │                          │       │
│  │ White = Changed          │  │ Bright = High Change     │       │
│  │ Black = Unchanged        │  │ Dark = Low Change        │       │
│  └──────────────────────────┘  └──────────────────────────┘       │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  💾 Export Results                                                 │
│  ┌──────────────────────┐  ┌──────────────────────┐              │
│  │ 📥 Download Change   │  │ 📥 Download         │              │
│  │    Map (CSV)         │  │    Statistics (CSV) │              │
│  └──────────────────────┘  └──────────────────────┘              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Tab 2: Gallery View (Detailed)

```
┌─────────────────────────────────────────────────────────────────────┐
│                         🖼️ Gallery Tab                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  All Loaded Images (5)                                             │
│                                                                     │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐                │
│  │ Image #1 │      │ Image #2 │      │ Image #3 │                │
│  │          │      │          │      │          │                │
│  │  [thumb] │      │  [thumb] │      │  [thumb] │                │
│  │          │      │          │      │          │                │
│  │ snapshot │      │ snapshot │      │ snapshot │                │
│  │ Oct-01   │      │ Oct-06   │      │ Oct-15   │                │
│  │          │      │          │      │          │                │
│  │ 1024x1024│      │ 1024x1024│      │ 1024x1024│                │
│  │ 3 bands  │      │ 3 bands  │      │ 3 bands  │                │
│  │ Float32  │      │ Float32  │      │ Float32  │                │
│  │          │      │          │      │          │                │
│  │[🗑️Remove]│      │[🗑️Remove]│      │[🗑️Remove]│                │
│  └──────────┘      └──────────┘      └──────────┘                │
│                                                                     │
│  ┌──────────┐      ┌──────────┐                                   │
│  │ Image #4 │      │ Image #5 │                                   │
│  │          │      │          │                                   │
│  │  [thumb] │      │  [thumb] │                                   │
│  │          │      │          │                                   │
│  │ snapshot │      │ snapshot │                                   │
│  │ Oct-20   │      │ Oct-25   │                                   │
│  │          │      │          │                                   │
│  │ 1024x1024│      │ 1024x1024│                                   │
│  │ 3 bands  │      │ 3 bands  │                                   │
│  │ Float32  │      │ Float32  │                                   │
│  │          │      │          │                                   │
│  │[🗑️Remove]│      │[🗑️Remove]│                                   │
│  └──────────┘      └──────────┘                                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Tab 3: Statistics View (Detailed)

```
┌─────────────────────────────────────────────────────────────────────┐
│                        📈 Statistics Tab                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  📋 Detailed Statistics                                            │
│  ┌────────────────────────────────────────────────────────┐       │
│  │ Metric               │ Value                           │       │
│  ├──────────────────────┼─────────────────────────────────┤       │
│  │ Total Pixels         │ 1,048,576                       │       │
│  │ Changed Pixels       │ 159,234                         │       │
│  │ Unchanged Pixels     │ 889,342                         │       │
│  │ Change Percentage    │ 15.18%                          │       │
│  │ Number of Regions    │ 47                              │       │
│  │ Mean Region Size     │ 3,387.11 px                     │       │
│  │ Max Region Size      │ 45,892 px                       │       │
│  └────────────────────────────────────────────────────────┘       │
│                                                                     │
│  ┌──────────────────────────┐  ┌──────────────────────────┐       │
│  │     Pie Chart            │  │     Bar Chart            │       │
│  │                          │  │                          │       │
│  │      Changed 15%         │  │    █                     │       │
│  │         ◐                │  │    █                     │       │
│  │    ◯   ◑                 │  │    █                     │       │
│  │  Unchanged 85%           │  │    █  █                  │       │
│  │                          │  │    █  █  █               │       │
│  │  🟢 Unchanged            │  │  ─────────────           │       │
│  │  🔴 Changed              │  │  % Reg Size              │       │
│  └──────────────────────────┘  └──────────────────────────┘       │
│                                                                     │
│  📊 Comparison Details                                             │
│  ┌──────────────────────────┐  ┌──────────────────────────┐       │
│  │ Earlier Image            │  │ Later Image              │       │
│  │ ────────────────────     │  │ ────────────────────     │       │
│  │ Name: snapshot-Oct-01    │  │ Name: snapshot-Oct-06    │       │
│  │ Size: 1024 x 1024        │  │ Size: 1024 x 1024        │       │
│  │ Bands: 3                 │  │ Bands: 3                 │       │
│  │ CRS: EPSG:4326           │  │ CRS: EPSG:4326           │       │
│  │ Type: float32            │  │ Type: float32            │       │
│  └──────────────────────────┘  └──────────────────────────┘       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## User Interaction Flow

```
┌─────────────┐
│  Launch App │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Welcome Screen  │
│ - Instructions  │
│ - Upload prompt │
└──────┬──────────┘
       │
       ▼
┌──────────────────────┐
│  Upload Images       │
│  ┌────────────────┐  │
│  │ Drag & Drop    │  │
│  │ or Browse      │  │
│  └────────────────┘  │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Images Loaded       │
│  • Thumbnails shown  │
│  • Metadata extracted│
│  • Gallery updated   │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Select Pair         │
│  • Earlier image     │
│  • Later image       │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Configure Method    │
│  • Detection algo    │
│  • Parameters        │
│  • Viz options       │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Run Analysis        │
│  • Processing...     │
│  • 3-5 seconds       │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  View Results        │
│  ┌────────────────┐  │
│  │ Analysis Tab   │  │
│  │ - KPIs         │  │
│  │ - Visuals      │  │
│  │ - Export       │  │
│  └────────────────┘  │
│  ┌────────────────┐  │
│  │ Gallery Tab    │  │
│  │ - All images   │  │
│  │ - Thumbnails   │  │
│  └────────────────┘  │
│  ┌────────────────┐  │
│  │ Statistics Tab │  │
│  │ - Detailed     │  │
│  │ - Charts       │  │
│  └────────────────┘  │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│  Export / Iterate    │
│  • Download CSVs     │
│  • Try new pair      │
│  • Try new method    │
└──────────────────────┘
```

---

## Sidebar States

### State 1: No Images
```
┌──────────────┐
│ 🔧 Config    │
├──────────────┤
│ Image Source │
│ ● Upload     │
│ ○ Existing   │
│              │
│ ┌──────────┐ │
│ │  Upload  │ │
│ │  Files   │ │
│ └──────────┘ │
│              │
│ Loaded: 0    │
│              │
│ [No options] │
│ [yet]        │
└──────────────┘
```

### State 2: 1 Image
```
┌──────────────┐
│ 🔧 Config    │
├──────────────┤
│ Image Source │
│ ● Upload     │
│ ○ Existing   │
│              │
│ ┌──────────┐ │
│ │  Upload  │ │
│ │  Files   │ │
│ └──────────┘ │
│              │
│ Loaded: 1    │
│              │
│ ⚠️ Need 2+   │
│ for analysis │
└──────────────┘
```

### State 3: 2+ Images (Ready)
```
┌──────────────┐
│ 🔧 Config    │
├──────────────┤
│ Image Source │
│ ● Upload     │
│ ○ Existing   │
│              │
│ ┌──────────┐ │
│ │  Upload  │ │
│ │  Files   │ │
│ └──────────┘ │
│              │
│ Loaded: 5    │
│              │
│ Earlier: #1▼ │
│ Later: #2  ▼ │
│              │
│ Method:      │
│ [Otsu... ▼]  │
│              │
│ ☑ Overlay    │
│ ☑ Heatmap    │
│              │
│ ┌──────────┐ │
│ │🚀 Run    │ │
│ │ Analysis │ │
│ └──────────┘ │
└──────────────┘
```

---

## Color Scheme

### Primary Colors
```
┌────────────────────────────────────────┐
│ Gradient Purple-Blue                   │
│ Primary: #667eea → #764ba2             │
│                                        │
│ Used for:                              │
│ • Header text                          │
│ • Buttons                              │
│ • Accent borders                       │
└────────────────────────────────────────┘
```

### Change Detection Colors
```
┌────────────────────────────────────────┐
│ Red: #e74c3c   → Changed areas         │
│ Green: #2ecc71 → Unchanged areas       │
│ Yellow: #f1c40f → Medium changes       │
│ Hot: red-yellow → Intensity heatmap    │
└────────────────────────────────────────┘
```

### UI Elements
```
┌────────────────────────────────────────┐
│ Background: #f8f9fa  → Light gray      │
│ Cards: #ffffff       → White           │
│ Text: #2c3e50        → Dark gray       │
│ Success: #d4edda     → Light green     │
│ Warning: #fff3cd     → Light yellow    │
└────────────────────────────────────────┘
```

---

## Responsive Behavior

### Desktop (> 1200px)
```
[Sidebar 20%] [Main Content 80%]
   Fixed         Scrollable
   Width         Flexible
```

### Tablet (768px - 1200px)
```
[Sidebar] [Main Content]
  Overlay   Full Width
 (Toggle)   (Scrollable)
```

### Mobile (< 768px)
```
[Main Content]
  Full Width
  Scrollable
[Sidebar Hidden]
  (Hamburger Menu)
```

---

## Icon Legend

```
🛰️  Satellite / Main Title
📊  Analysis / Charts
🖼️  Gallery / Images
📈  Statistics / Metrics
🔧  Configuration / Settings
📁  Files / Folders
📤  Upload
📥  Download
🚀  Run / Execute
🗑️  Delete / Remove
📅  Calendar / Date
🔴  Change / Alert
🟢  Success / Unchanged
⚙️  Settings
✅  Complete / Success
⚠️  Warning
❌  Error
💾  Save / Export
🔍  Search / Zoom
📋  List / Table
🎨  Visualization
🌿  Vegetation
🔥  Heat / Intensity
```

---

## Keyboard Shortcuts (Future)

```
Ctrl + U  →  Upload images
Ctrl + R  →  Run analysis
Ctrl + E  →  Export results
Ctrl + C  →  Clear all
Tab       →  Switch tabs
Esc       →  Close dialogs
```

---

## Loading States

### Upload Loading
```
┌──────────────────┐
│  Uploading...    │
│  ████████░░░░  │
│  65% Complete    │
└──────────────────┘
```

### Analysis Loading
```
┌──────────────────┐
│  🔄 Processing   │
│  Analyzing       │
│  satellite       │
│  images...       │
└──────────────────┘
```

### Success State
```
┌──────────────────┐
│  ✅ Success!     │
│  Analysis        │
│  completed       │
└──────────────────┘
```

---

## Error States

### Upload Error
```
┌──────────────────┐
│  ❌ Upload Failed│
│  File too large  │
│  or wrong format │
│  [Try Again]     │
└──────────────────┘
```

### Analysis Error
```
┌──────────────────┐
│  ❌ Error        │
│  Images have     │
│  different sizes │
│  or formats      │
└──────────────────┘
```

---

This visual guide helps you understand the complete UI structure and user experience! 🎨✨
