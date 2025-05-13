def write_log(d, v, uc, pgs, nimg, pgi, lf, pgl = 'N/A', pgcs = 'N/A', ybl = 'N/A', ybcs = 'N/A', sim = 'N/A'):
 simprint = ""
 if sim != 'N/A':
  for i in sim:
   simprint = simprint+f'            {i} \n'
 else:
  simprint = sim
 log_format = '============================================================== \n' \
 f'[{d}] nameCheck Log:\n' \
 f'Lists used -           HS: {pgl}, {pgcs}     YBA: {ybl}, {ybcs} \n' \
 '\n' \
 f'Verified students: {v}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'YBA unverified students: {uc}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'Not in YBA: {pgs}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'No tagged IMG: {nimg}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'The following students are not in YBA, but have similar names to those in YBA. These may be preferred names or misspellings: \n{simprint}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'In total: {len(v)}/{len(pgi)} students were verified leaving {len(uc)} unverified students in Yearbook Avenue, and {len(nimg)}/{len(v)} verified students had untagged images. \n' \
 f'Additionally, {len(pgs)} students were either not in Yearbook Avenue or otherwise failed to verify, or could have multiple last names, with {len(simprint)} of those names having possible matches. \n' \
 '==============================================================\n' \
 '\n' 
 
 
 with lf.open("a") as file:
  file.write(log_format)