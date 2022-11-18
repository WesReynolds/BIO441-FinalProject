import requests
import argparse
import pandas as pd
from Bio import SeqIO
import logging

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("epitope", help="fasta file containing epitopes")
    parser.add_argument("-alleles", default="ref_alleles.csv", metavar="<ref_alleles.csv>", required=False)
    parser.add_argument("-output", default="out.csv", metavar="<out.csv>", required=False)
    return vars(parser.parse_args())

def prepare_request(args):
    epitopes = list(SeqIO.parse(args["epitope"], "fasta"))
    seqs = "".join(f"%3E{epi.id}%0A{epi.seq}" for epi in epitopes)
    alleles_f = pd.read_csv(args["alleles"], converters={"length":str})
    a = ",".join(alleles_f["allele"])
    lens = ",".join(alleles_f["length"])
    logging.debug(f"seq: {seqs}\na: {a}\nlens: {lens}\n\n")

    data = f"method=netmhcpan_el&sequence_text={seqs}&allele={a}&length={lens}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    return headers, data

def run():
    logging.basicConfig(filename='mch_i.log', encoding='utf-8', level=logging.WARNING, 
        format='%(levelname)s: %(asctime)s %(message)s:', datefmt='%m/%d/%Y %H:%M:%S')
    args = parse_arguments()
    headers, data = prepare_request(args)

    response = requests.post('http://tools-cluster-interface.iedb.org/tools_api/mhci/', headers=headers, data=data)
    logging.debug(f"response: {response}")
    if not response.ok:
        logging.error(f"{response.status_code}: {response.reason}\n")
        response.raise_for_status()
    with open(args["output"], "w") as f_out:
        for line in response.iter_lines(decode_unicode=True):
            str_line = line.replace("\t", ",")
            f_out.write(str_line+"\n")

if __name__ == "__main__":
    run()