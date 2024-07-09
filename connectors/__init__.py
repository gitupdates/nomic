from nomic.connectors import huggingface_connecter

atlas_dataset = huggingface_connecter.load('aaa/bbb')

atlas_dataset.create_index(topic_model=True, embedding_model='NomicEmbed') 

print("Atlas dataset has been loaded and indexed successfully.")
