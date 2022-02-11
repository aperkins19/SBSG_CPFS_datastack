
# Installation

    import SBSG_api_interface.energy_solution_functions as es
    import SBSG_api_interface.amplicon_functions as amp

## EnergySolutions

### Get get_all_energy_solutions

This function requires no arguments and will return a database of the entire table.

    df = es.get_all_energy_solutions()


#es.create_table()
#es.enter_new_energy_solution(args_Es)
#df = es.get_all_energy_solutions()
#amp.enter_new_amplicon(args_amp)
df = amp.get_all_amplicons()
print(df['Template_Seq'])
