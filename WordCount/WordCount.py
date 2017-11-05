def WordCount(FileName,TopQty):
    '''
    'FileName' 	= text file to read in and count words
    'TopQty'	= Eg. TopQty=10 shows top 10 most occurring words
    '''

    import string
    optional_ignore=['the', 'a', 'and', 'of', 'on', 'to', 'i', 'in' ]  	# possible common words to skip
    count=dict()
    nonascii=bytearray(range(0x80,0x100)) 				# nonascii chars
    punctuation=string.punctuation.replace('\'','').replace('-','')	# ignore apostrophe and hyphens
    fh=open(FileName,'r')

    for line in fh:
        if line.isspace(): continue 					# ignore empty lines
        words=line.translate(None,punctuation+nonascii).replace('-',' ').lower().split(None)
        for word in words:
            if count.has_key(word): count[word]+=1
            else: count[word]=1
    for ignore in optional_ignore: count.pop(ignore)  # remove common words

    return sorted(count.items(),key=lambda x:x[1],reverse=True)[:TopQty]

