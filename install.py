import subprocess
import os

USE_PKG_MANAGER="USE PACKAGE MANAGER"
deps = [
        ("git", USE_PKG_MANAGER),
        ("curl", USE_PKG_MANAGER),
        ("nvim", USE_PKG_MANAGER),
        ("cargo", "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y"),
        ("tree-sitter", "cargo install tree-sitter-cli"),
        ("ripgrep", USE_PKG_MANAGER),
        ("nodejs", USE_PKG_MANAGER),
        ("npm", USE_PKG_MANAGER),
]

def install(pkg):
    if subprocess.call(["which", "apt"]) == 0:
        os.system(f"sudo apt install {pkg} -y")
    else:
        print("FAILED: Unsupported package manager :(")

def astro():
    os.system("git clone --depth 1 https://github.com/AstroNvim/AstroNvim ~/.config/nvim/*")

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
            install(pkg)
            continue
        os.system(req)

main()
