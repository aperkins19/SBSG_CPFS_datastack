
#args = {
#"Maker": "Alex",
#"Date":"09/02/22",
#"XTimes":4.0,
#"Description":"First tester energy sol",
#"K_Glut":0.3,
#"Mg_Glut":0.4,
#"Tris_Base":0.5,
#"DTT":0.6,
#"Amino_Acids":0.7,
#"Tyrosine":0.3,
#"CoA":0.2,
#"NAD":0.04,
#"Folinic_Acid":0.2,
#"cAMP":0.9,
#"Three_PGA":0.2,
#"HEPES":0.2,
#"Spermidine":0.8,
#"PEG_8000":0.1,
#"tRNA":0.8,
#"ATP":0.5,
#"GTP":0.5,
#"CTP":0.5,
#"UTP":0.5
#}

args_Es = {
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

args_amp = {
"Maker": "Alex",
"Unique_Word": "big.fighter",
"Date_batch_made":"11/02/22",
"Description":"best DARPIN",
"Template_Seq": "ccagccagaaaacgacctttctgtggtgaaaccggatgctgcaattcagagcggcagcaagtgggggacagcagaagacctgaccgccgcagagtggatgtttgacatggtgaagactatcgcaccatcagccagaaaaccgaattttgctgggtgggctaacgatatccgcctgatgcgtgaacgtgacggacgtaaccaccgcgacatgtgtgtgctgttccgctgggcatgctgagctaacaTCGAAATTAATACGACTCACTATAGGGAGACCACAACGGTTTCCCTCTAGAaataattttgtttaactttaagaaggagatataccCATATGggttcggacttaggccgcaagttactggaagctgcacgcgcgggtcaagacgacgaggtacgcatccttatggccaatggtgcggacgtcaacgccgccgataataccggaacaactcctttgcacctcgcagcatattccggccatttagagattgtagaggtactgcttaagcacggtgccgatgtagatgcgtcggacgtattcgggtacacgcctctccacctcgccgcttattggggccacttagaaattgtagaggtgctcttgaagaatggtgccgacgtgaatgctatggattcagacggcatgacaccgctccatctggccgcgaaatggggttatctggagatcgtcgaggttctcttgaaacatggcgccgacgtcaatgcacaagataagttcggcaagactgccttcgacatcagcatcgacaacggtaatgaggacctggccgagatccttcaaaagttgaatGCCGAAGCGGCCGCGAAGGAAGCGGCCGCAAAAGAGGCAGCCGCTAAAGCGatggagcttttcactggcgttgttcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgaagttcatctgcaccaccggcaagctgcccgtgccctggcccaccctcgtgaccaccctgacctacggcgtgcagtgcttcagccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccgaaggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgccgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgacttcaaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgtctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaacatcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcgacggccccgtgctgctgcccgacaaccactacctgagcacccagtccgccctgagcaaagaccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatctaaacaataactgaataggggatcccgactggcgagagccaggtaacgaatggatccccgagctcgagcaaagcccgccgaaaggcgggcttttctgtgtcgaccgatgcccttgagagccttcaacccagtcagctccttccggtgggcgcggggcatgactatcgtcgccgcacttatgactgtcttctttatcatgcaactcgtaggacaggtgccggcagcgctcttccgcttcctcgctcactgactcgctgcgctcggtcgttcggctgcggcgagcggtatcagctcactcaaaggcggtaatacggttatccacagaatcaggggataacgcaggaaagaacatgtgagcaaaagg",
"Forward_Primer_Seq":"ggatgctgcaattcagagcg",
"Reverse_Primer_Seq":"cccctgattctgtggataacc"

}



import SBSG_api_interface.energy_solution_functions as es
import SBSG_api_interface.amplicon_functions as amp
#es.create_table()
#es.enter_new_energy_solution(args_Es)
#df = es.get_all_energy_solutions()
#amp.enter_new_amplicon(args_amp)
df = amp.get_all_amplicons()
print(df['Template_Seq'])
