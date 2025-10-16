# Aurora routine workspace

This repository is a sandbox for building and testing routines with the
[Aurora framework](https://aurorabot.app/). It ships with a mirrored copy of the
public documentation so you can reference the APIs while you work, but the
project itself is focused on code rather than documentation scraping.

## Repository layout

The important top-level directories are:

| Path | Purpose |
| ---- | ------- |
| `scripts/AuroraRoutines/` | Sample routines, load order metadata, and other runtime helpers. |
| `scripts/download_aurora_docs.py` | Utility script for refreshing the offline documentation mirror. |
| `data/` | Input data used by tooling (for example the curated best practices path list). |
| `docs/` | Markdown notes maintained alongside the codebase, including best practices and the changelog. |
| `offline-docs/` | Static HTML export of the official Aurora documentation kept for quick reference. |

## Running a routine locally

You can test any routine (for example the Windwalker spec) using the standalone
Aurora client pointed at this repository. Aurora expects a specific directory
layout, a `loadorder.json` file that enumerates your Lua modules, and it
automatically supplies a namespace table when it loads each file. A minimal
Windwalker-style layout looks like this:

```
📂 scripts/
└── 📂 AuroraRoutines/
    ├── 📄 loadorder.json
    ├── 📄 Main.lua
    └── 📂 Routines/
        └── 📂 Warrior/
            └── 📂 Specialisation/
                ├── 📄 Spellbook.lua
                ├── 📄 Interface.lua
                └── 📄 Rotation.lua
```

### Step-by-step setup

1. Create the directory skeleton and `loadorder.json` (run these from the
   repository root if they do not already exist):

   ```bash
   mkdir -p scripts/AuroraRoutines
   cat <<'JSON' > scripts/AuroraRoutines/loadorder.json
   [
       "Main",
       "Routines/Warrior/Specialisation/Spellbook",
       "Routines/Warrior/Specialisation/Interface",
       "Routines/Warrior/Specialisation/Rotation"
   ]
   JSON
   ```

   **Do not** append `.lua` to the entries in `loadorder.json`; Aurora adds the
   extension automatically while loading.
2. Fill in `Main.lua` with shared utilities or setup logic and place the
   specialization files under `scripts/AuroraRoutines/Routines/` following the
   structure above. Keep related functionality in separate files, use
   descriptive names, and maintain a logical load order so dependencies are met.
3. Remember to update `loadorder.json` whenever you add, remove, or rename
   files so that dependencies are respected and names match exactly.

**Best practices**

- Keep related functionality grouped in separate files inside `Routines/`.
- Use descriptive file names and maintain a consistent load order.
- Place shared utilities in `Main.lua` so other files can reference them.

**Common mistakes to avoid**

- Forgetting to add new files to `loadorder.json`.
- Allowing file names to drift out of sync with the load order entries.
- Loading dependencies in the wrong order, which can break references.

Aurora's dynamic loader checks that your routines directory exists, reads the
`loadorder.json`, and then loads each file in the specified order. It injects
your namespace as the first argument, so your Lua files can attach behavior
directly to it:

```lua
local YourNamespace = ...

function YourNamespace.DoSomething()
    -- routine logic here
end
```

When you're ready to test, launch the client and run `/aur load <Namespace>`.
This repository ships with a Windwalker routine that registers itself as
`Windwalker`, so you can load it with `/aur load Windwalker`. Repeat the process
for any other spec by adjusting the namespace and file structure to match.

## Working with the offline docs

The mirrored site lives under `offline-docs/`. The HTML was captured directly
from the live documentation and assumes it is served from the web root. Because
the full copy is already committed to this repository you can browse it offline
without downloading anything. Point a tiny HTTP server at the directory:

```bash
python3 -m http.server --directory offline-docs 9000
```

and then open <http://localhost:9000/> in your browser.

To update the mirror, run the downloader script from a machine with internet
access:

```bash
python3 scripts/download_aurora_docs.py offline-docs
```

The script prints every fetched URL as it runs, making it straightforward to
spot missing pages or assets. Pass `--format markdown` if you want to refresh
the Markdown notes under `docs/best-practices/` instead.
