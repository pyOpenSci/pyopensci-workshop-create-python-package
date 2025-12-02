# Dev Container Configuration

This directory contains the configuration for GitHub Codespaces and VS Code Dev Containers.

## Shorter Terminal Prompt

The `postStartCommand` in `devcontainer.json` configures a shorter bash prompt (`\W\$ `) that shows only the current directory name instead of the full path. This makes the terminal easier to read, especially in workshop settings.

The command is idempotent—it only adds the `PS1` export line to `~/.bashrc` if it's not already present, so restarting the Codespace won't create duplicate lines.

### How to Override

If you prefer a different prompt, you can:

1. **Edit `~/.bashrc` directly**: Modify or remove the `export PS1='\W\$ '` line and add your preferred prompt setting.

2. **Use a custom dotfiles repo**: Configure your [GitHub Codespaces dotfiles](https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-github-codespaces-for-your-account#dotfiles) to set your preferred `PS1` value. Your dotfiles will take precedence.

### How to Revert

To remove this feature from the repository, delete the `postStartCommand` line from `devcontainer.json`.
