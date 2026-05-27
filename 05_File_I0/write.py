f=open("story.txt","w")
'''file is automatically created if file is not create
if file is created already then overwritten takes place'''
story="""once upon a time.
 A man sitting at the tree and reading a book,suddenly one apple drop on his head ."""
f.write(story)
f.close()