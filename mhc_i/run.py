import requests
import argparse
import pandas as pd

def run():
    parser = argparse.ArgumentParser()
    # parser.add_argument("epitope") #fasta file containing sequence
    parser.add_argument("-alleles", default="alleles.csv", metavar="<alleles.csv>", required=False)
    parser.add_argument("-output", default="out.csv", metavar="<out.csv>", required=False)
    args = vars(parser.parse_args())
    alleles_f = pd.read_csv(args["alleles"], converters={"length":str})
    a = ",".join(alleles_f["allele"])
    lens = ",".join(alleles_f["length"])
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    seqs = "%3Epeptide1%0AGHAHKVPRRLLKAAR"
    data = f"method=netmhcpan_el&sequence_text={seqs}&allele={a}&length={lens}"

    response = requests.post('http://tools-cluster-interface.iedb.org/tools_api/mhci/', headers=headers, data=data)
    if not response.ok:
        print(response.reason)
        response.raise_for_status()
    with open(args["output"], "w") as f_out:
        for line in response.iter_lines(decode_unicode=True):
            str_line = line.replace("\t", ",")
            f_out.write(str_line+"\n")

if __name__ == "__main__":
    run()