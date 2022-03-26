import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = "f55a817a21d442928de14333b1f5be7e", "francecentral"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
