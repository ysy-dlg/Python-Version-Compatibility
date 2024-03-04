def OT_eval(candidates_input, constraint_input):
    # It's much cleaner to handle base cases for recursion **first**.
    if not (constraint_input and candidates_input):
        # We ran out of one or the other. BTW, your original code doesn't
        # consider the case of an overly constrained situation.
        return (candidates_input, constraint_input)

    constraint = constraint_input[0]
    # At first I was going to replace the call to `.sort()` by using 
    # the free function `sorted` to maintain the "functional" theme. 
    # However, you don't really need to sort the list, as far as I can
    # tell; you just need to find the minimum and use it as a basis for
    # comparison.
    violations = [
        (len(re.findall(constraint, candidate)), candidate)
        for candidate in candidates_input
    ]

    # Now we create "all candidates with more than the minimum violations"
    minimal_violations = min(violations)[0]
    violators = [
        candidate
        for violation_count, candidate in violations
        if violation_count > minimal_violations
    ]
    # And hence "all candidates without that many violations"
    good_candidates = [
        candidate
        for candidate in input_candidates
        if candidate not in violators
    ]     

    # And now we can recurse.
    return OT_eval(good_candidates, constraint_input[1:])

# Then, outside, we do the actual result processing and output:

final_candidates, final_constraints = OT_eval(candidates, constraints)

if final_constraints:
    print "No candidates survived the selection process."
elif len(final_candidates) != 1:
    print "Couldn't determine a winner."
else:
    print "The winner is:", final_candidates[0]