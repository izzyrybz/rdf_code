from rdflib import Graph, Literal, RDF, URIRef
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import FOAF , XSD
from datetime import datetime
import copy

g = Graph()

# Create an RDF URI node to use as the subject for multiple triples

# Add triples using store's add() method.
'''g.add((test, RDF.type, FOAF.Person))
g.add((test, FOAF.nick, Literal("test", lang="en")))
g.add((test, FOAF.name, Literal("test Fales")))
g.add((test, FOAF.mbox, URIRef("mailto:test@example.org")))'''



#file__name= input("Please provide the file which the history of commits exists:")
path = '/home/vm/Git2RDF_test/commithistory.txt'
commit = {"commit_ref": "", "author": "", "action": "", "date":"" }
history = []
date_format = "%d,%b,%Y,%H:%M:%S%z"



def isdictempty(dict):
    for value in dict.values():
        if value:
            return False
        else:
            return True



with open(path,'r') as f:
    for line in f:
        #trim whitespace and split line
        if(line.isspace()):
            continue
        line = line.split()
        #print(line)
      
        for index, element in enumerate(line):
            #print(index,element)
            if (element == 'commit' and not (line[index-1]== 'Initial')):
                if(isdictempty(commit)):
                    #This is the first commit in the file
                    #print("This is the first commit in the file")
                    commit["commit_ref"]  = line[index+1]
                else:
                    #This is a start of a new commit
                    history.append(commit)
                    commit = copy.deepcopy(commit)
                    commit["commit_ref"] = line[index + 1]

            if(element == 'Author:'): 
                #print("adding person",line[index+1])
                commit["author"] = line[index+1]
            if(element == 'Date:'):
                date = line[index+3]+','+line[index+2]+','+line[index+5]+','+line[index+4]+line[index+6]
                #print("THIS IS DATE:",date)
                date_obj = datetime.strptime(date, date_format)
                #print(date_obj)
                commit["date"] = date_obj
                


        #history.append(commit)
    print(history)

            


#question =  input("What is your question?")


'''# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))
#test = URIRef("http://example.org/test")
            if(element == 'Author:'): 
                print("adding person",line[index+1])
                #g.add((test, RDF.type, FOAF.Person))
                #g.add((test, RDF.type, Literal(line[index-2])))
                #g.add((test, FOAF.maker, Literal(line[index+1])))'''

