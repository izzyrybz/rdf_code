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
commit = {"commit_ref": "", "author": "", "description": "", "date":"" }
history = []
date_format = " %a %b %d %H:%M:%S %Y %z"



def isdictempty(dict):
    for value in dict.values():
        if value:
            return False
        else:
            return True


def info_between_elements(lst, A, B):
    #print(lst)
    result = []
    first_commit_flag = True
    found_A = False
    for i, elem in enumerate(lst):
        #print(elem)
        if A in elem:
            found_A = True
        if found_A:
            elem = elem.strip()
            #print(elem)
            result.append(elem)
        if B in elem:
            if first_commit_flag:
                first_commit_flag=False
                continue
            else:
                break
    result.pop(0)
    result.pop(1)
    #for result
    #print(result)
    return result



with open(path,'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        if line == ['']:
            continue
        #print(line)
        for index, element in enumerate(line):
            #print(index,element)
            if ('commit' in element and not ('Initial'in element)):
                hash = element[element.index(":") + 1:]
                commit["commit_ref"]  = hash
            if('Author:' in element): 
                #print("adding person",line[index+1])
                name = element[element.index(":") + 1:]
                commit["author"] = name
            if('Description:' in element): 
                #print("adding person",line[index+1])
                description = element[element.index(":") + 1:]
                commit["description"] = description
            if('Date:' in element):
                date = element[element.index(":") + 1:]
                #print("THIS IS DATE:",date)
                date_obj = datetime.strptime(date, date_format)
                #print(date_obj)
                commit["date"] = date_obj
            if('------' in element):
                history.append(commit)
                commit = copy.deepcopy(commit)


            #print("--"*15)
            #print(commit)
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

