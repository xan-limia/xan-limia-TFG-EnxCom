import config as conf
        
if conf.IS_FASTER:
    from faster_whisper import WhisperModel

    model = WhisperModel(conf.MODEL, device=conf.DEVICE, compute_type=conf.COMPUTE_TYPE)

    def transcribe(filename, language = conf.LANGUAGE, verbose = conf.VERBOSE_TRASCRIPTION):
        
        return model.transcribe(audio=filename, beam_size=5, language=language, condition_on_previous_text=verbose)
else:
    import whisper

    model = whisper.load_model(name=conf.MODEL, device=conf.DEVICE)

    def transcribe(filename, language = conf.LANGUAGE, verbose = conf.VERBOSE_TRASCRIPTION):
        
        return model.transcribe(audio=filename, beam_size=5, language=language, verbose=verbose)