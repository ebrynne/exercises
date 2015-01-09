import json

raw_json = json.loads(open("Hangouts.json").read())



Iterate over and group by conversation, ordered by timestamp
Iterate over each conversation, when chat_id is joey and comment contains "ha(h)", "hehe" "haha", ":(-))" or ":-D", 
check if previous post is from me, and then put into hashmap keyed by year+week of year

# "conversation_id" : {
#   "id" : "UgzWHzDDZMGHAGdRQGd4AaABAQ"
# },

# "sender_id" : {
#           "gaia_id" : "101686657199986751817",
#           "chat_id" : "101686657199986751817"
#         },

#         "chat_message" : {
#           "message_content" : {
#             "segment" : [ {
#               "type" : "TEXT",
#               "text" : "Argh I was really meaning 'tonight' because I'm out skiing with Bruno tmr and have a friend coming from London on Sunday. But next week for sure! Need to give you the cheese before Tiffany claims them hahaha. She loves cheese!"
#             } ]
#           }
#         },

# ebrynneID: 100701463936216967601
# joeyId: 104409389910946456363