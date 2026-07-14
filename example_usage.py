from client import WisprFlowVoiceSummarizerClient
client = WisprFlowVoiceSummarizerClient()
print(client.summarize_dictation("So umm we need to refactor the SQL code and err push it today."))