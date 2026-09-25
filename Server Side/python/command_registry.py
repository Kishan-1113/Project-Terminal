COMMAND_REGISTRY = {

    # ============================================================
    # REPOSITORY
    # ============================================================

    "git.init": {"template": "git init", "requires_slots": []},

    "git.init.bare": {"template": "git init --bare", "requires_slots": []},

    "git.clone": {"template": "git clone {url}", "requires_slots": ["url"], "confirm": True},

    "git.clone.directory": {"template": "git clone {url} {directory}", "requires_slots": ["url", "directory"], "confirm": True},

    "git.status": {"template": "git status", "requires_slots": []},

    "git.status.short": {"template": "git status --short", "requires_slots": []},

    "git.status.branch": {"template": "git status --branch --short", "requires_slots": []},


    # ============================================================
    # BRANCHES
    # ============================================================

    "git.branch.list": {"template": "git branch -a", "requires_slots": []},

    "git.branch.list.local": {"template": "git branch", "requires_slots": []},

    "git.branch.list.remote": {"template": "git branch -r", "requires_slots": []},

    "git.branch.list.verbose": {"template": "git branch -vv", "requires_slots": []},

    "git.branch.current": {"template": "git branch --show-current", "requires_slots": []},

    "git.branch.create": {"template": "git checkout -b {branch_name}", "requires_slots": ["branch_name"]},

    "git.branch.create.from": {"template": "git checkout -b {branch_name} {start_point}", "requires_slots": ["branch_name", "start_point"]},

    "git.branch.delete": {"template": "git branch -d {branch_name}", "requires_slots": ["branch_name"], "confirm": True},

    "git.branch.delete.force": {"template": "git branch -D {branch_name}", "requires_slots": ["branch_name"], "confirm": True},

    "git.branch.rename": {"template": "git branch -m {old_name} {new_name}", "requires_slots": ["old_name", "new_name"], "confirm": True},

    "git.branch.rename.current": {"template": "git branch -m {new_name}", "requires_slots": ["new_name"], "confirm": True},

    "git.branch.switch": {"template": "git switch {branch_name}", "requires_slots": ["branch_name"]},

    "git.branch.switch.create": {"template": "git switch -c {branch_name}", "requires_slots": ["branch_name"]},

    "git.branch.switch.create.from": {"template": "git switch -c {branch_name} {start_point}", "requires_slots": ["branch_name", "start_point"]},

    "git.branch.track": {"template": "git branch --track {branch_name} {remote_branch}", "requires_slots": ["branch_name", "remote_branch"]},

    "git.branch.unset.upstream": {"template": "git branch --unset-upstream {branch_name}", "requires_slots": ["branch_name"]},

    "git.branch.set.upstream": {"template": "git branch --set-upstream-to={remote_branch} {branch_name}", "requires_slots": ["remote_branch", "branch_name"]},

    "git.branch.merged": {"template": "git branch --merged", "requires_slots": []},

    "git.branch.unmerged": {"template": "git branch --no-merged", "requires_slots": []},

    "git.branch.contains": {"template": "git branch --contains {commit}", "requires_slots": ["commit"]},

    "git.branch.no.contains": {"template": "git branch --no-contains {commit}", "requires_slots": ["commit"]},

    "git.branch.sort": {"template": "git branch --sort={field}", "requires_slots": ["field"]},


    # ============================================================
    # CHECKOUT
    # ============================================================

    "git.checkout": {"template": "git checkout {branch_name}", "requires_slots": ["branch_name"], "confirm": True},

    "git.checkout.create": {"template": "git checkout -b {branch_name}", "requires_slots": ["branch_name"]},

    "git.checkout.commit": {"template": "git checkout {commit}", "requires_slots": ["commit"], "confirm": True},

    "git.checkout.file": {"template": "git checkout {commit} -- {file}", "requires_slots": ["commit", "file"], "confirm": True},


    # ============================================================
    # ADD / STAGING
    # ============================================================

    "git.add": {"template": "git add {path}", "requires_slots": ["path"]},

    "git.add.all": {"template": "git add -A", "requires_slots": []},

    "git.add.all.current": {"template": "git add .", "requires_slots": []},

    "git.add.modified": {"template": "git add -u", "requires_slots": []},

    "git.add.interactive": {"template": "git add -i", "requires_slots": []},

    "git.add.patch": {"template": "git add -p", "requires_slots": []},

    "git.add.intent": {"template": "git add -N {path}", "requires_slots": ["path"]},

    "git.unstage": {"template": "git restore --staged {path}", "requires_slots": ["path"]},

    "git.unstage.all": {"template": "git restore --staged .", "requires_slots": []},


    # ============================================================
    # COMMIT
    # ============================================================

    "git.commit": {"template": "git commit -m \"{message}\"", "requires_slots": ["message"], "confirm": True},

    "git.commit.all": {"template": "git commit -a -m \"{message}\"", "requires_slots": ["message"], "confirm": True},

    "git.commit.amend": {"template": "git commit --amend", "requires_slots": [], "confirm": True},

    "git.commit.amend.message": {"template": "git commit --amend -m \"{message}\"", "requires_slots": ["message"], "confirm": True},

    "git.commit.no.edit": {"template": "git commit --amend --no-edit", "requires_slots": [], "confirm": True},

    "git.commit.empty": {"template": "git commit --allow-empty -m \"{message}\"", "requires_slots": ["message"], "confirm": True},

    "git.commit.signoff": {"template": "git commit -s -m \"{message}\"", "requires_slots": ["message"], "confirm": True},

    "git.commit.verbose": {"template": "git commit -v", "requires_slots": []},

    "git.commit.fixup": {"template": "git commit --fixup={commit}", "requires_slots": ["commit"], "confirm": True},


    # ============================================================
    # COMMIT HISTORY / LOG
    # ============================================================

    "git.log": {"template": "git log", "requires_slots": []},

    "git.log.oneline": {"template": "git log --oneline", "requires_slots": []},

    "git.log.graph": {"template": "git log --oneline --graph --all", "requires_slots": []},

    "git.log.all": {"template": "git log --all", "requires_slots": []},

    "git.log.recent": {"template": "git log -n {count}", "requires_slots": ["count"]},

    "git.log.author": {"template": "git log --author=\"{author}\"", "requires_slots": ["author"]},

    "git.log.file": {"template": "git log -- {file}", "requires_slots": ["file"]},

    "git.log.search.message": {"template": "git log --grep=\"{pattern}\"", "requires_slots": ["pattern"]},

    "git.log.after": {"template": "git log --after=\"{date}\"", "requires_slots": ["date"]},

    "git.log.before": {"template": "git log --before=\"{date}\"", "requires_slots": ["date"]},

    "git.log.between": {"template": "git log {from_ref}..{to_ref}", "requires_slots": ["from_ref", "to_ref"]},

    "git.log.follow": {"template": "git log --follow -- {file}", "requires_slots": ["file"]},

    "git.log.stat": {"template": "git log --stat", "requires_slots": []},

    "git.log.patch": {"template": "git log -p", "requires_slots": []},

    "git.log.first.parent": {"template": "git log --first-parent", "requires_slots": []},


    # ============================================================
    # SHOW / INSPECT COMMITS
    # ============================================================

    "git.show": {"template": "git show {commit}", "requires_slots": ["commit"]},

    "git.show.latest": {"template": "git show HEAD", "requires_slots": []},

    "git.show.stat": {"template": "git show --stat {commit}", "requires_slots": ["commit"]},

    "git.show.name": {"template": "git show --name-only {commit}", "requires_slots": ["commit"]},

    "git.show.file": {"template": "git show {commit}:{file}", "requires_slots": ["commit", "file"]},

    "git.rev.parse": {"template": "git rev-parse {ref}", "requires_slots": ["ref"]},

    "git.rev.parse.head": {"template": "git rev-parse HEAD", "requires_slots": []},


    # ============================================================
    # DIFF
    # ============================================================

    "git.diff": {"template": "git diff", "requires_slots": []},

    "git.diff.staged": {"template": "git diff --staged", "requires_slots": []},

    "git.diff.cached": {"template": "git diff --cached", "requires_slots": []},

    "git.diff.file": {"template": "git diff -- {file}", "requires_slots": ["file"]},

    "git.diff.branches": {"template": "git diff {branch1}..{branch2}", "requires_slots": ["branch1", "branch2"]},

    "git.diff.commits": {"template": "git diff {commit1} {commit2}", "requires_slots": ["commit1", "commit2"]},

    "git.diff.stat": {"template": "git diff --stat", "requires_slots": []},

    "git.diff.name.only": {"template": "git diff --name-only", "requires_slots": []},

    "git.diff.name.status": {"template": "git diff --name-status", "requires_slots": []},


    # ============================================================
    # PUSH
    # ============================================================

    "git.push": {"template": "git push", "requires_slots": [], "confirm": True},
    

    "git.push.remote": {"template": "git push {remote}", "requires_slots": ["remote"], "confirm": True},

    "git.push.branch": {"template": "git push {remote} {branch_name}", "requires_slots": ["remote", "branch_name"], "confirm": True},

    "git.push.set.upstream": {"template": "git push -u {remote} {branch_name}", "requires_slots": ["remote", "branch_name"], "confirm": True},

    "git.push.current": {"template": "git push {remote} HEAD", "requires_slots": ["remote"], "confirm": True},

    "git.push.force": {"template": "git push --force", "requires_slots": [], "confirm": True},

    "git.push.force.with.lease": {"template": "git push --force-with-lease", "requires_slots": [], "confirm": True},

    "git.push.tags": {"template": "git push {remote} --tags", "requires_slots": ["remote"], "confirm": True},

    "git.push.delete.branch": {"template": "git push {remote} --delete {branch_name}", "requires_slots": ["remote", "branch_name"], "confirm": True},


    # ============================================================
    # PULL
    # ============================================================

    "git.pull": {"template": "git pull", "requires_slots": [], "confirm": True},

    "git.pull.remote": {"template": "git pull {remote}", "requires_slots": ["remote"], "confirm": True},

    "git.pull.branch": {"template": "git pull {remote} {branch_name}", "requires_slots": ["remote", "branch_name"], "confirm": True},

    "git.pull.rebase": {"template": "git pull --rebase", "requires_slots": [], "confirm": True},

    "git.pull.no.rebase": {"template": "git pull --no-rebase", "requires_slots": [], "confirm": True},


    # ============================================================
    # FETCH
    # ============================================================

    "git.fetch": {"template": "git fetch", "requires_slots": []},

    "git.fetch.remote": {"template": "git fetch {remote}", "requires_slots": ["remote"]},

    "git.fetch.branch": {"template": "git fetch {remote} {branch_name}", "requires_slots": ["remote", "branch_name"]},

    "git.fetch.all": {"template": "git fetch --all", "requires_slots": []},

    "git.fetch.prune": {"template": "git fetch --prune", "requires_slots": []},

    "git.fetch.all.prune": {"template": "git fetch --all --prune", "requires_slots": []},


    # ============================================================
    # REMOTES
    # ============================================================

    "git.remote.list": {"template": "git remote", "requires_slots": []},

    "git.remote.verbose": {"template": "git remote -v", "requires_slots": []},

    "git.remote.add": {"template": "git remote add {name} {url}", "requires_slots": ["name", "url"], "confirm": True},

    "git.remote.remove": {"template": "git remote remove {name}", "requires_slots": ["name"], "confirm": True},

    "git.remote.rename": {"template": "git remote rename {old_name} {new_name}", "requires_slots": ["old_name", "new_name"], "confirm": True},

    "git.remote.set.url": {"template": "git remote set-url {name} {url}", "requires_slots": ["name", "url"], "confirm": True},

    "git.remote.get.url": {"template": "git remote get-url {name}", "requires_slots": ["name"]},

    "git.remote.show": {"template": "git remote show {name}", "requires_slots": ["name"]},

    "git.remote.prune": {"template": "git remote prune {name}", "requires_slots": ["name"], "confirm": True},


    # ============================================================
    # MERGE
    # ============================================================

    "git.merge": {"template": "git merge {branch_name}", "requires_slots": ["branch_name"], "confirm": True},

    "git.merge.no.commit": {"template": "git merge --no-commit {branch_name}", "requires_slots": ["branch_name"], "confirm": True},

    "git.merge.squash": {"template": "git merge --squash {branch_name}", "requires_slots": ["branch_name"], "confirm": True},

    "git.merge.abort": {"template": "git merge --abort", "requires_slots": [], "confirm": True},

    "git.merge.continue": {"template": "git merge --continue", "requires_slots": [], "confirm": True},


    # ============================================================
    # REBASE
    # ============================================================

    "git.rebase": {"template": "git rebase {branch_name}", "requires_slots": ["branch_name"], "confirm": True},

    "git.rebase.interactive": {"template": "git rebase -i {branch_name}", "requires_slots": ["branch_name"], "confirm": True},

    "git.rebase.abort": {"template": "git rebase --abort", "requires_slots": [], "confirm": True},

    "git.rebase.continue": {"template": "git rebase --continue", "requires_slots": [], "confirm": True},

    "git.rebase.skip": {"template": "git rebase --skip", "requires_slots": [], "confirm": True},

    "git.rebase.autosquash": {"template": "git rebase -i --autosquash {branch_name}", "requires_slots": ["branch_name"], "confirm": True},


    # ============================================================
    # RESET
    # ============================================================

    "git.reset": {"template": "git reset --hard", "requires_slots": [], "confirm": True},

    "git.reset.soft": {"template": "git reset --soft {commit}", "requires_slots": ["commit"], "confirm": True},

    "git.reset.mixed": {"template": "git reset --mixed {commit}", "requires_slots": ["commit"], "confirm": True},

    "git.reset.hard.commit": {"template": "git reset --hard {commit}", "requires_slots": ["commit"], "confirm": True},

    "git.reset.file": {"template": "git reset {file}", "requires_slots": ["file"], "confirm": True},

    "git.reset.head": {"template": "git reset HEAD", "requires_slots": [], "confirm": True},


    # ============================================================
    # RESTORE
    # ============================================================

    "git.restore": {"template": "git restore {file}", "requires_slots": ["file"], "confirm": True},

    "git.restore.all": {"template": "git restore .", "requires_slots": [], "confirm": True},

    "git.restore.staged": {"template": "git restore --staged {file}", "requires_slots": ["file"]},

    "git.restore.staged.all": {"template": "git restore --staged .", "requires_slots": []},

    "git.restore.source": {"template": "git restore --source={commit} {file}", "requires_slots": ["commit", "file"], "confirm": True},


    # ============================================================
    # REVERT
    # ============================================================

    "git.revert": {"template": "git revert {commit}", "requires_slots": ["commit"], "confirm": True},

    "git.revert.no.edit": {"template": "git revert --no-edit {commit}", "requires_slots": ["commit"], "confirm": True},

    "git.revert.abort": {"template": "git revert --abort", "requires_slots": [], "confirm": True},

    "git.revert.continue": {"template": "git revert --continue", "requires_slots": [], "confirm": True},


    # ============================================================
    # STASH
    # ============================================================

    "git.stash": {"template": "git stash", "requires_slots": []},

    "git.stash.push": {"template": "git stash push", "requires_slots": []},

    "git.stash.message": {"template": "git stash push -m \"{message}\"", "requires_slots": ["message"]},

    "git.stash.include.untracked": {"template": "git stash push -u", "requires_slots": []},

    "git.stash.all": {"template": "git stash push -a", "requires_slots": []},

    "git.stash.list": {"template": "git stash list", "requires_slots": []},

    "git.stash.show": {"template": "git stash show {stash}", "requires_slots": ["stash"]},

    "git.stash.show.patch": {"template": "git stash show -p {stash}", "requires_slots": ["stash"]},

    "git.stash.apply": {"template": "git stash apply {stash}", "requires_slots": ["stash"]},

    "git.stash.pop": {"template": "git stash pop {stash}", "requires_slots": ["stash"]},

    "git.stash.drop": {"template": "git stash drop {stash}", "requires_slots": ["stash"], "confirm": True},

    "git.stash.clear": {"template": "git stash clear", "requires_slots": [], "confirm": True},

    "git.stash.branch": {"template": "git stash branch {branch_name} {stash}", "requires_slots": ["branch_name", "stash"], "confirm": True},


    # ============================================================
    # TAGS
    # ============================================================

    "git.tag.list": {"template": "git tag", "requires_slots": []},

    "git.tag.list.pattern": {"template": "git tag -l \"{pattern}\"", "requires_slots": ["pattern"]},

    "git.tag.create": {"template": "git tag {tag_name}", "requires_slots": ["tag_name"]},

    "git.tag.create.annotated": {"template": "git tag -a {tag_name} -m \"{message}\"", "requires_slots": ["tag_name", "message"]},

    "git.tag.create.commit": {"template": "git tag {tag_name} {commit}", "requires_slots": ["tag_name", "commit"]},

    "git.tag.show": {"template": "git show {tag_name}", "requires_slots": ["tag_name"]},

    "git.tag.delete": {"template": "git tag -d {tag_name}", "requires_slots": ["tag_name"], "confirm": True},

    "git.tag.push": {"template": "git push {remote} {tag_name}", "requires_slots": ["remote", "tag_name"], "confirm": True},

    "git.tag.push.all": {"template": "git push {remote} --tags", "requires_slots": ["remote"], "confirm": True},


    # ============================================================
    # FILE REMOVAL / TRACKING
    # ============================================================

    "git.rm": {"template": "git rm {file}", "requires_slots": ["file"], "confirm": True},

    "git.rm.cached": {"template": "git rm --cached {file}", "requires_slots": ["file"], "confirm": True},

    "git.rm.recursive": {"template": "git rm -r {directory}", "requires_slots": ["directory"], "confirm": True},

    "git.mv": {"template": "git mv {source} {destination}", "requires_slots": ["source", "destination"], "confirm": True},

    "git.ls.files": {"template": "git ls-files", "requires_slots": []},

    "git.ls.files.modified": {"template": "git ls-files -m", "requires_slots": []},

    "git.ls.files.others": {"template": "git ls-files --others --exclude-standard", "requires_slots": []},


    # ============================================================
    # CLEAN
    # ============================================================

    "git.clean": {"template": "git clean -n", "requires_slots": []},

    "git.clean.files": {"template": "git clean -f", "requires_slots": [], "confirm": True},

    "git.clean.directories": {"template": "git clean -fd", "requires_slots": [], "confirm": True},

    "git.clean.ignored": {"template": "git clean -fdX", "requires_slots": [], "confirm": True},

    "git.clean.all": {"template": "git clean -fdx", "requires_slots": [], "confirm": True},


    # ============================================================
    # BLAME
    # ============================================================

    "git.blame": {"template": "git blame {file}", "requires_slots": ["file"]},

    "git.blame.line": {"template": "git blame -L {start},{end} {file}", "requires_slots": ["start", "end", "file"]},

    "git.blame.revision": {"template": "git blame {commit} -- {file}", "requires_slots": ["commit", "file"]},


    # ============================================================
    # CHERRY PICK
    # ============================================================

    "git.cherry.pick": {"template": "git cherry-pick {commit}", "requires_slots": ["commit"], "confirm": True},

    "git.cherry.pick.no.commit": {"template": "git cherry-pick -n {commit}", "requires_slots": ["commit"], "confirm": True},

    "git.cherry.pick.abort": {"template": "git cherry-pick --abort", "requires_slots": [], "confirm": True},

    "git.cherry.pick.continue": {"template": "git cherry-pick --continue", "requires_slots": [], "confirm": True},

    "git.cherry.pick.skip": {"template": "git cherry-pick --skip", "requires_slots": [], "confirm": True},


    # ============================================================
    # REFL​​OG
    # ============================================================

    "git.reflog": {"template": "git reflog", "requires_slots": []},

    "git.reflog.all": {"template": "git reflog --all", "requires_slots": []},

    "git.reflog.branch": {"template": "git reflog {branch_name}", "requires_slots": ["branch_name"]},


    # ============================================================
    # BISect
    # ============================================================

    "git.bisect.start": {"template": "git bisect start", "requires_slots": [], "confirm": True},

    "git.bisect.good": {"template": "git bisect good {commit}", "requires_slots": ["commit"]},

    "git.bisect.bad": {"template": "git bisect bad {commit}", "requires_slots": ["commit"]},

    "git.bisect.skip": {"template": "git bisect skip", "requires_slots": []},

    "git.bisect.reset": {"template": "git bisect reset", "requires_slots": [], "confirm": True},

    "git.bisect.log": {"template": "git bisect log", "requires_slots": []},

    "git.bisect.run": {"template": "git bisect run {command}", "requires_slots": ["command"], "confirm": True},


    # ============================================================
    # REMOTE BRANCHES
    # ============================================================

    "git.remote.branch.list": {"template": "git branch -r", "requires_slots": []},

    "git.remote.branch.delete": {"template": "git push {remote} --delete {branch_name}", "requires_slots": ["remote", "branch_name"], "confirm": True},

    "git.remote.branch.prune": {"template": "git fetch --prune", "requires_slots": []},


    # ============================================================
    # CONFIGURATION
    # ============================================================

    "git.config.list": {"template": "git config --list", "requires_slots": []},

    "git.config.global.list": {"template": "git config --global --list", "requires_slots": []},

    "git.config.get": {"template": "git config --get {key}", "requires_slots": ["key"]},

    "git.config.get.global": {"template": "git config --global --get {key}", "requires_slots": ["key"]},

    "git.config.set": {"template": "git config {key} \"{value}\"", "requires_slots": ["key", "value"]},

    "git.config.set.global": {"template": "git config --global {key} \"{value}\"", "requires_slots": ["key", "value"]},

    "git.config.unset": {"template": "git config --unset {key}", "requires_slots": ["key"], "confirm": True},

    "git.config.unset.global": {"template": "git config --global --unset {key}", "requires_slots": ["key"], "confirm": True},

    "git.config.user.name": {"template": "git config --global user.name \"{name}\"", "requires_slots": ["name"]},

    "git.config.user.email": {"template": "git config --global user.email \"{email}\"", "requires_slots": ["email"]},

    "git.config.editor": {"template": "git config --global core.editor \"{editor}\"", "requires_slots": ["editor"]},


    # ============================================================
    # SUBMODULES
    # ============================================================

    "git.submodule.list": {"template": "git submodule", "requires_slots": []},

    "git.submodule.add": {"template": "git submodule add {url} {path}", "requires_slots": ["url", "path"], "confirm": True},

    "git.submodule.init": {"template": "git submodule init", "requires_slots": []},

    "git.submodule.update": {"template": "git submodule update", "requires_slots": []},

    "git.submodule.update.init": {"template": "git submodule update --init", "requires_slots": []},

    "git.submodule.update.recursive": {"template": "git submodule update --init --recursive", "requires_slots": []},

    "git.submodule.sync": {"template": "git submodule sync", "requires_slots": []},

    "git.submodule.deinit": {"template": "git submodule deinit {path}", "requires_slots": ["path"], "confirm": True},


    # ============================================================
    # WORKTREES
    # ============================================================

    "git.worktree.list": {"template": "git worktree list", "requires_slots": []},

    "git.worktree.add": {"template": "git worktree add {path} {branch_name}", "requires_slots": ["path", "branch_name"], "confirm": True},

    "git.worktree.add.create": {"template": "git worktree add -b {branch_name} {path}", "requires_slots": ["branch_name", "path"], "confirm": True},

    "git.worktree.remove": {"template": "git worktree remove {path}", "requires_slots": ["path"], "confirm": True},

    "git.worktree.prune": {"template": "git worktree prune", "requires_slots": [], "confirm": True},


    # ============================================================
    # ARCHIVE
    # ============================================================

    "git.archive": {"template": "git archive {ref}", "requires_slots": ["ref"]},

    "git.archive.zip": {"template": "git archive --format=zip --output={file}.zip {ref}", "requires_slots": ["file", "ref"]},

    "git.archive.tar": {"template": "git archive --format=tar --output={file}.tar {ref}", "requires_slots": ["file", "ref"]},


    # ============================================================
    # DIAGNOSTICS
    # ============================================================

    "git.version": {"template": "git --version", "requires_slots": []},

    "git.help": {"template": "git help {command}", "requires_slots": ["command"]},

    "git.command.help": {"template": "git {command} --help", "requires_slots": ["command"]},

    "git.check.ignore": {"template": "git check-ignore {path}", "requires_slots": ["path"]},

    "git.check.attr": {"template": "git check-attr {attribute} -- {path}", "requires_slots": ["attribute", "path"]},

    "git.count.objects": {"template": "git count-objects -v", "requires_slots": []},

    "git.fsck": {"template": "git fsck", "requires_slots": []},

    "git.verify.pack": {"template": "git verify-pack {pack_file}", "requires_slots": ["pack_file"]},


    # ============================================================
    # SHORTCUTS / ALIASES
    # ============================================================

    "git.alias.list": {"template": "git config --get-regexp '^alias\\.'", "requires_slots": []},

    "git.alias.set": {"template": "git config --global alias.{name} \"{command}\"", "requires_slots": ["name", "command"]},

    "git.alias.remove": {"template": "git config --global --unset alias.{name}", "requires_slots": ["name"], "confirm": True},


    # ============================================================
    # GIT NOTES
    # ============================================================

    "git.notes.list": {"template": "git notes list", "requires_slots": []},

    "git.notes.show": {"template": "git notes show {commit}", "requires_slots": ["commit"]},

    "git.notes.add": {"template": "git notes add -m \"{message}\" {commit}", "requires_slots": ["message", "commit"]},

    "git.notes.remove": {"template": "git notes remove {commit}", "requires_slots": ["commit"], "confirm": True},


    # ============================================================
    # GIT LFS
    # ============================================================

    "git.lfs.install": {"template": "git lfs install", "requires_slots": []},

    "git.lfs.track": {"template": "git lfs track \"{pattern}\"", "requires_slots": ["pattern"]},

    "git.lfs.untrack": {"template": "git lfs untrack \"{pattern}\"", "requires_slots": ["pattern"], "confirm": True},

    "git.lfs.list": {"template": "git lfs ls-files", "requires_slots": []},

    "git.lfs.pull": {"template": "git lfs pull", "requires_slots": [], "confirm": True},

    "git.lfs.push": {"template": "git lfs push {remote} {branch_name}", "requires_slots": ["remote", "branch_name"], "confirm": True},


    # ============================================================
    # PATCHES
    # ============================================================

    "git.format.patch": {"template": "git format-patch {commit}", "requires_slots": ["commit"]},

    "git.apply": {"template": "git apply {patch}", "requires_slots": ["patch"], "confirm": True},

    "git.apply.check": {"template": "git apply --check {patch}", "requires_slots": ["patch"]},

    "git.am": {"template": "git am {patch}", "requires_slots": ["patch"], "confirm": True},

    "git.am.abort": {"template": "git am --abort", "requires_slots": [], "confirm": True},

    "git.am.continue": {"template": "git am --continue", "requires_slots": [], "confirm": True},


    # ============================================================
    # TAG / VERSION DESCRIBE
    # ============================================================

    "git.describe": {"template": "git describe", "requires_slots": []},

    "git.describe.tags": {"template": "git describe --tags", "requires_slots": []},

    "git.describe.always": {"template": "git describe --always", "requires_slots": []},


    # ============================================================
    # HASH / OBJECT OPERATIONS
    # ============================================================

    "git.hash.object": {"template": "git hash-object {file}", "requires_slots": ["file"]},

    "git.cat.file": {"template": "git cat-file -p {object}", "requires_slots": ["object"]},

    "git.show.ref": {"template": "git show-ref", "requires_slots": []},

    "git.for.each.ref": {"template": "git for-each-ref", "requires_slots": []},


    # ============================================================
    # GIT RERERE
    # ============================================================

    "git.rerere.status": {"template": "git rerere status", "requires_slots": []},

    "git.rerere.diff": {"template": "git rerere diff", "requires_slots": []},

    "git.rerere.enabled": {"template": "git config rerere.enabled true", "requires_slots": []},


    # ============================================================
    # CONTAINERS
    # ============================================================

    "docker.container.list": {"template": "docker ps","requires_slots": []},
    "docker.container.list.all": {"template": "docker ps -a","requires_slots":[]},

    "docker.container.run": {"template": "docker run {image}","requires_slots": ["image"],     "confirm": True
    },

    "docker.container.run.name": {
        "template": "docker run --name {container_name} {image}",
        "requires_slots": ["container_name", "image"],
        "confirm": True
    },

    "docker.container.run.port": {
        "template": "docker run -p {host_port}:{container_port} {image}",
        "requires_slots": ["host_port", "container_port", "image"],
        "confirm": True
    },

    "docker.container.run.detached": {
        "template": "docker run -d {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.container.run.interactive": {
        "template": "docker run -it {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.container.start": {
        "template": "docker start {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.container.stop": {
        "template": "docker stop {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.container.restart": {
        "template": "docker restart {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.container.pause": {
        "template": "docker pause {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.container.unpause": {
        "template": "docker unpause {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.container.kill": {
        "template": "docker kill {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.container.remove": {
        "template": "docker rm {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.container.remove.force": {
        "template": "docker rm -f {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.container.inspect": {
        "template": "docker inspect {container}",
        "requires_slots": ["container"]
    },

    "docker.container.logs": {
        "template": "docker logs {container}",
        "requires_slots": ["container"]
    },

    "docker.container.logs.follow": {
        "template": "docker logs -f {container}",
        "requires_slots": ["container"]
    },

    "docker.container.logs.tail": {
        "template": "docker logs --tail {lines} {container}",
        "requires_slots": ["lines", "container"]
    },

    "docker.container.stats": {
        "template": "docker stats {container}",
        "requires_slots": ["container"]
    },

    "docker.container.top": {
        "template": "docker top {container}",
        "requires_slots": ["container"]
    },

    "docker.container.exec": {
        "template": "docker exec {container} {command}",
        "requires_slots": ["container", "command"],
        "confirm": True
    },

    "docker.container.exec.interactive": {
        "template": "docker exec -it {container} {command}",
        "requires_slots": ["container", "command"],
        "confirm": True
    },

    "docker.container.rename": {
        "template": "docker rename {old_name} {new_name}",
        "requires_slots": ["old_name", "new_name"],
        "confirm": True
    },

    "docker.container.cp.to": {
        "template": "docker cp {source} {container}:{destination}",
        "requires_slots": ["source", "container", "destination"],
        "confirm": True
    },

    "docker.container.cp.from": {
        "template": "docker cp {container}:{source} {destination}",
        "requires_slots": ["container", "source", "destination"],
        "confirm": True
    },


    # ============================================================
    # IMAGES
    # ============================================================

    "docker.image.list": {
        "template": "docker images",
        "requires_slots": []
    },

    "docker.image.list.all": {
        "template": "docker images -a",
        "requires_slots": []
    },

    "docker.image.pull": {
        "template": "docker pull {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.image.push": {
        "template": "docker push {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.image.remove": {
        "template": "docker rmi {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.image.remove.force": {
        "template": "docker rmi -f {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.image.inspect": {
        "template": "docker image inspect {image}",
        "requires_slots": ["image"]
    },

    "docker.image.history": {
        "template": "docker history {image}",
        "requires_slots": ["image"]
    },

    "docker.image.tag": {
        "template": "docker tag {source} {target}",
        "requires_slots": ["source_image", "target_image"],
        "confirm": True
    },

    "docker.image.save": {
        "template": "docker save -o {file} {image}",
        "requires_slots": ["file_name", "image"],
        "confirm": True
    },

    "docker.image.load": {
        "template": "docker load -i {file}",
        "requires_slots": ["file_path"],
        "confirm": True
    },

    "docker.image.prune": {
        "template": "docker image prune",
        "requires_slots": [],
        "confirm": True
    },

    "docker.image.prune.all": {
        "template": "docker image prune -a",
        "requires_slots": [],
        "confirm": True
    },


    # ============================================================
    # BUILD
    # ============================================================

    "docker.build": {
        "template": "docker build {path}",
        "requires_slots": ["path"],
        "confirm": True
    },

    "docker.build.tagged": {
        "template": "docker build -t {image} {path}",
        "requires_slots": ["image_name", "path"],
        "confirm": True
    },

    "docker.build.no_cache": {
        "template": "docker build --no-cache -t {image} {path}",
        "requires_slots": ["image_name", "path"],
        "confirm": True
    },

    "docker.build.pull": {
        "template": "docker build --pull -t {image} {path}",
        "requires_slots": ["image_name", "path"],
        "confirm": True
    },


    # ============================================================
    # NETWORKS
    # ============================================================

    "docker.network.list": {
        "template": "docker network ls",
        "requires_slots": []
    },

    "docker.network.create": {
        "template": "docker network create {network}",
        "requires_slots": ["network_name"],
        "confirm": True
    },

    "docker.network.remove": {
        "template": "docker network rm {network}",
        "requires_slots": ["network"],
        "confirm": True
    },

    "docker.network.inspect": {
        "template": "docker network inspect {network}",
        "requires_slots": ["network"]
    },

    "docker.network.connect": {
        "template": "docker network connect {network} {container}",
        "requires_slots": ["network", "container"],
        "confirm": True
    },

    "docker.network.disconnect": {
        "template": "docker network disconnect {network} {container}",
        "requires_slots": ["network", "container"],
        "confirm": True
    },

    "docker.network.disconnect.force": {
        "template": "docker network disconnect -f {network} {container}",
        "requires_slots": ["network", "container"],
        "confirm": True
    },

    "docker.network.prune": {
        "template": "docker network prune",
        "requires_slots": [],
        "confirm": True
    },


    # ============================================================
    # VOLUMES
    # ============================================================

    "docker.volume.list": {
        "template": "docker volume ls",
        "requires_slots": []
    },

    "docker.volume.create": {
        "template": "docker volume create {volume}",
        "requires_slots": ["volume"],
        "confirm": True
    },

    "docker.volume.inspect": {
        "template": "docker volume inspect {volume}",
        "requires_slots": ["volume"]
    },

    "docker.volume.remove": {
        "template": "docker volume rm {volume}",
        "requires_slots": ["volume"],
        "confirm": True
    },

    "docker.volume.prune": {
        "template": "docker volume prune",
        "requires_slots": [],
        "confirm": True
    },


    # ============================================================
    # DOCKER COMPOSE
    # ============================================================

    "docker.compose.up": {
        "template": "docker compose up",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.up.detached": {
        "template": "docker compose up -d",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.down": {
        "template": "docker compose down",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.down.volumes": {
        "template": "docker compose down -v",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.start": {
        "template": "docker compose start",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.stop": {
        "template": "docker compose stop",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.restart": {
        "template": "docker compose restart",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.ps": {
        "template": "docker compose ps",
        "requires_slots": []
    },

    "docker.compose.logs": {
        "template": "docker compose logs",
        "requires_slots": []
    },

    "docker.compose.logs.follow": {
        "template": "docker compose logs -f",
        "requires_slots": []
    },

    "docker.compose.pull": {
        "template": "docker compose pull",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.build": {
        "template": "docker compose build",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.build.no_cache": {
        "template": "docker compose build --no-cache",
        "requires_slots": [],
        "confirm": True
    },

    "docker.compose.exec": {
        "template": "docker compose exec {service} {command}",
        "requires_slots": ["service", "command"],
        "confirm": True
    },

    "docker.compose.run": {
        "template": "docker compose run {service} {command}",
        "requires_slots": ["service", "command"],
        "confirm": True
    },


    # ============================================================
    # SYSTEM / INFORMATION
    # ============================================================

    "docker.version": {
        "template": "docker version",
        "requires_slots": []
    },

    "docker.info": {
        "template": "docker info",
        "requires_slots": []
    },

    "docker.disk.usage": {
        "template": "docker system df",
        "requires_slots": []
    },

    "docker.disk.usage.verbose": {
        "template": "docker system df -v",
        "requires_slots": []
    },


    # ============================================================
    # CLEANUP
    # ============================================================

    "docker.system.prune": {
        "template": "docker system prune",
        "requires_slots": [],
        "confirm": True
    },

    "docker.system.prune.all": {
        "template": "docker system prune -a",
        "requires_slots": [],
        "confirm": True
    },

    "docker.system.prune.volumes": {
        "template": "docker system prune --volumes",
        "requires_slots": [],
        "confirm": True
    },

    "docker.container.prune": {
        "template": "docker container prune",
        "requires_slots": [],
        "confirm": True
    },


    # ============================================================
    # LOGIN / REGISTRY
    # ============================================================

    "docker.login": {
        "template": "docker login",
        "requires_slots": [],
        "confirm": True
    },

    "docker.login.registry": {
        "template": "docker login {registry}",
        "requires_slots": ["registry"],
        "confirm": True
    },

    "docker.logout": {
        "template": "docker logout",
        "requires_slots": [],
        "confirm": True
    },

    "docker.logout.registry": {
        "template": "docker logout {registry}",
        "requires_slots": ["registry"],
        "confirm": True
    },


    # ============================================================
    # TAG / CONTAINER COMMIT
    # ============================================================

    "docker.container.commit": {
        "template": "docker commit {container} {image}",
        "requires_slots": ["container", "image"],
        "confirm": True
    },


    # ============================================================
    # EXPORT / IMPORT
    # ============================================================

    "docker.container.export": {
        "template": "docker export -o {file} {container}",
        "requires_slots": ["file", "container"],
        "confirm": True
    },

    "docker.container.import": {
        "template": "docker import {file} {image}",
        "requires_slots": ["file", "image"],
        "confirm": True
    },

    #============================================================
    #                   Linux Commands                                  
    #============================================================


    # ============================================================
    # FILESYSTEM / NAVIGATION
    # ============================================================

    "linux.pwd": {
        "template": "pwd",
        "requires_slots": []
    },

    "linux.ls": {
        "template": "ls",
        "requires_slots": []
    },

    "linux.ls.hidden": {
        "template": "ls -la",
        "requires_slots": []
    },

    "linux.cd": {
        "template": "cd {path}",
        "requires_slots": ["path"]
    },

    "linux.cd.parent": {
        "template": "cd ..",
        "requires_slots": []
    },

    "linux.cd.home": {
        "template": "cd ~",
        "requires_slots": []
    },

    "linux.mkdir": {
        "template": "mkdir {directory}",
        "requires_slots": ["directory_name"]
    },

    "linux.mkdir.parents": {
        "template": "mkdir -p {directory}",
        "requires_slots": ["directory_name"]
    },

    "linux.touch": {
        "template": "touch {file}",
        "requires_slots": ["file_name"]
    },

    "linux.cp": {
        "template": "cp {source} {destination}",
        "requires_slots": ["source", "destination"],
        "confirm": True
    },

    "linux.mv": {
        "template": "mv {source} {destination}",
        "requires_slots": ["source", "destination"],
        "confirm": True
    },

    "linux.rename": {
        "template": "mv {old_name} {new_name}",
        "requires_slots": ["old_name", "new_name"],
        "confirm": True
    },

    "linux.rm": {
        "template": "rm {file}",
        "requires_slots": ["file"],
        "confirm": True
    },

    "linux.rm.directory": {
        "template": "rmdir {directory}",
        "requires_slots": ["directory"],
        "confirm": True
    },

    "linux.rm.recursive": {
        "template": "rm -rf {directory}",
        "requires_slots": ["directory"],
        "confirm": True
    },

    "linux.find": {
        "template": "find {path} -name '{name}'",
        "requires_slots": ["path", "name"]
    },

    "linux.locate": {
        "template": "locate {name}",
        "requires_slots": ["name"]
    },

    "linux.file.type": {
        "template": "file {path}",
        "requires_slots": ["path"]
    },

    "linux.stat": {
        "template": "stat {path}",
        "requires_slots": ["path"]
    },


    # ============================================================
    # FILE CONTENT
    # ============================================================

    "linux.cat": {
        "template": "cat {file}",
        "requires_slots": ["file"]
    },

    "linux.less": {
        "template": "less {file}",
        "requires_slots": ["file"]
    },

    "linux.head": {
        "template": "head {file}",
        "requires_slots": ["file"]
    },

    "linux.tail": {
        "template": "tail {file}",
        "requires_slots": ["file"]
    },

    "linux.tail.follow": {
        "template": "tail -f {file}",
        "requires_slots": ["file"]
    },

    "linux.grep": {
        "template": "grep '{pattern}' {file}",
        "requires_slots": ["pattern", "file"]
    },

    "linux.grep.recursive": {
        "template": "grep -R '{pattern}' {path}",
        "requires_slots": ["pattern", "path"]
    },

    "linux.wc": {
        "template": "wc {file}",
        "requires_slots": ["file"]
    },

    "linux.sort": {
        "template": "sort {file}",
        "requires_slots": ["file"]
    },

    "linux.uniq": {
        "template": "uniq {file}",
        "requires_slots": ["file"]
    },

    "linux.cut": {
        "template": "cut {options} {file}",
        "requires_slots": ["options", "file"]
    },

    "linux.awk": {
        "template": "awk '{expression}' {file}",
        "requires_slots": ["expression", "file"]
    },

    "linux.sed": {
        "template": "sed '{expression}' {file}",
        "requires_slots": ["expression", "file"]
    },


    # ============================================================
    # PERMISSIONS
    # ============================================================

    "linux.chmod": {
        "template": "chmod {permissions} {path}",
        "requires_slots": ["permissions", "path"],
        "confirm": True
    },

    "linux.chmod.readwrite": {
        "template": "chmod {permissions} {path}",
        "requires_slots": ["permissions", "path"],
        "confirm": True
    },

    "linux.chmod.execute": {
        "template": "chmod +x {path}",
        "requires_slots": ["path"],
        "confirm": True
    },

    "linux.chown": {
        "template": "chown {owner} {path}",
        "requires_slots": ["owner", "path"],
        "confirm": True
    },

    "linux.chgrp": {
        "template": "chgrp {group} {path}",
        "requires_slots": ["group", "path"],
        "confirm": True
    },

    "linux.umask": {
        "template": "umask",
        "requires_slots": []
    },


    # ============================================================
    # DISK / STORAGE
    # ============================================================

    "linux.df": {
        "template": "df",
        "requires_slots": []
    },

    "linux.df.human": {
        "template": "df -h",
        "requires_slots": []
    },

    "linux.du": {
        "template": "du -sh {path}",
        "requires_slots": ["path"]
    },

    "linux.du.large": {
        "template": "du -ah {path} | sort -rh | head -20",
        "requires_slots": ["path"]
    },

    "linux.lsblk": {
        "template": "lsblk",
        "requires_slots": []
    },

    "linux.mount": {
        "template": "mount {device} {mount_point}",
        "requires_slots": ["device", "mount_point"],
        "confirm": True
    },

    "linux.umount": {
        "template": "umount {mount_point}",
        "requires_slots": ["mount_point"],
        "confirm": True
    },

    "linux.fdisk": {
        "template": "sudo fdisk -l",
        "requires_slots": [],
        "confirm": False
    },

    "linux.free": {
        "template": "free -h",
        "requires_slots": []
    },

    "linux.free.swap": {
        "template": "free -h",
        "requires_slots": []
    },


    # ============================================================
    # PROCESSES
    # ============================================================

    "linux.ps": {
        "template": "ps",
        "requires_slots": []
    },

    "linux.ps.all": {
        "template": "ps aux",
        "requires_slots": []
    },

    "linux.top": {
        "template": "top",
        "requires_slots": []
    },

    "linux.htop": {
        "template": "htop",
        "requires_slots": []
    },

    "linux.kill": {
        "template": "kill {pid}",
        "requires_slots": ["pid"],
        "confirm": True
    },

    "linux.kill.force": {
        "template": "kill -9 {pid}",
        "requires_slots": ["pid"],
        "confirm": True
    },

    "linux.pgrep": {
        "template": "pgrep -a {process_name}",
        "requires_slots": ["process_name"]
    },

    "linux.pkill": {
        "template": "pkill {process_name}",
        "requires_slots": ["process_name"],
        "confirm": True
    },

    "linux.jobs": {
        "template": "jobs",
        "requires_slots": []
    },

    "linux.bg": {
        "template": "bg {job_id}",
        "requires_slots": ["job_id"]
    },

    "linux.fg": {
        "template": "fg {job_id}",
        "requires_slots": ["job_id"]
    },


    # ============================================================
    # SYSTEM INFORMATION
    # ============================================================

    "linux.uname": {
        "template": "uname -a",
        "requires_slots": []
    },

    "linux.hostname": {
        "template": "hostname",
        "requires_slots": []
    },

    "linux.uptime": {
        "template": "uptime",
        "requires_slots": []
    },

    "linux.date": {
        "template": "date",
        "requires_slots": []
    },

    "linux.time": {
        "template": "date '+%H:%M:%S'",
        "requires_slots": []
    },

    "linux.whoami": {
        "template": "whoami",
        "requires_slots": []
    },

    "linux.who": {
        "template": "who",
        "requires_slots": []
    },

    "linux.id": {
        "template": "id",
        "requires_slots": []
    },

    "linux.lscpu": {
        "template": "lscpu",
        "requires_slots": []
    },

    "linux.lsmem": {
        "template": "lsmem",
        "requires_slots": []
    },


    # ============================================================
    # APT
    # ============================================================

    "ubuntu.apt.update": {
        "template": "sudo apt update",
        "requires_slots": [],
        "confirm": True
    },

    "ubuntu.apt.upgrade": {
        "template": "sudo apt upgrade",
        "requires_slots": [],
        "confirm": True
    },

    "ubuntu.apt.install": {
        "template": "sudo apt install {package}",
        "requires_slots": ["package"],
        "confirm": True
    },

    "ubuntu.apt.remove": {
        "template": "sudo apt remove {package}",
        "requires_slots": ["package"],
        "confirm": True
    },

    "ubuntu.apt.purge": {
        "template": "sudo apt purge {package}",
        "requires_slots": ["package"],
        "confirm": True
    },

    "ubuntu.apt.search": {
        "template": "apt search {package}",
        "requires_slots": ["package"]
    },

    "ubuntu.apt.show": {
        "template": "apt show {package}",
        "requires_slots": ["package"]
    },

    "ubuntu.apt.list.installed": {
        "template": "apt list --installed",
        "requires_slots": []
    },

    "ubuntu.apt.autoremove": {
        "template": "sudo apt autoremove",
        "requires_slots": [],
        "confirm": True
    },

    "ubuntu.apt.autoclean": {
        "template": "sudo apt autoclean",
        "requires_slots": [],
        "confirm": True
    },


    # ============================================================
    # SNAP
    # ============================================================

    "ubuntu.snap.install": {
        "template": "sudo snap install {package}",
        "requires_slots": ["package"],
        "confirm": True
    },

    "ubuntu.snap.remove": {
        "template": "sudo snap remove {package}",
        "requires_slots": ["package"],
        "confirm": True
    },

    "ubuntu.snap.list": {
        "template": "snap list",
        "requires_slots": []
    },


    # ============================================================
    # SYSTEMD
    # ============================================================

    "linux.systemctl.status": {
        "template": "systemctl status {service}",
        "requires_slots": ["service"]
    },

    "linux.systemctl.start": {
        "template": "sudo systemctl start {service}",
        "requires_slots": ["service"],
        "confirm": True
    },

    "linux.systemctl.stop": {
        "template": "sudo systemctl stop {service}",
        "requires_slots": ["service"],
        "confirm": True
    },

    "linux.systemctl.restart": {
        "template": "sudo systemctl restart {service}",
        "requires_slots": ["service"],
        "confirm": True
    },

    "linux.systemctl.reload": {
        "template": "sudo systemctl reload {service}",
        "requires_slots": ["service"],
        "confirm": True
    },

    "linux.systemctl.enable": {
        "template": "sudo systemctl enable {service}",
        "requires_slots": ["service"],
        "confirm": True
    },

    "linux.systemctl.disable": {
        "template": "sudo systemctl disable {service}",
        "requires_slots": ["service"],
        "confirm": True
    },

    "linux.systemctl.list": {
        "template": "systemctl list-units --type=service",
        "requires_slots": []
    },

    "linux.journalctl": {
        "template": "journalctl",
        "requires_slots": []
    },

    "linux.journalctl.follow": {
        "template": "journalctl -f",
        "requires_slots": []
    },


    # ============================================================
    # NETWORKING
    # ============================================================

    "linux.ip.address": {
        "template": "ip addr",
        "requires_slots": []
    },

    "linux.ip.interface": {
        "template": "ip link",
        "requires_slots": []
    },

    "linux.ip.route": {
        "template": "ip route",
        "requires_slots": []
    },

    "linux.ip.neighbor": {
        "template": "ip neigh",
        "requires_slots": []
    },

    "linux.ping": {
        "template": "ping -c 4 {host}",
        "requires_slots": ["host"]
    },

    "linux.traceroute": {
        "template": "traceroute {host}",
        "requires_slots": ["host"]
    },

    "linux.dig": {
        "template": "dig {domain}",
        "requires_slots": ["domain"]
    },

    "linux.nslookup": {
        "template": "nslookup {domain}",
        "requires_slots": ["domain"]
    },

    "linux.curl": {
        "template": "curl {url}",
        "requires_slots": ["url"]
    },

    "linux.wget": {
        "template": "wget {url}",
        "requires_slots": ["url"],
        "confirm": True
    },

    "linux.ss": {
        "template": "ss -tulpn",
        "requires_slots": []
    },

    "linux.netstat": {
        "template": "netstat -tulpn",
        "requires_slots": []
    },

    "linux.hostname.resolve": {
        "template": "getent hosts {hostname}",
        "requires_slots": ["hostname"]
    },


    # ============================================================
    # SSH
    # ============================================================

    "linux.ssh.connect": {
        "template": "ssh {user}@{host}",
        "requires_slots": ["user", "host"]
    },

    "linux.ssh.keygen": {
        "template": "ssh-keygen -t ed25519",
        "requires_slots": []
    },

    "linux.ssh.copy_id": {
        "template": "ssh-copy-id {user}@{host}",
        "requires_slots": ["user", "host"],
        "confirm": True
    },

    "linux.scp.upload": {
        "template": "scp {source} {user}@{host}:{destination}",
        "requires_slots": ["source", "user", "host", "destination"],
        "confirm": True
    },

    "linux.scp.download": {
        "template": "scp {user}@{host}:{source} {destination}",
        "requires_slots": ["user", "host", "source", "destination"],
        "confirm": True
    },


    # ============================================================
    # USERS
    # ============================================================

    "linux.user.list": {
        "template": "cut -d: -f1 /etc/passwd",
        "requires_slots": []
    },

    "linux.user.add": {
        "template": "sudo useradd {username}",
        "requires_slots": ["username"],
        "confirm": True
    },

    "linux.user.delete": {
        "template": "sudo userdel {username}",
        "requires_slots": ["username"],
        "confirm": True
    },

    "linux.user.modify": {
        "template": "sudo usermod {options} {username}",
        "requires_slots": ["options", "username"],
        "confirm": True
    },

    "linux.user.password": {
        "template": "sudo passwd {username}",
        "requires_slots": ["username"],
        "confirm": True
    },

    # ============================================================
    # GROUPS
    # ============================================================

    "linux.group.list": {
        "template": "getent group",
        "requires_slots": []
    },

    "linux.group.add": {
        "template": "sudo groupadd {group}",
        "requires_slots": ["group"],
        "confirm": True
    },

    "linux.group.delete": {
        "template": "sudo groupdel {group}",
        "requires_slots": ["group"],
        "confirm": True
    },

    "linux.group.add_user": {
        "template": "sudo usermod -aG {group} {username}",
        "requires_slots": ["group", "username"],
        "confirm": True
    },


    # ============================================================
    # ARCHIVES
    # ============================================================

    "linux.tar.create": {
        "template": "tar -cvf {archive}.tar {source}",
        "requires_slots": ["archive", "source"],
        "confirm": True
    },

    "linux.tar.extract": {
        "template": "tar -xvf {archive}",
        "requires_slots": ["archive"],
        "confirm": True
    },

    "linux.tar.list": {
        "template": "tar -tvf {archive}",
        "requires_slots": ["archive"]
    },

    "linux.gzip": {
        "template": "gzip {file}",
        "requires_slots": ["file"],
        "confirm": True
    },

    "linux.gunzip": {
        "template": "gunzip {file}",
        "requires_slots": ["file"],
        "confirm": True
    },

    "linux.zip": {
        "template": "zip -r {archive}.zip {source}",
        "requires_slots": ["archive", "source"],
        "confirm": True
    },

    "linux.unzip": {
        "template": "unzip {archive}",
        "requires_slots": ["archive"]
    },


    # ============================================================
    # SHELL UTILITIES
    # ============================================================

    "linux.echo": {
        "template": "echo '{text}'",
        "requires_slots": ["text"]
    },

    "linux.env": {
        "template": "env",
        "requires_slots": []
    },

    "linux.export": {
        "template": "export {name}='{value}'",
        "requires_slots": ["name", "value"]
    },

    "linux.alias": {
        "template": "alias {name}='{command}'",
        "requires_slots": ["name", "command"]
    },

    "linux.history": {
        "template": "history",
        "requires_slots": []
    },

    "linux.clear": {
        "template": "clear",
        "requires_slots": []
    },

    "linux.which": {
        "template": "which {command}",
        "requires_slots": ["command"]
    },

    "linux.whereis": {
        "template": "whereis {command}",
        "requires_slots": ["command"]
    },

    "linux.man": {
        "template": "man {command}",
        "requires_slots": ["command"]
    },

    "linux.help": {
        "template": "{command} --help",
        "requires_slots": ["command"]
    },


    # ============================================================
    # PROCESS PRIORITY
    # ============================================================

    "linux.nice": {
        "template": "nice -n {priority} {command}",
        "requires_slots": ["priority", "command"]
    },

    "linux.renice": {
        "template": "renice {priority} -p {pid}",
        "requires_slots": ["priority", "pid"],
        "confirm": True
    },


    # ============================================================
    # CRON
    # ============================================================

    "linux.cron.list": {
        "template": "crontab -l",
        "requires_slots": []
    },

    "linux.cron.edit": {
        "template": "crontab -e",
        "requires_slots": [],
        "confirm": True
    },

    "linux.cron.remove": {
        "template": "crontab -r",
        "requires_slots": [],
        "confirm": True
    },


    # ============================================================
    # LOGGING
    # ============================================================

    "linux.logs.system": {
        "template": "journalctl",
        "requires_slots": []
    },

    "linux.logs.kernel": {
        "template": "dmesg",
        "requires_slots": []
    },

    "linux.logs.service": {
        "template": "journalctl -u {service}",
        "requires_slots": ["service"]
    },


    # ============================================================
    # UFW FIREWALL
    # ============================================================

    "ubuntu.ufw.status": {
        "template": "sudo ufw status",
        "requires_slots": []
    },

    "ubuntu.ufw.enable": {
        "template": "sudo ufw enable",
        "requires_slots": [],
        "confirm": True
    },

    "ubuntu.ufw.disable": {
        "template": "sudo ufw disable",
        "requires_slots": [],
        "confirm": True
    },

    "ubuntu.ufw.allow": {
        "template": "sudo ufw allow {port}",
        "requires_slots": ["port"],
        "confirm": True
    },

    "ubuntu.ufw.deny": {
        "template": "sudo ufw deny {port}",
        "requires_slots": ["port"],
        "confirm": True
    },

    "ubuntu.ufw.delete_rule": {
        "template": "sudo ufw delete allow {port}",
        "requires_slots": ["port"],
        "confirm": True
    },

    "linux.sudo": {
        "template": "sudo {command}",
        "requires_slots": ["command"],
        "confirm": True
    },


    # ============================================================
    # COMMAND DISCOVERY
    # ============================================================

    "linux.command.version": {
        "template": "{command} --version",
        "requires_slots": ["command"]
    },

    "linux.command.exists": {
        "template": "command -v {command}",
        "requires_slots": ["command"]
    },


    # ============================================================
    # SYSTEM CONTROL
    # ============================================================

    "linux.shutdown": {
        "template": "sudo shutdown now",
        "requires_slots": [],
        "confirm": True
    },

    "linux.reboot": {
        "template": "sudo reboot",
        "requires_slots": [],
        "confirm": True
    },

    "linux.logout": {
        "template": "logout",
        "requires_slots": []
    },


    # ============================================================
    # TERMINAL / SHELL
    # ============================================================

    "linux.exit": {
        "template": "exit",
        "requires_slots": []
    },

    "linux.source": {
        "template": "source {file}",
        "requires_slots": ["file"]
    },

    "linux.bash": {
        "template": "bash",
        "requires_slots": []
    },

    "linux.ssh.exit": {
        "template": "exit",
        "requires_slots": []
    },


    # ============================================================
    # DOCKER
    # ============================================================

    "docker.ps": {
        "template": "docker ps",
        "requires_slots": []
    },

    "docker.ps.all": {
        "template": "docker ps -a",
        "requires_slots": []
    },

    "docker.images": {
        "template": "docker images",
        "requires_slots": []
    },

    "docker.pull": {
        "template": "docker pull {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.run": {
        "template": "docker run {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.stop": {
        "template": "docker stop {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.start": {
        "template": "docker start {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.restart": {
        "template": "docker restart {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.rm": {
        "template": "docker rm {container}",
        "requires_slots": ["container"],
        "confirm": True
    },

    "docker.rmi": {
        "template": "docker rmi {image}",
        "requires_slots": ["image"],
        "confirm": True
    },

    "docker.logs": {
        "template": "docker logs {container}",
        "requires_slots": ["container"]
    },

    "docker.exec": {
        "template": "docker exec -it {container} {command}",
        "requires_slots": ["container", "command"],
        "confirm": True
    },

    "linux.networkmanager.status": {
        "template": "systemctl status NetworkManager",
        "requires_slots": []
    },

    "linux.networkmanager.restart": {
        "template": "sudo systemctl restart NetworkManager",
        "requires_slots": [],
        "confirm": True
    },

    "linux.dns.status": {
        "template": "resolvectl status",
        "requires_slots": []
    },

    "linux.ln": {
        "template": "ln -s {target} {link}",
        "requires_slots": ["target", "link"],
        "confirm": True
    },

    "linux.ln.hard": {
        "template": "ln {target} {link}",
        "requires_slots": ["target", "link"],
        "confirm": True
    },

    "linux.mount.list": {
        "template": "mount",
        "requires_slots": []
    },

    "linux.fsck": {
        "template": "sudo fsck {device}",
        "requires_slots": ["device"],
        "confirm": True
    },

    "ubuntu.dpkg.list": {
        "template": "dpkg -l",
        "requires_slots": []
    },

    "ubuntu.dpkg.install": {
        "template": "sudo dpkg -i {package}",
        "requires_slots": ["package"],
        "confirm": True
    },

    "ubuntu.dpkg.remove": {
        "template": "sudo dpkg -r {package}",
        "requires_slots": ["package"],
        "confirm": True
    },

    "windows.touch": {
        "template": "type nul > {filename}",
        "requires_slots": ["filename"]
    },

    "windows.cd.desktop": {
        "template": "cd /d %USERPROFILE%\\Desktop",
        "requires_slots": []
    },

    "windows.cd.documents": {
        "template": "cd /d %USERPROFILE%\\Documents",
        "requires_slots": []
    },

    "windows.cd.downloads": {
        "template": "cd /d %USERPROFILE%\\Downloads",
        "requires_slots": []
    },

    "windows.cd.home": {
        "template": "cd /d %USERPROFILE%",
        "requires_slots": []
    },

    "windows.cd.parent": {
        "template": "cd ..",
        "requires_slots": []
    },

    "windows.pwd": {
        "template": "cd",
        "requires_slots": []
    },

    "windows.dir": {
        "template": "dir",
        "requires_slots": []
    },

    "windows.dir.hidden": {
        "template": "dir /a",
        "requires_slots": []
    },

    "windows.mkdir": {
        "template": "mkdir {dirname}",
        "requires_slots": ["dirname"]
    },

    "windows.delete.file": {
        "template": "del {filename}",
        "requires_slots": ["filename"],
        "confirm": True
    },

    "windows.delete.folder": {
        "template": "rmdir /s /q {dirname}",
        "requires_slots": ["dirname"],
        "confirm": True
    },

    "windows.copy": {
        "template": "copy {source} {destination}",
        "requires_slots": ["source", "destination"]
    },

    "windows.move": {
        "template": "move {source} {destination}",
        "requires_slots": ["source", "destination"]
    },

    "windows.rename": {
        "template": "ren {oldname} {newname}",
        "requires_slots": ["oldname", "newname"]
    },

    "windows.clear": {
        "template": "cls",
        "requires_slots": []
    },

    "windows.echo": {
        "template": "echo {text}",
        "requires_slots": ["text"]
    },

    "windows.type": {
        "template": "type {filename}",
        "requires_slots": ["filename"]
    }

}