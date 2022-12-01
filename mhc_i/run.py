import requests
import argparse
import pandas as pd
from Bio import SeqIO
import logging

OUTPUT_DIR = "../ProgramData/BindingData/"

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("epitope", help="fasta file containing epitopes")
    parser.add_argument("-alleles", default="ref_alleles.csv", metavar="<ref_alleles.csv>", required=False)
    parser.add_argument("-output_dir", default=OUTPUT_DIR, metavar="<data_output/>", required=False)
    return vars(parser.parse_args())

def prepare_requests(args):
    data_ls = []
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    alleles_f = pd.read_csv(args["alleles"], converters={"length":str})
    a = ",".join(alleles_f["allele"])
    lens = ",".join(alleles_f["length"])
    logging.debug(f"a: {a}, lens: {lens}\n")

    for epi in list(SeqIO.parse(args["epitope"], "fasta")):
        logging.debug(f"epi: {epi.id}, {epi.seq}\n")
        data_ls.append((epi.id, f"method=netmhcpan_el&sequence_text=%3E{epi.id}%0A{epi.seq}&allele={a}&length={lens}"))

    return headers, data_ls

def run():
    logging.basicConfig(filename=f"{args['output_dir']}mch_i.log", encoding='utf-8', level=logging.ERROR, 
        format='%(levelname)s: %(asctime)s %(message)s:', datefmt='%m/%d/%Y %H:%M:%S')
    args = parse_arguments()
    headers, data_ls = prepare_requests(args)

    for epi_id, data in data_ls:
        response = requests.post('http://tools-cluster-interface.iedb.org/tools_api/mhci/', headers=headers, data=data)
        logging.debug(f"response: {response}")
        if not response.ok:
            logging.error(f"{response.status_code}: {response.reason}\n")
            response.raise_for_status()
        with open(f"{args['output_dir']}{epi_id}.csv", "w") as f_out:
            for line in response.iter_lines(decode_unicode=True):
                str_line = line.replace("\t", ",")
                f_out.write(str_line+"\n")

if __name__ == "__main__":
    run()