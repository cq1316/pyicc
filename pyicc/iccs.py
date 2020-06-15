from pyicc.components import cal_status


def icc1(feats):
    inter_ms, intra_ms, error_ms = cal_status(feats=feats)
    numerator = (intra_ms - error_ms) / len(feats)
    denominator = (intra_ms - error_ms) / len(feats) + error_ms
    icc1 = numerator / denominator
    return icc1


def icc2(feats):
    inter_ms, intra_ms, error_ms = cal_status(feats=feats)
    numerator = (intra_ms - error_ms) / len(feats)
    denominator = (intra_ms - error_ms) / len(feats) + error_ms + (inter_ms - error_ms) / len(feats[0])
    icc2 = numerator / denominator
    return icc2


def icc3(feats):
    inter_ms, intra_ms, error_ms = cal_status(feats=feats)
    numerator = intra_ms - (len(feats[0]) / (len(feats[0]) - 1)) * error_ms
    denominator = intra_ms + (len(feats) - 1) * (len(feats[0]) / (len(feats[0]) - 1)) * error_ms
    icc3 = numerator / denominator
    return icc3


def icc4(feats):
    inter_ms, intra_ms, error_ms = cal_status(feats=feats)
    numerator = intra_ms - error_ms
    denominator = intra_ms + (len(feats) - 1) * error_ms + (len(feats) / len(feats[0])) * (inter_ms - error_ms)
    icc4 = numerator / denominator
    return icc4

