# -*- coding: utf-8 -*_
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This script reads information of a group from
a .yaml file and computes its coset table.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Example usage:

    python coset_enum_example.py filename [-std]

    filename: required, the .yaml file to be parsed.
       - std: optional, needs no value, if added then
              the output table is standardized.
"""
import argparse
import yaml
from fpgroup import FpGroup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="Input file name")
    parser.add_argument("-std", type=bool, default=True, help="Standardize the coset table or not")
    parser.add_argument("-out", metavar="-o", type=str, default=None, help="output file name")
    args = parser.parse_args()
    with open(args.filename, "r") as f:
        data = yaml.load(f)
        rels = data["relators"]
        subg = data["subgroup-generators"]
        name = data["name"]
        G = FpGroup(rels, subg, name)
        G.compute(args.std)
        G.print_table(args.out)


if __name__ == "__main__":
    main()