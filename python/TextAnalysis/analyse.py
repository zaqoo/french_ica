from unicodedata import category
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


import sys

sys.path.insert(0, '../')
sys.path.insert(0, '.')
from conf import *
from ordonnance import *
from medicament import *
from examination import *

key = "653aadbe72bd4d8da93f7bf1b7cea508"
endpoint = "https://entityanalysisica.cognitiveservices.azure.com/"

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example function for recognizing entities from text
def entity_recognition_example(client, documents):

    try:
        result = client.recognize_entities(documents = documents)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                    "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")

    except Exception as err:
        print("Encountered exception. {}".format(err))

# Example function for extracting information from healthcare-related text 
def health_example(client, documents):

    poller = client.begin_analyze_healthcare_entities(documents)
    result = poller.result()

    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("...Normalized Text: {}".format(entity.normalized_text))
            print("...Category: {}".format(entity.category))
            print("...Subcategory: {}".format(entity.subcategory))
            print("...Offset: {}".format(entity.offset))
            print("...Confidence score: {}".format(entity.confidence_score))
        for relation in doc.entity_relations:
            print("Relation of type: {} has the following roles".format(relation.relation_type))
            for role in relation.roles:
                print("...Role '{}' with entity '{}'".format(role.name, role.entity.text))
        print("------------------------------------------")

def print_health_entity(entity):
    print("Entity: {}".format(entity.text))
    print("...Normalized Text: {}".format(entity.normalized_text))
    print("...Category: {}".format(entity.category))
    print("...Subcategory: {}".format(entity.subcategory))
    print("...Offset: {}".format(entity.offset))
    print("...Confidence score: {}".format(entity.confidence_score))


def searchRelation(entityRelations, name):
    for e in entityRelations:
        if e.relation_type == name:
            return e
    return None

#function for extracting health entities
def extract_medication(client, documents):
    
    poller = client.begin_analyze_healthcare_entities(documents)
    result = poller.result()
    print("poller : ")
    print(poller)
    print("result : ")
    print(result)
        
    docs = [doc for doc in result if not doc.is_error]
    print("docs :")
    print(docs)
    ordonnance = Ordonance()
        
    for idx, doc in enumerate(docs):
        for relation in doc.entity_relations:
            print("Relation of type: {} has the following roles".format(relation.relation_type))
            for role in relation.roles:
                print("...Role '{}' with entity '{}'".format(role.name, role.entity.text))

        for entity in doc.entities:
            print_health_entity(entity)
            if (entity.category == "MedicationName"):
                medicament = Medicament()
                medicament.setName(entity.text)
                ordonnance.addMedicament(medicament)
            elif (entity.category == "MedicationForm"):
                rel = searchRelation(doc.entity_relations, "FormOfMedication")
                if rel is not None:
                    index = ordonnance.getMedIndex(rel.roles[0].entity.text)
                    ordonnance.getMedicaments()[index].setForm(entity.text)
            elif (entity.category == "Frequency"):
                rel = searchRelation(doc.entity_relations, "FrequencyOfMedication")
                if rel is not None:
                    index = ordonnance.getMedIndex(rel.roles[0].entity.text)
                    ordonnance.getMedicaments()[index].setFrequency(entity.text)
            elif (entity.category == "Time"):
                rel = searchRelation(doc.entity_relations, "TimeOfMedication")
                if rel is not None:
                    index = ordonnance.getMedIndex(rel.roles[0].entity.text)
                    ordonnance.getMedicaments()[index].setDuration(entity.text)
            elif (entity.category == "Dosage"):
                rel = searchRelation(doc.entity_relations, "DosageOfMedication")
                if rel is not None:
                    index = ordonnance.getMedIndex(rel.roles[0].entity.text)
                    ordonnance.getMedicaments()[index].setDosage(entity.text)
            elif (entity.category == "ExaminationName"):
                exam = Examination(entity.text)
                ordonnance.addMedicament(exam)



        print("------------------------------------------")
        
        print("ORDONANCE EXTRACTED")
        print(ordonnance.toJSON())

def pii_recognition_example(client, documents):
    response = client.recognize_pii_entities(documents)
    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        print("Redacted Text: {}".format(doc.redacted_text))
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("\tCategory: {}".format(entity.category))
            print("\tConfidence Score: {}".format(entity.confidence_score))
            print("\tOffset: {}".format(entity.offset))
            print("\tLength: {}".format(entity.length))


def analyse_input(str):
    entity_recognition_example(client, str)
    extract_medication(client, str)
    pii_recognition_example(client, str)