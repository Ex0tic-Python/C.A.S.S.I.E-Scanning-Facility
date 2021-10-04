from os import getcwd

wav_type_dict = {
    'intercom': 'CASSIE_Intercom',
    'letter': 'CASSIE_Letters',
    'number': 'CASSIE_Numbers',
    'sentence': 'CASSIE_Sentences',
    'word': 'CASSIE_Words'
}

def get_wav_path(wav_type, wav_name):
    return f'{getcwd()}\CASSIE\{wav_type_dict[wav_type]}\{wav_type}_{wav_name}.wav'
