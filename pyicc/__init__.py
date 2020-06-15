from pyicc.iccs import icc1, icc2, icc3, icc4


def _icc(feat_dfs, method, threshold):
    feat_ind = []
    for i in range(feat_dfs[0].shape[1]):
        feats = []
        for feat_df in feat_dfs:
            feats.append(feat_df[:][i].values)
        if method == "icc1":
            icc = icc1(feats)
        elif method == "icc2":
            icc = icc2(feats)
        elif method == "icc3":
            icc = icc3(feats)
        elif method == "icc4":
            icc = icc4(feats)
        else:
            icc = icc3(feats)
        if icc >= threshold:
            feat_ind.append(i)
    return feat_ind
