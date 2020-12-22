import json

class eventFormEntries(object):
    
    def __init__(self, eventID, eventName, partnersName, eventDate, eventType, teamSize, eventOwner, eventDesc):
        self.eventID = eventID
        self.eventName = eventName
        self.partnersName = partnersName
        self.eventDate = eventDate
        self.eventType = eventType
        self.teamSize = teamSize
        self.eventOwner = eventOwner
        self.eventDesc = eventDesc

    def mergeUserInputTemplate(self, eventCollection):
        
        #Insert static template
        doc = open('static/eventTemplate.json' , encoding='utf8')
        doc = json.load(doc)
        
        #Set ID of current entry with PLM Project Name
        doc['_id']  = self.eventID
        
        #Merge User Input Details with static template
        for key in doc['allMajorEvents']:
            key['mainEvent']['eventName'] = self.eventName
            key['mainEvent']['description'] += '\n'+ 'Event Details: \n' + self.eventDesc
            key['mainEvent']['startDate'] = self.eventDate
            key['mainEvent']['dueDate'] = self.eventDate
            key['mainEvent']['eventOwner'] = self.eventOwner

            for subkey in key['subEvents']:
                subkey['eventName'] = self.eventName
                subkey['description'] += self.eventDesc
                subkey['startDate'] = self.eventDate
                subkey['dueDate'] = self.eventDate
                subkey['eventOwner']= self.eventOwner
                
        print("Document merged for Project "+doc['_id'])
        
        eventCollection.insert_one(doc)
        print("Date inserted into DB for Project code: "+doc['_id'])
