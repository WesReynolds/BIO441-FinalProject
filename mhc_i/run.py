import requests

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}
seqs = "%3Epeptide1%0AGHAHKVPRRLLKAAR%0A%3Epeptide2%0ALKAADASADADGSGSGSGSG"
alleles = "HLA-A*01:01,HLA-A*03:01"
lengths = "9,10"
data = f"method=netmhcpan_el&sequence_text={seqs}&allele={alleles}&length={lengths}"

response = requests.post("http://tools-cluster-interface.iedb.org/tools_api/mhci/", headers=headers, data=data)
for line in response.iter_lines(decode_unicode=True):
    str_line = line.replace("\t", ",")
    print(str_line)