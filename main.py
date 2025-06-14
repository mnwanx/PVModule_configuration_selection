# criterion 1: Able to fit the available roof space (Please cross-refer the outcome of Step 2)
'''
• If Ntot ≤ Nroof_max_LA and Ntot ≤ Nroof_max_LU, the optimal PV mounting arrangement is lengthwise across.
• If Ntot ≤ Nroof_max_LU and Ntot > Nroof_max_LA, the optimal PV mounting arrangement is lengthwise up.
• If Ntot > Nroof_max_LU and Ntot ≤ Nroof_max_LA, the optimal PV mounting arrangement is lengthwise across.
• If Ntot > Nroof_max_LA and Ntot > Nroof_max_LU, the PV array CANNOT fit the available roof space. Thus,
the PV array configuration does not meet this criterion. Different PV module OR inverter OR both
components should be selected in the sizing process and the sizing process should be repeated.
'''

# criterion 2: Within the optimal range of total number of PV modules that matches the inverter-to-PV array sizing ratio
'''
• If Ntot is not within the optimal range (i.e. outside the range of Ntot_opt obtained in Step 3),
different PV module OR inverter OR both components should be selected in the sizing
process. The sizing process should be repeated.
• If Ntot is within the optimal range of Ntot_opt obtained in Step 3, the PV array configuration
meets this criterion.
'''

# criterion 3: If more than one PV array configurations meet both Criterion 1 and 2, choose the PV array configuration with the largest Ntot as the final PV array configuration. Else, the sole PV array configuration that meets both Criterion 1 and 2 is selected as the final PV array configuration.


class PVConfig():
    def test(self):
        return "s"
    def lengthwise_config(self, Ntot):
        i = Ntot
        if (i <= self.Nroof_max_LA and i <= self.Nroof_max_LU) or (i > self.Nroof_max_LU and i <= self.Nroof_max_LA):
            return "LA"
        elif i <= self.Nroof_max_LU and i > self.Nroof_max_LA:
            return "LU"
        else:
            return "Dimension Error"
    def check_criterion(self):
        for i in range(1, self.Np_max_per_mppt_inv+1):
            for j in range(self.Ns_min_mp, self.Ns_max_oc+1):
                lw_config = "| " + self.lengthwise_config(i*j) + " Config"
                if (i*j in range(self.Ntot_opt[0], self.Ntot_opt[1] + 1)):
                    result = "[ + ] "
                else:
                    result = "[ - ] "
                    # lw_config = ""
                    #lw_config = "| " + self.lengthwise_config() + " Config"
                print(f"{result} {i} X {j} = {i * j} {lw_config}")
                #length_config = lengthwise_config(i*j)
                #print(length_config)


    def __init__(self, Ns_min_mp, Ns_max_oc, Np_max_per_mppt_inv, Nroof_max_LA, Nroof_max_LU, Ntot_opt):
        self.Ns_min_mp = Ns_min_mp
        self.Ns_max_oc = Ns_max_oc
        self.Np_max_per_mppt_inv = Np_max_per_mppt_inv
        self.Nroof_max_LA = Nroof_max_LA
        self.Nroof_max_LU = Nroof_max_LU
        self.Ntot_opt = Ntot_opt
    


run_check = PVConfig(
    Nroof_max_LA=20, 
    Nroof_max_LU=16, 
    Ntot_opt=[18,19], 
    Ns_max_oc=14, 
    Ns_min_mp=6, 
    Np_max_per_mppt_inv=2)

run_check.check_criterion()