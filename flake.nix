{
  description = "A game of solitaire written in Python with Pygame using Nix";

  inputs = {
    # nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    pyproject-nix = {
      url = "github:nix-community/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, pyproject-nix, ... }: let 
    inherit (nixpkgs) lib;
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    pyproject = pyproject-nix.lib.project.loadPyproject {
      projectRoot = ./.;
    };
    python = pkgs.python3;
  in {
    # nix build
    packages.${system}.default = let
      attrs = pyproject.renderers.buildPythonPackage { inherit python; };
    in python.pkgs.buildPythonApplication attrs;

    # nix run
    apps.${system}.default = {
      type = "app";
      program = "${self.packages.${system}.default}/bin/freecell";
    };

    # nix develop
    devShells.${system}.default = let
      devDependencies = pyproject.renderers.withPackages {
        inherit python;
        extras = builtins.attrNames 
                    pyproject.pyproject.project.optional-dependencies;
      };
    pythonEnv = python.withPackages devDependencies;
    in pkgs.mkShell {
      buildInputs = [ pythonEnv ];
    };
  };
}
