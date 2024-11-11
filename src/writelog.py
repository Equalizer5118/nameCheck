def write_log(d, v, uc, pgs, nimg, pgi, lf):
 log_format = '============================================================== \n' \
 f'[{d}] nameCheck Log:\n' \
 '\n' \
 f'Verified students: {v}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'YBA unverified students: {uc}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'Not in YBA/misspelled: {pgs}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'No tagged IMG: {nimg}\n' \
 '\n' \
 '\n' \
 '\n' \
 f'In total: {len(v)}/{len(pgi)} students were verified leaving {len(uc)} unverified students in Yearbook Avenue, and {len(nimg)}/{len(v)} verified students had untagged images. \n' \
 f'Additionally, {len(pgs)} students were either not in Yearbook Avenue or otherwise failed to verify, or could have multiple last names. \n' \
 '==============================================================\n' \
 '\n' 
 
 
 with lf.open("a") as file:
  file.write(log_format)