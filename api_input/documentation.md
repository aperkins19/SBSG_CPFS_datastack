# Introduction

This python package will allow you to interact with the SBSG CFPS Database.

When the docker compose has spun up all of the containers in the docker network, run:

    docker exec -it api_tester /bin/bash

Then execute your scripts:
e.g.
    python test.py

# Installation

    import SBSG_api_interface.energy_solution_functions as es
    import SBSG_api_interface.amplicon_functions as amp

## EnergySolutions

### get_all_energy_solutions()

This function requires no arguments and will return a database of the entire table.

    df = es.get_all_energy_solutions()

### enter_new_energy_solution()

First define the energy solution as a python dictionary and choose a Unique_Word that has not yet been used.
e.g.

    args_es = {
    "Maker": "Alex",
    "Unique_Word": "benji",
    "Date_batch_made":"11/02/22",
    "XTimes":"4.0",
    "Description":"third tester energy sol",
    "K_Glut":"6.3",
    "Mg_Glut":0.5,
    "Tris_Base":"7.5",
    "DTT":"0.6",
    "Amino_Acids":"87",
    "Tyrosine":"5.53",
    "CoA":"0.23",
    "NAD":"0.024",
    "Folinic_Acid":"5.52",
    "cAMP":"525.9",
    "Three_PGA":"0.2235",
    "HEPES":"0.3452",
    "Spermidine":"5345.8",
    "PEG_8000":"0.3451",
    "tRNA":"0345.8",
    "ATP":"0345.5",
    "GTP":"0.34515",
    "CTP":"0.3455",
    "UTP":"3450.5"
    }

The pass it to the function to enter it into the energy_solution_table table in the database.
The exhaused parameter will automatically be set to false and a data entry timestamp generated.

    es.enter_new_energy_solution(args_es)


## Amplicons

### get_all_amplicons()

This function requires no arguments and will return a database of the entire amplicons_table.

    df = amp.get_all_amplicons()

### enter_new_amplicon()

First define the amplicon as a python dictionary and choose a Unique_Word that has not yet been used.
e.g.

    args_amp = {
    "Maker": "Alex",

    "Unique_Word": "big.fighter",

    "Date_batch_made":"11/02/22",

    "Description":"best DARPIN",

    "Template_Seq": "ccagccagaaaacgacctttctgtggtgaaaccggatgctgcaattcagagcggcagcaagtgggggacagcagaagacctgaccgccgcagagtggatgtttgacatggtgaagactatcgcaccatcagccagaaaaccgaattttgctgggtgggctaacgatatccgcctgatgcgtgaacgtgacggacgtaaccaccgcgacatgtgtgtgctgttccgctgggcatgctgagctaacaTCGAAATTAATACGACTCACTATAGGGAGACCACAACGGTTTCCCTCTAGAaataattttgtttaactttaagaaggagatataccCATATGggttcggacttaggccgcaagttactggaagctgcacgcgcgggtcaagacgacgaggtacgcatccttatggccaatggtgcggacgtcaacgccgccgataataccggaacaactcctttgcacctcgcagcatattccggccatttagagattgtagaggtactgcttaagcacggtgccgatgtagatgcgtcggacgtattcgggtacacgcctctccacctcgccgcttattggggccacttagaaattgtagaggtgctcttgaagaatggtgccgacgtgaatgctatggattcagacggcatgacaccgctccatctggccgcgaaatggggttatctggagatcgtcgaggttctcttgaaacatggcgccgacgtcaatgcacaagataagttcggcaagactgccttcgacatcagcatcgacaacggtaatgaggacctggccgagatccttcaaaagttgaatGCCGAAGCGGCCGCGAAGGAAGCGGCCGCAAAAGAGGCAGCCGCTAAAGCGatggagcttttcactggcgttgttcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgaagttcatctgcaccaccggcaagctgcccgtgccctggcccaccctcgtgaccaccctgacctacggcgtgcagtgcttcagccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccgaaggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgccgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgacttcaaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgtctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaacatcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcgacggccccgtgctgctgcccgacaaccactacctgagcacccagtccgccctgagcaaagaccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatctaaacaataactgaataggggatcccgactggcgagagccaggtaacgaatggatccccgagctcgagcaaagcccgccgaaaggcgggcttttctgtgtcgaccgatgcccttgagagccttcaacccagtcagctccttccggtgggcgcggggcatgactatcgtcgccgcacttatgactgtcttctttatcatgcaactcgtaggacaggtgccggcagcgctcttccgcttcctcgctcactgactcgctgcgctcggtcgttcggctgcggcgagcggtatcagctcactcaaaggcggtaatacggttatccacagaatcaggggataacgcaggaaagaacatgtgagcaaaagg",

    "Forward_Primer_Seq":"ggatgctgcaattcagagcg",

    "Reverse_Primer_Seq":"cccctgattctgtggataacc"
    }

The pass it to the function to enter it into the amplicons_table table in the database.
A data entry timestamp will be automatically generated.

    amp.enter_new_amplicon(args_amp)
