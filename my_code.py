import pytest

def fix_phone_num(phone_num_to_fix):
    # given "5125558823". Split the parts, then recombine and return
    area_code = phone_num_to_fix[0:3] # 512 (first three digits)
    three_part = phone_num_to_fix[3:6] # 555 (next three digits)
    four_part = phone_num_to_fix[6:] # # 8823 (last four digits)
  
    fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
    return fixed_num

def test_fix_phone_num():
    # Original assertion
    assert fix_phone_num("5125558823") == '(512) 555 8823'
    
    # Additional assertions (Step 1)
    assert fix_phone_num("5554429876") == '(555) 442 9876'
    assert fix_phone_num("3216543333") == '(321) 654 3333'
    
def test_fix_phone_num_fail():
    # Failed input cases (Step 2)
    assert fix_phone_num("555-442-98761") == '(555) 442 9876'
    assert fix_phone_num("(321) 654 3333") == '(321) 654 3333'