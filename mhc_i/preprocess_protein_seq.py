import sys
from os.path import basename

def preprocess_protein_seq(args):
    with open(args[1], "r") as f_in:
        f_out_name = basename(args[1])
        with open(f"externaldata/{f_out_name}_processed.fasta", "w") as f_out:
            i = 0
            for line in f_in.read().split():
                f_out.write(f">seq{i}\n{line}\n")
                i += 1
    return


if __name__ == "__main__":
    preprocess_protein_seq(sys.argv)