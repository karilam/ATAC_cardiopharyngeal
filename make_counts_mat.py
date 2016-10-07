cond_peak_counts = dict()
peaks = set()

for fil in os.listdir('/home/kari/Documents/ATAC_analysis/bedtools_multicov_counts'):
	f = file(os.path.join('/home/kari/Documents/ATAC_analysis/bedtools_multicov_counts',fil))
	cond_peak_counts[fil] = dict()
	counts = filter(len, f.read().split('\n'))
	for i in range(len(counts)):
		cols = counts[i].split('\t')
		cond_peak_counts[fil][cols[3]] = cols[4]
		peaks.add(cols[3])


w = file('/home/kari/Documents/ATAC_analysis/610151820_counts.txt','w')

conds = os.listdir('/home/kari/Documents/ATAC_analysis/bedtools_multicov_counts')
peaks = list(peaks)

w.write('peaks' + '\t' + '\t'.join(conds) + '\n')
for i in range(len(peaks)):
	w.write(peaks[i])
	for j in range(len(conds)):
		w.write('\t' + cond_peak_counts[conds[j]][peaks[i]])
	w.write('\n')
	
