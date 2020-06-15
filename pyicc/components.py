import numpy as np


# 计算总体均值，组间均值，组内均值
def mean_status(feats):
    total_mean = np.mean(feats)
    intraclass_mean = list(map(lambda x: np.mean(x), feats))
    interclass_mean = [np.mean(list(map(lambda x: x[i], feats))) for i in range(len(feats[0]))]
    return total_mean, intraclass_mean, interclass_mean


# 计算误差自由度，组间自由度，组内自由度
def degree_of_freedoms(feats):
    interclass_df = len(feats) - 1
    intraclass_df = len(feats[0]) - 1
    error_df = intraclass_df * interclass_df
    return interclass_df, intraclass_df, error_df


# 总体ss
def cal_total_SS(feats, total_mean):
    total_ss = 0
    for i in range(len(feats)):
        for j in range(len(feats[0])):
            total_ss = total_ss + np.square(feats[i][j] - total_mean)
    return total_ss


# 组间ss
def cal_inter_SS(total_mean, intraclass_mean, intra_length):
    inter_ss = 0
    for m in intraclass_mean:
        inter_ss = inter_ss + intra_length * np.square(m - total_mean)
    return inter_ss


# 组内ss
def cal_intra_SS(total_mean, interclass_mean, inter_length):
    intra_ss = 0
    for m in interclass_mean:
        intra_ss = intra_ss + inter_length * np.square(m - total_mean)
    return intra_ss


# 计算各个均方
def cal_MS(feats, total_mean, intraclass_mean, interclass_mean):
    total_ss = cal_total_SS(feats=feats,
                            total_mean=total_mean)
    inter_ss = cal_inter_SS(total_mean=total_mean,
                            intraclass_mean=intraclass_mean,
                            intra_length=len(feats[0]))
    intra_ss = cal_intra_SS(total_mean=total_mean,
                            interclass_mean=interclass_mean,
                            inter_length=len(feats))
    error_ss = total_ss - inter_ss - intra_ss
    interclass_df, intraclass_df, error_df = degree_of_freedoms(feats=feats)
    inter_ms = inter_ss / interclass_df
    intra_ms = intra_ss / intraclass_df
    error_ms = error_ss / error_df
    return inter_ms, intra_ms, error_ms


def cal_status(feats):
    total_mean, intraclass_mean, interclass_mean = mean_status(feats)
    inter_ms, intra_ms, error_ms = cal_MS(feats=feats,
                                          total_mean=total_mean,
                                          intraclass_mean=intraclass_mean,
                                          interclass_mean=interclass_mean)
    return inter_ms, intra_ms, error_ms


