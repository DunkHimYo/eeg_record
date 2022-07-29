from cortex2.emotiv_cortex2_client import EmotivCortex2Client

url = "wss://localhost:6868"
client = EmotivCortex2Client(url,
                 client_id='nhM6jH4dy2MWa2KT7cvo2vJKrYg04ANkl3GdDt1m',
                 client_secret="dVLsKmT5Fkzt9RHL8qWwKxRN5Oi4vWW3OePgTZnIafVIEeTcAcBP6KAVTA9L5aYTzKArOyA6BxFqF2ksnTLjI7iYwwJJyRaE5ZXoBEMhYoAvnS9mVcnk4Lc6q4FzUv7F",
                 check_response=True,
                 authenticate=True,
                 debug=True, data_deque_size=1,
                 debit=10)
client.query_headsets()
client.connect_headset(0)
client.request_access()
session_info=client.create_activated_session(0)

client.subscribe(streams=["met"])
client.create_record(title='a',session_id=session_info['id'])
record_info=client.stop_record(title='a',session_id=session_info['id'])

client.disconnect_headset(client.headset_id)
client.export_record(record_ids=record_info['record']['uuid'],folder=r'C:/Users/tjqn1/PycharmProjects/pythonProject15',stream_types=['PM'], format='CSV', version='V1')
