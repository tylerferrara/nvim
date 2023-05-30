import subprocess
import os

USE_PKG_MANAGER="USE PACKAGE MANAGER"
deps = [
        ("make", USE_PKG_MANAGER),
        ("cmake", USE_PKG_MANAGER),
        ("ninja-build", USE_PKG_MANAGER),
        ("gettext", USE_PKG_MANAGER),
        ("unzip", USE_PKG_MANAGER),
        ("git", USE_PKG_MANAGER),
        ("curl", USE_PKG_MANAGER),
        ("cargo", "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y"),
        ("tree-sitter", "cargo install tree-sitter-cli"),
        ("rp", USE_PKG_MANAGER, "ripgrep"),
        ("nodejs", USE_PKG_MANAGER),
        ("npm", USE_PKG_MANAGER),
]

def compile_nvim():
    os.system("sudo git clone https://github.com/neovim/neovim.git /opt/neovim")
    os.system("cd /opt/neovim && sudo make CMAKE_BUILD_TYPE=RelWithDebInfo CMAKE_INSTALL_PREFIX=/usr/bin")
    os.system("sudo ln /opt/neovim/build/bin/nvim /usr/bin")

def install(pkg):
    if subprocess.call(["which", "apt"]) == 0:
        os.system(f"sudo apt install {pkg} -y")
    else:
        print("FAILED: Unsupported package manager :(")

def use_astro():
    os.system("git clone --depth 1 https://github.com/AstroNvim/AstroNvim ~/.config/nvim")

def main():
    print("Install script for NeoVim config")
    for dep in deps:
        pkg = dep[0]
        req = dep[1]
        print(f"Looking for \"{pkg}\"")
        if subprocess.call(["which", pkg]) == 0:
            print(f"FOUND \"{pkg}\"")
            continue
        if req is USE_PKG_MANAGER:
            if len(dep) > 2:
                pkg = dep[2]
            install(pkg)
            continue
        os.system(req)

    compile_nvim()
    use_astro()


main()
