---
description: Set up a full ZBRAIN OS — sovereign AI-ready knowledge operating system in Obsidian. Runs onboarding questions, creates the full 24-folder structure, governance rules, agent personas, galaxy files, CLAUDE.md boot sequence, and Universe Canvas.
---

# /zbrain-setup

You are setting up a **ZBRAIN OS** — a sovereign knowledge operating system that turns a business or founder's scattered knowledge into a structured, AI-ready system.

This is not an Obsidian tutorial. This is a methodology that makes knowledge compoundable, AI agents governable, and businesses less dependent on individuals holding information in their heads.

---

## STEP 1 — ONBOARDING QUESTIONS

Before building anything, ask the user these questions. Wait for answers before proceeding.

```
I'll ask you 12 questions. Your answers generate a custom OS.
Short answers are fine — we can refine later.

1. What is your name? (This becomes the vault owner)

2. What is the primary business this OS is for?
   (e.g., "Pet Relocation agency", "Law firm", "SaaS startup")

3. What industry are you in?
   (e.g., "Professional services", "E-commerce", "Content/Media")

4. List your active projects or departments (comma-separated):
   (e.g., "SEO, Client onboarding, Content production, Finance")

5. What AI tools do you currently use or plan to use?
   (e.g., "Claude Code, ChatGPT, Perplexity, Zapier")

6. What information must NEVER be accessible to AI agents?
   (e.g., "Medical records", "Financial passwords", "Client personal data")

7. What is the most expensive knowledge problem you have right now?
   (e.g., "Staff leave and take knowledge with them",
    "AI output can't be trusted", "Nobody knows where anything is")

8. Do you have any existing knowledge systems to migrate?
   (e.g., "Notion workspace", "Google Drive folder", "Code project")

9. Where should the vault live?
   (e.g., "C:\Users\[NAME]\ZBRAIN_MASTER" or "~/zbrain")

10. Which galaxies are most important to you right now? (pick 2-3)
    Business / Personal / AI / Knowledge / Finance / Health / Spiritual

11. What does success look like in 12 months for this system?
    (e.g., "Every AI session starts with full context automatically")

12. Do you want the SEO/GEO Engine knowledge graph imported?
    (yes = runs graphify on an external project folder)
    yes / no
```

---

## STEP 2 — CONFIRM VAULT PATH

Tell the user:

```
I'll create your vault at: [VAULT_PATH]

This will create:
- 24 structured folders
- 11 governance rule files
- 7 galaxy files (one per galaxy they selected)
- 7 AI agent persona files
- 11 World State files
- 8 Civilization files
- 1 CLAUDE.md boot sequence
- 1 Universe Canvas
- 1 ZBRAIN_OS.md master index

Estimated time: ~3 minutes

Proceed? (yes to continue)
```

---

## STEP 3 — CREATE FOLDER STRUCTURE

Use PowerShell (Windows) or Bash (Mac/Linux) to create the full structure.

### Windows (PowerShell)

