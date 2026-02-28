OOD_THRESHOLD = 0.12  

def is_ood(mutual_info):
    return mutual_info.item() > OOD_THRESHOLD