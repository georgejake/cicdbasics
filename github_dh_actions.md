### GitHub Actions & DockerHub

#### Folder structure for github actions 
github specifically looks for this folder in your root
your-repo/
└── .github/
    └── workflows/
        └── ci.yml        ← create this 


#### Push to main vs Pull Request to main
on: pull_request (targeting main)When a PR is opened, updated, or reopened — before merge
on: push (to main)When code actually lands on main — after merge
#### My strategy
Since I merge PRs into main, a merge IS a push to main 
Local → dev branch → PR to main → Merge → main
                         ↑               ↑
                   PR trigger fires   Push trigger fires
#### Why we should use PR Trigger
    - pull_request --> Running tests/linting before merge (gate check)
    - push to main ---> Building & pushing Docker image after merge (actual CI artifact)

#### How Github Action work in this project

You merge PR to main
        │
        ▼
GitHub Actions VM spins up (ubuntu-latest)
        │
        ├── 1. Pulls your repo code
        │
        ├── 2. Logs into DockerHub (using your secrets)
        │
        ├── 3. Builds Docker image (runs your Dockerfile)
        │
        └── 4. Pushes image → DockerHub (yourname/fastapi-app:latest)

#### Expression Wrapper in ci.yaml

The anatomy of ${{ secrets.DOCKERHUB_USERNAME }}
It has 3 distinct parts:
${{  secrets.DOCKERHUB_USERNAME  }}
 ↑       ↑           ↑
 │       │           └── The secret's name (you defined this in GitHub Settings)
 │       └────────────── The "context" — where GitHub is looking
 └────────────────────── Expression syntax — tells GitHub "evaluate this"

    - secrets is context object in github. There are many other context available in github
        - github --> ${{ github.actor }}
        - env --> ${{ env.MY_VAR }}
        - runner --> ${{ runner.os }}
    quick mental model
    ${{ context.KEY }}
     │       │
     │       └── specific variable inside that context
     └── which "bag" to look in (secrets / github / env / runner)

#### How DockerHub image naming actually works
In DockerHub, the image tag itself encodes everything — your username, repository name, and version tag all in one string.

johndoe  /  mydockerexp  :  latest

   ↑             ↑             ↑

username    repository      version

(your DH    (you created     tag

 account)    this in DH)

#### Add DockerHub Secrets to GitHub

Before the workflow, you need to store your DockerHub credentials safely in GitHub. Never hardcode these in your YAML.Go to your GitHub repo →  Settings → Secrets and variables → Actions → New repository secret and add these two:
Secret NameValueDOCKERHUB_USERNAMEYour DockerHub usernameDOCKERHUB_TOKENA DockerHub Access Token (not your password)
    - Settings level
        - What it controls
            - Your Profile Settings (top right avatar)Your personal account references
            - Repository Settings (inside your repo)CI/CD, secrets, branches for that specific repo
Secrets live at the Repository level — not your profile.

#### Why we had to add docker/setup-buildx-action@v3
    - name: Set up Docker Buildx        # ← new step added here
        - uses: docker/setup-buildx-action@v3
GitHub Actions by default uses the docker driver to build images — and that driver does not support the type=gha cache export we added.
Think of it like this:
docker driver          →  basic car, no roof rack
                          can't carry/store cache on top

docker-container driver →  car with roof rack
                           can carry cache in and out ✅

