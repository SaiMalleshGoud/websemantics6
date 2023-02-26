#Importing required packages
import csv
from rdflib import Graph, Literal, Namespace, RDF, URIRef

# Defining namespaces
SCHEMA = Namespace('http://schema.org/')
MY_ONTOLOGY = Namespace('http://example.org/my_ontology#')
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")

# Loading CSV files
csv_file1 = open('reduced_dataset1.csv', 'r')
csv_file2 = open('reduced_dataset2.csv', 'r')
reader1 = csv.DictReader(csv_file1)
reader2 = csv.DictReader(csv_file2)

# Creating an RDF graph
g = Graph()
g1 = Graph()
# Iterate over the CSV rows of dataset1 and add triples to the graph
for row in reader1:
    # Creating URI for the subject
    subject_uri1 = MY_ONTOLOGY[row['ID']]
    # Adding type information
    g.add((subject_uri1, RDF.type, SCHEMA.Movies))
    # Adding Graph properties
    g.add((subject_uri1, SCHEMA.movie_title, Literal(row['title'])))
    g.add((subject_uri1, SCHEMA.release_year, Literal(row['release_year'])))
    g.add((subject_uri1, SCHEMA.locations, Literal(row['locations'])))
    g.add((subject_uri1, SCHEMA.fun_facts, Literal(row['fun_facts'])))


# Iterate over the CSV rows of dataset2 and add triples to the graph
for row in reader2:
    # Creating URI for the subject
    subject_uri2 = MY_ONTOLOGY[row['ID']]
    # Adding type information
    g1.add((subject_uri2, RDF.type, SCHEMA.Movies))
    # Adding properties
    g1.add((subject_uri2, SCHEMA.movie_title, Literal(row['title'])))
    g1.add((subject_uri2, SCHEMA.production_company, Literal(row['production_company'])))
    g1.add((subject_uri2, SCHEMA.distributor, Literal(row['distributor'])))
    g1.add((subject_uri2, SCHEMA.director, Literal(row['director'])))
    g1.add((subject_uri2, SCHEMA.writer, Literal(row['writer'])))
    g1.add((subject_uri2, SCHEMA.actor1, Literal(row['actor1'])))
    g1.add((subject_uri2, SCHEMA.actor2, Literal(row['actor2'])))
    g1.add((subject_uri2, SCHEMA.actor3, Literal(row['actor3'])))
 
# Saving data in rdf format
g.serialize('dataset1.rdf', format='xml')
g1.serialize('dataset2.rdf', format='xml')