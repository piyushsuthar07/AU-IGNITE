# AU-IGNITE
Team project repository for developing, tracking, and maintaining all code and documentation.


## 📌 Quick Overview

- The **admin publishes tasks** (markdown files) in the `main` branch.
- Each member completes the task **in their personal branch only**.
- ❗ **No member is allowed to merge anything into main.**
- ❗ **Do not edit or push to another member’s branch.**

## 📄 Task Files (Naming Rules)

Tasks appear in main as Markdown files:
task1.md
task2.md
task3.md


The admin will announce which task to complete (e.g., *“Complete task2.md”*).

If starter code is required, it will be provided inside or alongside the task file.

---

## 📁 Repository Structure (Example)
main/ → Admin only (tasks like task1.md, task2.md)
└── task1.md
└── task2.md

piyush-suthar/ → Member branch
nishant-kumawat/
Pratik/
hema-negi/
Faijan/


Every member has **one dedicated branch**.  
Branches must remain separate — **no cross-branch modifications**.

---

## 🔐 Branch Rules & Permissions

### **Main Branch (`main`)**
- Admin-only access
- Members **must NOT**:
  - push changes  
  - edit files  
  - merge anything into main  

### **Member Branches (Example: `shubham`)**
- Work ONLY in your branch
- Push ONLY to your branch
- Don’t touch other members’ branches
- Don’t merge branches or create PRs
- Don’t create new branches without admin approval

> ⚠ Even if GitHub doesn't restrict it technically, these rules MUST be followed.  
> The admin will revert incorrect commits.

---


## 🚀 How to Submit Your Assignment
## 🔀 Git Branch Workflow Diagram

```mermaid
flowchart TD

    A[Admin Creates Repo] --> B[Admin Creates Member Branches]
    B --> C[Admin Publishes Task Files in main]

    C --> D[Member Clones Repository]
    D --> E[Member Fetches All Branches]
    E --> F[Member Switches to Own Branch]

    F --> G[Member Completes Assignment in Own Branch]
    G --> H[Member Adds & Commits Code]
    H --> I[Member Pushes Code to Their Branch]

    I --> J[Admin Reviews Work in Each Member Branch]
    J --> K[Admin Updates main When Needed]

    style A fill:#ffd280,stroke:#000
    style B fill:#ffd280,stroke:#000
    style C fill:#ffd280,stroke:#000

    style D fill:#b3e6ff,stroke:#000
    style E fill:#b3e6ff,stroke:#000
    style F fill:#b3e6ff,stroke:#000
    style G fill:#b3e6ff,stroke:#000
    style H fill:#b3e6ff,stroke:#000
    style I fill:#b3e6ff,stroke:#000

    style J fill:#c6ffb3,stroke:#000
    style K fill:#c6ffb3,stroke:#000
```
### 1️⃣ Clone the repository
```bash
git clone <repo-url>
cd <repo-folder>

