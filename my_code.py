import pytest

def fix_phone_num(phone_num_to_fix):
    # (Step 5 and 7 Revisions)

    # Allow only digits
    if not phone_num_to_fix.isdigit():
        raise ValueError("Phone number contains invalid characters.")
        
    # Remove all non-digit characters to clean the number
    cleaned_num = ''.join(filter(str.isdigit, phone_num_to_fix))

    # Check that the phone number contains exactly 10 digits
    if len(cleaned_num) != 10:
        raise ValueError("Phone number must be exactly 10 digits long.")

    # Split the parts and recombine into the standard phone format
    area_code = cleaned_num[0:3]  # 512 (first three digits)
    three_part = cleaned_num[3:6]  # 555 (next three digits)
    four_part = cleaned_num[6:]  # 8823 (last four digits)
  
    # Format and return the fixed phone number
    fixed_num = f"({area_code}) {three_part} {four_part}"
  
    return fixed_num


def test_fix_phone_num():
    # Original working case
    assert fix_phone_num("5125558823") == '(512) 555 8823'
    
    # Additional assertions (Step 1)
    assert fix_phone_num("5554429876") == '(555) 442 9876'
    assert fix_phone_num("3216543333") == '(321) 654 3333'


# def test_fix_phone_num_fail():
#     # Failed input cases (Step 2)
#     assert fix_phone_num("555-442-98761") == '(555) 442 9876'
#     assert fix_phone_num("(321) 654 3333") == '(321) 654 3333'


def test_fix_phone_num_value_error():
    # ValueError cases for non-digit characters and incorrect length (Step 4)
    with pytest.raises(ValueError):
        fix_phone_num("invalid123")  # Non-digit characters

    with pytest.raises(ValueError):
        fix_phone_num("123456789")  # Too short

    with pytest.raises(ValueError):
        fix_phone_num("123456789012")  # Too long


def test_fix_phone_num_non_digits():
    # Test that a ValueError is raised if the input contains non-digit characters (Step 5)
    with pytest.raises(ValueError):
        fix_phone_num("555-442-9876")  # Contains hyphens
    
    with pytest.raises(ValueError):
        fix_phone_num("abc1234567")  # Contains letters
    
    with pytest.raises(ValueError):
        fix_phone_num("123 456 7890")  # Contains spaces
