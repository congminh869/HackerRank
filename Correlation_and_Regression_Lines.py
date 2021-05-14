"""
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute Karl Pearson’s coefficient of correlation between these scores.
Compute the answer correct to three decimal places.

Output Format

In the text box, using the language of your choice, print the floating point/decimal value required. Do not leave any leading or trailing spaces.

For example, if your answer is 0.255. In python you can print using
"""


import math
ps = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
hs = [10, 25,17, 11, 13, 17, 20, 13, 9, 15]
n = len(ps)
var_ps, var_hs, cov = 0,0,0

mean_ps = sum(ps)/len(ps)
mean_hs= sum(hs)/len(hs)

for i in range(n):
    var_ps +=(int(ps[i])-mean_ps)*(int(ps[i])-mean_ps)
    var_hs += (int(hs[i])-mean_hs)*(int(hs[i])-mean_hs)
    cov    += (ps[i]-mean_ps)*(hs[i]-mean_hs)
    
var_ps = round(var_ps/(n-1),3)
var_hs = round(var_hs/(n-1),3)
cov    = round(cov/(n-1),3)

r =  round(cov/(math.sqrt(var_ps*var_hs)),3)
print(r) #0.145
