# criterion 1: Able to fit the available roof space (Please cross-refer the outcome of Step 2)
'''
• If Ntot ≤ Nroof_max_LA and Ntot ≤ Nroof_max_LU = lengthwise across.
• If Ntot ≤ Nroof_max_LU and Ntot > Nroof_max_LA = lengthwise up.
• If Ntot > Nroof_max_LU and Ntot ≤ Nroof_max_LA = lengthwise across.
• If Ntot > Nroof_max_LA and Ntot > Nroof_max_LU = X
'''

# criterion 2: Within the optimal range of total number of PV modules that matches the inverter-to-PV array sizing ratio
'''
• If Ntot is not within the optimal range (Ntot.e. outside the range of Ntot_opt obtained in Step 3),
different PV module OR inverter OR both components should be selected in the sizing
process. The sizing process should be repeated.
• If Ntot is within the optimal range of Ntot_opt obtained in Step 3, the PV array configuration
meets this criterion.
'''

# criterion 3: If more than one PV array configurations meet both Criterion 1 and 2, choose the PV array configuration with the largest Ntot as the final PV array configuration. Else, the sole PV array configuration that meets both Criterion 1 and 2 is selected as the final PV array configuration.


class PVConfig():
    def print_table(self):
        col_widths = [max(len(str(x)) for x in col) for col in zip(*([self.headers] + self.data))]
        
        def format_row(row):
            return " | ".join(f"{str(x):<{w}}" for x, w in zip(row, col_widths))
        
        line = "-+-".join('-' * w for w in col_widths)
        print(format_row(self.headers))
        print(line)
        for row in self.data:
            # print(format_row(row[3][0]))
            print(format_row(row))
    
    def lengthwise_config(self, Ntot):
        criterion_2 = "❌"
        if Ntot <= self.Nroof_max_LA and Ntot <= self.Nroof_max_LU:
            criterion_2 = "✅"
        elif Ntot <= self.Nroof_max_LU and Ntot > self.Nroof_max_LA:
            criterion_2 = "✅"
        elif Ntot > self.Nroof_max_LU and Ntot <= self.Nroof_max_LA:
            criterion_2 = "✅"
        return criterion_2
    def check_criterion(self):
        current_max = 0
        for Ntot in range(1, self.Np_max_per_mppt_inv+1):
            for j in range(self.Ns_min_mp, self.Ns_max_oc+1):
                lw_config = self.lengthwise_config(Ntot*j)
                star = " "
                if (Ntot*j in range(self.Ntot_opt[0], self.Ntot_opt[1] + 1)):
                    result = "✅"
                    star = "*"
                else:
                    result = "❌"
                    # lw_config = ""
                    #lw_config = "| " + self.lengthwise_config() + " Config"
                # print(f"{result} {Ntot} X {j} = {Ntot * j} {lw_config}")
                #length_config = lengthwise_config(Ntot*j)
                #print(length_config)
                self.data.append([f"{star}{Ntot} X {j} = {Ntot * j}", f"{lw_config}", result])
                # if j == 8:
                #     break

    def __init__(self, Ns_min_mp, Ns_max_oc, Np_max_per_mppt_inv, Nroof_max_LA, Nroof_max_LU, Ntot_opt):
        self.headers = ["Dimension", "Criterion 1", "Criterion 2"]
        self.data = []
        self.Ns_min_mp = Ns_min_mp
        self.Ns_max_oc = Ns_max_oc
        self.Np_max_per_mppt_inv = Np_max_per_mppt_inv
        self.Nroof_max_LA = Nroof_max_LA
        self.Nroof_max_LU = Nroof_max_LU
        self.Ntot_opt = Ntot_opt
    


run_check = PVConfig(
    Nroof_max_LA=25, 
    Nroof_max_LU=27, 
    Ntot_opt=[24,26], 
    Ns_max_oc=27, 
    Ns_min_mp=8, 
    Np_max_per_mppt_inv=2)

run_check.check_criterion()
run_check.print_table()


