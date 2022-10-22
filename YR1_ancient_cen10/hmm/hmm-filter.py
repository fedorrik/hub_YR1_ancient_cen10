from sys import argv


# read list
with open('hmm.list') as f:
    hmm_list = f.read().split('\n')

# read hmm file
with open(argv[1]) as f:
    hmm = f.read()

hmm = hmm.split('//\n')[:-1]
out_hmm = []
for i in hmm:
    name = i.split('\n')[1].split()[-1]
    # put here what to filter with
    if name in hmm_list:
        out_hmm.append(i)

out_hmm = '//\n'.join(out_hmm)
print(out_hmm)