```powershell
$vault = "[VAULT_PATH]"
$folders = @(
    "00_INBOX\Captures", "00_INBOX\Voice_Notes", "00_INBOX\Images",
    "00_INBOX\Screenshots", "00_INBOX\PDFs", "00_INBOX\Documents",
    "00_INBOX\Emails", "00_INBOX\WhatsApp", "00_INBOX\OCR", "00_INBOX\Processing",
    "01_UNIVERSE\Galaxies", "01_UNIVERSE\Worlds", "01_UNIVERSE\Systems",
    "01_UNIVERSE\Connections", "01_UNIVERSE\Stargates", "01_UNIVERSE\Universe_Maps",
    "10_THINKING\Master_MOCs", "10_THINKING\Frameworks", "10_THINKING\Mental_Models",
    "10_THINKING\Decision_Frameworks", "10_THINKING\Systems_Thinking",
    "10_THINKING\Research_Questions", "10_THINKING\Whiteboards",
    "10_THINKING\Brainstorms", "10_THINKING\Opportunities", "10_THINKING\Risks",
    "20_REFERENCE\Books", "20_REFERENCE\Research_Papers", "20_REFERENCE\Reports",
    "20_REFERENCE\Government_Sources", "20_REFERENCE\Regulations",
    "20_REFERENCE\Standards", "20_REFERENCE\Competitors", "20_REFERENCE\APIs",
    "20_REFERENCE\Templates", "20_REFERENCE\Checklists", "20_REFERENCE\Glossaries",
    "30_CREATING\Businesses", "30_CREATING\Websites", "30_CREATING\Blogs",
    "30_CREATING\Landing_Pages", "30_CREATING\Reports", "30_CREATING\Videos",
    "30_CREATING\Assets", "30_CREATING\Campaigns", "30_CREATING\Deliverables",
    "40_PUBLISHED\Websites", "40_PUBLISHED\Articles", "40_PUBLISHED\Videos",
    "40_PUBLISHED\PDFs", "40_PUBLISHED\Reports", "40_PUBLISHED\Newsletters",
    "40_PUBLISHED\Social", "40_PUBLISHED\Assets", "40_PUBLISHED\Archives",
    "50_ARCHIVE\Projects", "50_ARCHIVE\Research", "50_ARCHIVE\Businesses",
    "50_ARCHIVE\Ideas", "50_ARCHIVE\Systems", "50_ARCHIVE\Legacy",
    "60_SYSTEMS\Global_Rules", "60_SYSTEMS\Personas", "60_SYSTEMS\System_Prompts",
    "60_SYSTEMS\Instructions", "60_SYSTEMS\Memory_Rules", "60_SYSTEMS\Tool_Definitions",
    "60_SYSTEMS\Agents", "60_SYSTEMS\Workflows", "60_SYSTEMS\Automations",
    "60_SYSTEMS\Scripts", "60_SYSTEMS\Templates", "60_SYSTEMS\Integrations",
    "70_PROJECTS\Active", "70_PROJECTS\Planned", "70_PROJECTS\Waiting",
    "70_PROJECTS\Blocked", "70_PROJECTS\Review", "70_PROJECTS\Completed",
    "70_PROJECTS\Cancelled",
    "80_JOURNAL\Daily", "80_JOURNAL\Weekly", "80_JOURNAL\Monthly",
    "80_JOURNAL\Quarterly", "80_JOURNAL\Annual", "80_JOURNAL\Reviews",
    "90_PERSONAL\Identity", "90_PERSONAL\Life_OS", "90_PERSONAL\Health",
    "90_PERSONAL\Relationships", "90_PERSONAL\Finance", "90_PERSONAL\Learning",
    "90_PERSONAL\Goals", "90_PERSONAL\Experiences", "90_PERSONAL\Personal_Memory",
    "90_PERSONAL\Allowed_Context", "90_PERSONAL\Private_Hidden",
    "91_TRACKING\Business", "91_TRACKING\Personal", "91_TRACKING\Projects",
    "91_TRACKING\Operations",
    "92_AUDIT\Decision_Audits", "92_AUDIT\Project_Audits", "92_AUDIT\Retrospectives",
    "93_SCORECARDS\Projects", "93_SCORECARDS\Businesses", "93_SCORECARDS\Systems",
    "94_OBSERVABILITY\Dashboards", "94_OBSERVABILITY\Reports", "94_OBSERVABILITY\Metrics",
    "95_MEMORY\Decisions", "95_MEMORY\Lessons", "95_MEMORY\Mistakes",
    "95_MEMORY\Discoveries", "95_MEMORY\Rules", "95_MEMORY\Patterns",
    "95_MEMORY\Playbooks", "95_MEMORY\Best_Practices",
    "96_CIVILIZATION", "97_GOVERNANCE_QA\Policies", "97_GOVERNANCE_QA\Procedures",
    "97_GOVERNANCE_QA\Standards", "97_GOVERNANCE_QA\Compliance",
    "98_ACCESS_CONTROL\Users", "98_ACCESS_CONTROL\Roles",
    "98_ACCESS_CONTROL\Permissions", "98_ACCESS_CONTROL\Security",
    "99_WORLD_STATE",
    "ENGINES", "WORKSPACES", "graph-imports", "graphify-out"
)
foreach ($f in $folders) {
    New-Item -ItemType Directory -Force "$vault\$f" | Out-Null
}
Write-Host "Folder structure created."
```

