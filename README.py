meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "MOMAZO: un muy buen meme"
            "MEME: imagen chitosa"
            "FUNA: Efectuar un acto público de agravio y denuncia"
            "BOOMER:persona anciana"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print(palabra no encontrada.)
