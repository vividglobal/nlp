import json
import pymongo
import random
from pymongo import MongoClient


open('nlu.yml', 'w').close()
open('domain2.yml', 'w').close()
open('stories.yml', 'w').close()
# myclient = pymongo.MongoClient("mongodb://13.231.230.27:27017/")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dev_database"]
keywordsDB = mydb["keywords"]
x = keywordsDB.find({'BotId':'60cc4c783498c3a7075bb747'})
x=x[0]
# print(x['Layout']['vi'])
i = 0 #index of intents
t = 0 #index of utters
listIntents=[]
with open("domain2.yml", "w", encoding= "utf8") as f:
	f.write('version: "2.0"\n\nintents:' + '\n')
with open("nlu.yml", "w", encoding= "utf8") as f:
	f.write('version: "2.0"\n\nnlu:' + '\n')
with open("stories.yml", "w", encoding= "utf8") as f:
	f.write('version: "2.0"\n\nstories:' + '\n')

for group in x['Layout']['vi']:
	for block in group['value']:
		i+=1
		intents = block['userSays'].split(',')
		if(len(intents)>2):
			if(intents[0] not in listIntents or intents[1] not in listIntents):       
				with open("nlu.yml", "a", encoding= "utf8") as f:
					f.write('- intent: i_' + str(i) + '\n')
					f.write('  examples: |\n')
					for intent in intents:
						listIntents.append(intent)
						f.write("    - " + intent.lower().strip())
						f.write("\n")

				with open("stories.yml", "a", encoding= "utf8") as f:
					f.write('- story: s_' + str(i) + '\n')
					f.write('  steps:\n')
					f.write("  - intent: i_" + str(i) + '\n')
					f.write("  - action: utter_" + str(i) + '\n')

				with open("domain2.yml", "a", encoding= "utf8") as f:
					f.write('- i_' + str(i) + '\n')
					# for b in a['botReplys']:
					#     f.write("   - " + b)
					#     f.write("\n")
with open("domain2.yml", "a", encoding= "utf8") as f:
	f.write('responses:' + '\n')
i=0
for group in x['Layout']['vi']:
	for block in group['value']:
		i+=1
		with open("domain2.yml", "a", encoding= "utf8") as f:
			f.write("  utter_" + str(i) + ':\n')
			for answer in block['botReplys']:
				if(type(answer)==list):
					for card in answer:
						f.write("  - custom:\n")
						f.write("      blocks:\n")
						f.write("      - type: section\n")
						f.write("        card: "+card.strip()+"\n")
						f.write("        status: ok" + '\n')


				else:
					answer=answer.replace(":"," ").replace("\n"," ")
					f.write("  - custom:\n")
					f.write("      blocks:\n")
					f.write("      - type: section\n")
					f.write("        text: "+answer+"\n")
					f.write("        status: ok" + '\n')
with open("domain2.yml", "a", encoding= "utf8") as f:
	f.write("  utter_other:" + '\n')
	f.write("  - custom:\n")
	f.write("      blocks:\n")
	f.write("      - type: section\n")
	f.write("        status: notfound" + '\n')
# with open("domain2.yml", "a", encoding= "utf8") as f:
# 	for j in range(i):
# 		f.write('- utter_' + str(j+1) + '\n')
# 	f.write('- utter_other')

with open("domain2.yml", "a", encoding= "utf8") as f:
	f.write("session_config:\n")
	f.write("  session_expiration_time: 60\n")
	f.write("  carry_over_slots_to_new_session: true\n")


print(listIntents)