### Mac/Linux (Bash)

```bash
VAULT="[VAULT_PATH]"
mkdir -p "$VAULT"/{00_INBOX/{Captures,Voice_Notes,Images,Screenshots,PDFs,Documents,Emails,WhatsApp,OCR,Processing},01_UNIVERSE/{Galaxies,Worlds,Systems,Connections,Stargates,Universe_Maps},10_THINKING/{Master_MOCs,Frameworks,Mental_Models,Decision_Frameworks,Systems_Thinking,Research_Questions,Whiteboards,Brainstorms,Opportunities,Risks},20_REFERENCE/{Books,Research_Papers,Reports,Government_Sources,Regulations,Standards,Competitors,APIs,Templates,Checklists,Glossaries},30_CREATING/{Businesses,Websites,Blogs,Landing_Pages,Reports,Videos,Assets,Campaigns,Deliverables},40_PUBLISHED/{Websites,Articles,Videos,PDFs,Reports,Newsletters,Social,Assets,Archives},50_ARCHIVE/{Projects,Research,Businesses,Ideas,Systems,Legacy},60_SYSTEMS/{Global_Rules,Personas,System_Prompts,Instructions,Memory_Rules,Tool_Definitions,Agents,Workflows,Automations,Scripts,Templates,Integrations},70_PROJECTS/{Active,Planned,Waiting,Blocked,Review,Completed,Cancelled},80_JOURNAL/{Daily,Weekly,Monthly,Quarterly,Annual,Reviews},90_PERSONAL/{Identity,Life_OS,Health,Relationships,Finance,Learning,Goals,Experiences,Personal_Memory,Allowed_Context,Private_Hidden},91_TRACKING/{Business,Personal,Projects,Operations},92_AUDIT/{Decision_Audits,Project_Audits,Retrospectives},93_SCORECARDS/{Projects,Businesses,Systems},94_OBSERVABILITY/{Dashboards,Reports,Metrics},95_MEMORY/{Decisions,Lessons,Mistakes,Discoveries,Rules,Patterns,Playbooks,Best_Practices},96_CIVILIZATION,97_GOVERNANCE_QA/{Policies,Procedures,Standards,Compliance},98_ACCESS_CONTROL/{Users,Roles,Permissions,Security},99_WORLD_STATE,ENGINES,WORKSPACES,graph-imports,graphify-out}
echo "Folder structure created."
```

---

## STEP 4 — INITIALIZE GIT

**This is critical** — git init creates a VCS boundary that tools like graphify respect.

```bash
cd [VAULT_PATH]
git init
git add .
git commit -m "Initial ZBRAIN OS structure"
```

---

## STEP 5 — CREATE CLAUDE.md

Use the template from `60_SYSTEMS/System_Prompts/ZBRAIN_OS_Master_Prompt.md`.

Replace all placeholders with the onboarding answers from Step 1.

Customise Section 13 (Domain Knowledge) with industry-specific context from the onboarding answers.

---

## STEP 6 — CREATE CORE FILES

Create these files using the standard metadata template, customised for this owner:

### Priority 1 — Must exist before first AI session
- `99_WORLD_STATE/Current_Reality.md`
- `99_WORLD_STATE/Active_Projects.md`
- `99_WORLD_STATE/Next_Actions.md`
- `99_WORLD_STATE/Critical_Risks.md`
- `96_CIVILIZATION/Constitution.md`
- `60_SYSTEMS/Global_Rules/00_Prime_Directive.md`
- `60_SYSTEMS/Global_Rules/08_AI_Agent_Standards.md`
- `ZBRAIN_OS.md` (master index)

