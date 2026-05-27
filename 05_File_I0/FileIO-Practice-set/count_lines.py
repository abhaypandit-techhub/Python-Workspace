import argparse

parser=argparse.ArgumentParser(description="Count Line")
parser.add_argument("fileName")
parser.add_argument("word")
args=parser.parse_args()

count=0
word=[args.word]
with open("args.FileName",'r') as f:
  for line in f:
    if line in word:
      count=count+1

print("the total number of line : ",count)