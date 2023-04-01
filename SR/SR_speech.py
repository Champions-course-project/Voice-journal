import SR.full_record as full_record


def speech(bytes_array: bytes, framerate: int):
    """
    Распознаватель речи.\n
    Входные аргументы:
    - bytes_array - байтовый поток с аудиоинформацией;
    - framerate - частота записи.\n
    Выходные данные:
    - список возможных словосочетаний - при успешном распознавании;
    - False - при ошибке во время распознавания.
    """
    try:
        result = full_record.STT.decode_bytestream(bytes_array, framerate)
        if result:
            words_list = []
            for transcript in result['alternative']:
                words_list.append(transcript['transcript'])
            return words_list
        else:
            return False
    except Exception as exc:
        print(type(exc).__name__)
        print(exc.args)
        return False
