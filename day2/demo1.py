def is_id_invalid_brute_force(id_str: str):
    """Original brute force check."""
    return id_str[0:len(id_str) // 2] == id_str[len(id_str) // 2:len(id_str)]

def construct_invalid_ids(start, end):
    """Yield all invalid IDs in range [start, end] using constructive approach.
    
    An ID is invalid if its first half equals its second half.
    Only even-length numbers can satisfy this condition.
    """
    s_len, e_len = len(str(start)), len(str(end))
    
    for length in range(s_len, e_len + 1):
        # Odd lengths can never have equal halves since the halves have different lengths
        if length % 2 != 0:
            continue
        
        n = length // 2
        min_base = 10**(n - 1)
        max_base = 10**n
        
        for base in range(min_base, max_base):
            invalid_id = int(str(base) + str(base))
            if invalid_id < start:
                continue
            elif invalid_id > end:
                break
            else:
                yield invalid_id

if __name__ == "__main__":
    with open("input.txt") as f:
        ranges = f.read().split(",")
        
        # Brute force approach
        brute_force_sum = 0
        for rng in ranges:
            start, end = [int(i) for i in rng.split("-")]
            for id_val in range(start, end + 1):
                if is_id_invalid_brute_force(str(id_val)):
                    brute_force_sum += id_val
        
        # Constructive approach
        constructive_sum = 0
        for rng in ranges:
            start, end = [int(i) for i in rng.split("-")]
            for id_val in construct_invalid_ids(start, end):
                constructive_sum += id_val
        
        print(f"Brute force sum: {brute_force_sum}")
        print(f"Constructive sum: {constructive_sum}")
        assert brute_force_sum == constructive_sum, "Results do not match!"
        print("Results match! Refactoring successful.")
