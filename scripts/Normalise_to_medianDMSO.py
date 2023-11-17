median_dmso = ann.loc[ann['sample'] == 'DMSO', 'NormBg'].median()
ann['NormDMSO'] = ann['NormBg'] / median_dmso
ann['logNormDMSO'] = np.log2(ann['NormDMSO'] + 1)

median_norm_dmso = ann['NormDMSO'].median()
mad_norm_dmso = ann['NormDMSO'].mad()
ann['ZscoreRobust'] = (ann['NormDMSO'] - median_norm_dmso) / mad_norm_dmso

median_log_norm_dmso = ann['logNormDMSO'].median()
mad_log_norm_dmso = ann['logNormDMSO'].mad()
ann['ZscoreRobustLog'] = (ann['logNormDMSO'] - median_log_norm_dmso) / mad_log_norm_dmso
