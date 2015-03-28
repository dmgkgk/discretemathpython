print "p \t q \t r \t ~p or q \t r->p \t ((~p) or q) -> (r->p))"
for p in [True, False]:
  for q in [True, False]:
    for r in [True, False]:
      pi1 = (not p) or q
      pi2 = (not r) or p
      pi = (not pi1) or pi2
      print p, "\t", q, "\t", r, "\t", pi1, "\t\t", pi2, "\t\t", pi
     