### Priority 2 — Create in first session
- All remaining `99_WORLD_STATE/` files
- All `96_CIVILIZATION/` files
- All `60_SYSTEMS/Global_Rules/` files (00-10)
- All `60_SYSTEMS/Personas/` files
- All `01_UNIVERSE/Galaxies/` files (for selected galaxies)

Each file must include a **12 Month Goals** section.

---

## STEP 7 — KNOWLEDGE GRAPH (optional, requires API key)

If the user has an existing project to graph:

```bash
# Install graphify
pip install graphifyy

# Extract with Claude backend (requires ANTHROPIC_API_KEY env var)
graphify extract "[PROJECT_PATH]" --backend claude

# Export to Obsidian vault as quarantined import
graphify export obsidian --dir "[VAULT_PATH]/graph-imports/[ENGINE_NAME]/obsidian-vault"
```

Then create `graph-imports/[ENGINE_NAME]/_index.md` as the navigation portal.

---

## STEP 8 — CONFIGURE OBSIDIAN

### Register vault (Windows)

Edit `C:\Users\[USERNAME]\AppData\Roaming\obsidian\obsidian.json`:

```json
{
  "vaults": {
    "[UNIQUE_ID]": {
      "path": "[VAULT_PATH]",
      "ts": [TIMESTAMP],
      "open": true
    }
  }
}
```

### Configure Graph View

Create `.obsidian/graph.json` with colour groups for each major folder layer. Recommended settings:
- `showOrphans: true`
- `showTags: true`
- `hideUnresolved: false`
- `nodeSizeMultiplier: 1.4`
- `repelStrength: 10`
- At least one colour group per major folder layer

---

## STEP 9 — CREATE UNIVERSE CANVAS

Create `00_UNIVERSE.canvas` with:
- **Center**: ZBRAIN OS sun node with the 5 questions
- **Orbital groups**: World State, Civilization, Systems/Personas, Engines, Galaxies
- **Measure band**: 91-94 tracking/audit/scorecards/observability
- **Memory band**: 95-98 memory/governance/access
- **Knowledge layer band**: 00-50 inbox through archive
- **Personal band**: 70 projects, 80 journal, 90 personal
- **Deep space**: embedded graph canvases (if graphify was run)

---

## STEP 10 — VERIFY

After setup, run this verification checklist:

```
✓ CLAUDE.md exists and boot sequence is readable
✓ 99_WORLD_STATE/Current_Reality.md exists and is filled in
✓ 96_CIVILIZATION/Constitution.md exists
✓ 60_SYSTEMS/Global_Rules/00_Prime_Directive.md exists
✓ git status shows clean working tree
✓ Obsidian opens vault correctly
✓ Graph View (Ctrl+G) shows nodes from all major folders
✓ 00_UNIVERSE.canvas opens and shows full layout
✓ No credentials or API keys exist in any files
✓ Private folder declared in CLAUDE.md security boundary
```

If all checks pass, the system is live.

---

## WHAT TO SAY AT THE END

Tell the user:

```
Your ZBRAIN OS is live.

What was built:
- [X] folders across [N] layers
- [N] governance rule files
- [N] agent personas with explicit permissions
- [N] galaxy files with 12-month goals
- Boot sequence that loads full context in 4 reads
- Universe Canvas showing every layer of your knowledge system

Next steps:
1. Fill in 99_WORLD_STATE/Current_Reality.md — describe what is happening right now
2. Fill in the 12 Month Goals tables in each Galaxy file
3. Run graphify on any existing projects you want to import
4. Press Ctrl+G in Obsidian to see the live graph

The system answers 5 questions:
What is true? What are we doing? Is it working? What did we learn? What should change?

If it can't answer them yet — that's what to build next.
```

---

## REFERENCE

Full case study: `95_MEMORY/Playbooks/ZBRAIN_OS_Case_Study.md`
Master prompt template: `60_SYSTEMS/System_Prompts/ZBRAIN_OS_Master_Prompt.md`
Architecture spec: `ZBRAIN_OS.md`
