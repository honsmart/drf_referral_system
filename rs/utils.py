import datetime

def generate_ref_code():
    timestamp = datetime.datetime.now().strftime("%s%f")[:14]
    referral_code = timestamp
    return referral_code[:8]