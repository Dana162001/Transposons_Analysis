import pathlib

from Bio import GenBank, SeqIO


def load_gb_file(path):
    return list(SeqIO.parse(path, 'genbank'))[0]


def parse_gbff_location(location: str):
    strings_to_remove = ["complement(", ")", ">", "<"]
    for to_remove in strings_to_remove:
        location = location.replace(to_remove, "")
    return [int(x) for x in location.split("..")]


def parse_gbff_file(file_path: pathlib.Path):
    with open(file_path) as f:
        gen_cds_content = GenBank.read(f)

    mobile_elements = []
    cds = []

    for feature in gen_cds_content.features:
        if feature.key == "mobile_element":
            for qualifier in feature.qualifiers:
                if qualifier.value == '"ISEscan"':
                    location = parse_gbff_location(feature.location)
                    mobile_elements.append(location)

        if feature.key == "CDS":
            if "join" in feature.location:
                continue
            location = parse_gbff_location(feature.location)
            cds.append(location)

    return gen_cds_content.sequence, mobile_elements, cds