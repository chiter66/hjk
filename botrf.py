import telebot
from telebot import types
import random
import time
from telebot.types import InputMediaPhoto, InputMediaVideo


bot = telebot.TeleBot('6734100186:AAHydnwFQLNereoNh-8X-gMnxNqzeufRuwA')



card_images = {

   1: 'AgACAgIAAxkBAAICAAFmmmBalZSz3Lu7AAHxpZ8EMaeIZ70AAkvdMRuZRNFIZHVYSpjdDVgBAAMCAAN4AAM1BA',
   2: 'AgACAgIAAxkBAAICAWaaYFrD8TBxCkmDzPd_5DOZm74NAAJN3TEbmUTRSFNNPNCD6BqxAQADAgADeAADNQQ',
   3: 'AgACAgIAAxkBAAICA2aaYFr6nakjgOMOsa1FO5hhx1X7AAKm4jEbMyrRSI93dAuApg6yAQADAgADeAADNQQ',
   4: 'AgACAgIAAxkBAAICAmaaYFoEF2l-7yrIpEm0rArq_jivAAJS3TEbmUTRSNcjkQPFoh94AQADAgADeAADNQQ',
   5: 'AgACAgIAAxkBAAICBGaaYFqr4tLMXJGBoyURcgMJBliSAAKp4jEbMyrRSHVZSFnwsoxNAQADAgADeQADNQQ',
   6: 'AgACAgIAAxkBAAICBWaaYFo-RjNJLddoczAnRg8U1Op5AAKs4jEbMyrRSGBnFxCXkVPxAQADAgADeAADNQQ',
   7: 'AgACAgIAAxkBAAICDGaabMKdLaN-MwSFOj6XOBv9KrV7AALV4jEbMyrRSDaqyZWJ6jkYAQADAgADeAADNQQ',
   8: 'AgACAgIAAxkBAAICDWaabML-WmjRGwYj2kjeZ6W_XOGEAALW4jEbMyrRSE14ksZLkIHFAQADAgADeQADNQQ',
   9: 'AgACAgIAAxkBAAICDmaabMKvUqC0SP_AXCwfmmgKQ3rNAALZ4jEbMyrRSCbEjD-03NXgAQADAgADeQADNQQ',
   10: 'AgACAgIAAxkBAAICD2aabMIrZN-_1v4_5XuyH4AIFTQJAALc4jEbMyrRSBMYvEC_NJyTAQADAgADeQADNQQ',
   11: 'AgACAgIAAxkBAAICEGaabMJRqjA9rYUXaOZsrZj-IbZEAALf4jEbMyrRSNjbrpzuwOZ5AQADAgADeQADNQQ',
   12: 'AgACAgIAAxkBAAICF2aabUq6-WdnZPjnLF4RG45n2ovnAAL04jEbMyrRSJ6K5neVmInBAQADAgADeAADNQQ',
   13: 'AgACAgIAAxkBAAICFmaabUpYGa6zY9HDs5YTnuoAAcT9lgACWN0xG5lE0Uj5a4BkEuVO8AEAAwIAA3kAAzUE',
   14: 'AgACAgIAAxkBAAICGGaabUo_QhnRTxpP2xENg5X9df1JAAL14jEbMyrRSHpkkhvO8FAyAQADAgADeAADNQQ',
   15:'AgACAgIAAxkBAAICGWaabUp4xcN9kj8yH_-sqNtsw8G6AAL44jEbMyrRSK8Y8EmMNKrxAQADAgADeQADNQQ',
   16: 'AgACAgIAAxkBAAICGmaabUoMncFoB5SKsdAMlEw6W-XQAAL64jEbMyrRSJoNqMZ9ZDUDAQADAgADeAADNQQ',
   17: 'AgACAgIAAxkBAAICIGaabaekHzu3ryBL_dbFi-VQ4yd7AAJh4jEbvAixSILe_6PSdDDlAQADAgADeQADNQQ',
   18: 'AgACAgIAAxkBAAICIWaabae-0fgtZDbAWTp2UaxkbQ_LAAJr4jEbvAixSEkw9H14Z0NkAQADAgADeQADNQQ',
   19: 'AgACAgIAAxkBAAICImaabaecl_LWP-STt0I4c3-TlrdoAAJt4jEbvAixSDD75bfwK49nAQADAgADeAADNQQ',
   20: 'AgACAgIAAxkBAAICI2aabae0Ly8Cf04c9UasZdqUHD2EAAJx4jEbvAixSFhSe_zW_133AQADAgADeAADNQQ',
   21: 'AgACAgIAAxkBAAICJGaabac9U0VBu4lpxy3qi54DPo9iAAJz4jEbvAixSBDWAAG9gIGpnwEAAwIAA3gAAzUE',
   22: 'AgACAgIAAxkBAAICJWaabaetdJcuG2c_MAjrpkt0fDNBAAJg3TEbmUTRSBuM9V8AAdnKugEAAwIAA3kAAzUE',
   23: 'AgACAgIAAxkBAAICJ2aabaesr0iQeUalYc-4wzJvc3aLAAKB4jEbMyrRSJntGV_3eThDAQADAgADeQADNQQ',
   24: 'AgACAgIAAxkBAAICJmaabadNZIURnxUjp8W4LezSZdQAA3fiMRszKtFIQ7y6CP2m6H4BAAMCAAN5AAM1BA',
   25: 'AgACAgIAAxkBAAICKGaabae3j3ypZ4Hs5SV9pOfL4BrlAAKE4jEbMyrRSLENdEzUdhJnAQADAgADeQADNQQ',
   26: 'AgACAgIAAxkBAAICMmaablfcaZ5LyaFrvymbhpUrf-CYAAKq2jEbfnewSO6vXaS7sdj5AQADAgADeQADNQQ',
   27: 'AgACAgIAAxkBAAICM2aablebGhlO08O9sE7W5GlUDy-SAAKs2jEbfnewSF1UB0x6rD4kAQADAgADeAADNQQ',
   28: 'AgACAgIAAxkBAAICNGaablfYjoRqcDaFPNZIw9TmMm82AAKt2jEbfnewSH-fThyDifG2AQADAgADeQADNQQ',
   29: 'AgACAgIAAxkBAAICNWaablebeSRgMFEW-s6R21_pJg7pAAK62jEbfnewSEP0Ut9u3xZeAQADAgADeQADNQQ',
   30: 'AgACAgIAAxkBAAICNmaablfCJBuDniQEYgABQvm-xtf4RQACvdoxG353sEh_ZxAldFq_6gEAAwIAA3gAAzUE',
   31: 'AgACAgIAAxkBAAICN2aabldUDXALWTpXUS6xBMAvGnCIAAK_2jEbfnewSHUb9Xwo-I6BAQADAgADeQADNQQ',
   32: 'AgACAgIAAxkBAAICOGaabldPOLzsaV0jdlVH7QkGFDKQAAKL4jEbMyrRSD_pEpf7CaBiAQADAgADeQADNQQ',
   33: 'AgACAgIAAxkBAAICOWaablcTP_9dgnUxh1wBc_obY8VoAAK34jEbMyrRSFLUBc6WFP69AQADAgADeAADNQQ',
   34: 'AgACAgIAAxkBAAICO2aablfJufmKClQucA6R6ng3l-blAALK4jEbMyrRSC83IeVrKUTLAQADAgADeQADNQQ',
   35: 'AgACAgIAAxkBAAICOmaabldUB_Kp55ay8Nc1HRbnym2zAAK-4jEbMyrRSEMuz3hnpmK1AQADAgADeQADNQQ',
   36: 'AgACAgIAAxkBAAICPGaableO81phH-wF-gls2jPt_51sAAKW3TEbmUTRSGte-u-XdFZyAQADAgADbQADNQQ',
   37: 'AgACAgIAAxkBAAICPWaableseSv4cGYf8ISQ2H1NPqnAAALQ4jEbMyrRSH0nqJF11toPAQADAgADeAADNQQ'

    }
card_videos = {
   38: 'BAACAgIAAxkBAAICS2aab0jcvKgKfGD6DpAnQXSr-5JwAALPTgACfnewSKDvBSMg9NcjNQQ',
   39: 'BAACAgIAAxkBAAICSmaab0j_hEL8hJNLXc25yI_LZ0x2AAJjRwACMv2YSKQOK8Zqf_jVNQQ',
   40: 'BAACAgIAAxkBAAICTGaab0iZ_vUBLD1y-QABlvWQdGKzsAAC2U4AAn53sEgryh02JSxQvjUE',
   41: 'BAACAgIAAxkBAAICTWaab0ij_XNdhvhrbqFQzWb6ca8YAALdTgACfnewSMquSGgqmptANQQ',
   42: 'BAACAgIAAxkBAAICTmaab0htQmY_dg8LkDmdyt4oq1-vAALjTgACfnewSFJRteQK33x-NQQ',
   43: 'BAACAgIAAxkBAAICT2aab0gG9IDq5fwiUbeuFToWC7YGAALlTgACfnewSJoe4vfdiOPUNQQ',
   44: 'BAACAgIAAxkBAAICUGaab0jEmJCem4uZWW8Xb0YzxajLAAIsTwACmUTRSKT0bH9T7rleNQQ'
    }


card_texts = {
    1: "Коки Фурихата \n Статы:  \n Дриблинг:c \n Бросок :c \n Физ.':c \n Везучесть: b+ \n Пас:b+ \n Данк:нету \n Ум(IQ):c+ \n Скрытая способность: Нету",
    2: "Хироши Фукуда \n Статы:  \n Дриблинг:b \n Бросок :c- \n Физ.':c \n Везучесть: s+ \n Пас:c \n Данк:нету \n Ум(IQ):b+ \n Скрытая способность: Нету ",
    3: "Коичи Кавахара \n Статы:  \n Дриблинг:c \n Бросок :c \n Физ.':b \n Везучесть: a \n Пас:b\n Данк:нету \n Ум(IQ):c \n Скрытая способность: Нету ",
    4: "Шинске Кимура \n Статы:  \n Дриблинг:b \n Бросок :c- \n Физ.':a \n Везучесть: b \n Пас:c \n Данк:b \n Ум(IQ):b+ \n Скрытая способность: Нету ",
    5: "Киёши Мияджи \n Статы:  \n Дриблинг:b \n Бросок :b \n Физ.':c \n Везучесть: s+ \n Пас:b \n Данк:нету \n Ум(IQ):b+ \n Скрытая способность: Нету ",
    6: "Тайске Оцубо \n Статы:  \n Дриблинг:b \n Бросок :c- \n Физ.':bb \n Везучесть: s+ \n Пас:c \n Данк:нету \n Ум(IQ):c \n Скрытая способность: Нету",
    7: "Лю Вэй \n Статы: \n Дриблинг:b  \n Бросок :b \n Физ.':a \n Везучесть: ss+ \n Пас:a-- \n Данк:b+ \n Ум(IQ):b+ \n Скрытая способность: Нету",
    8: "Кенъичи Окамура \n Статы:  \n Дриблинг:a- \n Бросок :bb \n Физ.':b+ \n Везучесть:s \n Пас:b \n Данк:b++ \n Ум(IQ):c \n Скрытая способность Нету :",
    9: "Кенске Фукуи \n Статы:  \n Дриблинг:b \n Бросок:b \n Физ.':b \n Везучесть: s \n Пас:b \n Данк:c \n Ум(IQ):a \n Скрытая способность: Нету",
    10: "Рё Сакурай \n Статы:  \n Дриблинг:b \n Бросок:a \n Физ.':b \n Везучесть: s \n Пас:b \n Данк:c \n Ум(IQ):b \n Скрытая способность: Нету",
    11: "Коске Вакамацу \n Статы:  \n Дриблинг:a \n Бросок:b \n Физ.':b \n Везучесть: s \n Пас:b \n Данк:b \n Ум(IQ):b \n Скрытая способность: Нету",
    12: "Сатоши Цучида \n Статы:  \n Дриблинг:b \n Бросок :b \n Физ.':a- \n Везучесть: s+ \n Пас:d+ \n Данк:b \n Ум(IQ):a \n Скрытая способность: Нету",
    13: "Шого Хайзаки \n Статы:  \n Дриблинг:b+ \n Бросок:a \n Физ.':b+ \n Везучесть: s \n Пас:b \n Данк:b \n Ум(IQ):a- \n Скрытая способность: \n Копирование",
    14: "Тацуя Химуро \n Статы: \n Дриблинг:a- \n Бросок:a \n Физ.':a- \n Везучесть: s \n Пас:b \n Данк:b \n Ум(IQ):a \n Скрытая способность: Нету",
    15: "Юкио Касамацу \n Статы: \n Дриблинг:a- \n Бросок:b+ \n Физ.':a- \n Везучесть: s \n Пас:a \n Данк:a \n Ум(IQ):b \n Скрытая способность: Нету",
    16: "Мицухиро Хаякава \n Статы:  \n Дриблинг:b+ \n Бросок:a- \n Физ.':a+ \n Везучесть: s \n Пас:a \n Данк:b \n Ум(IQ):b \n Скрытая способность: Нету",
    17: "👑Теппей арикшн👑 \n Статы: \n Дриблинг:a+ \n Бросок :ss \n Физ.':a+ \n Везучесть:s \n Пас:ss+ \n Ум(IQ):s+ \n Скрытая способность: \n 🦾руки-крюки🦾",
    18: "☠Макото Тьома☠ \n Статы:  \n Дриблинг:a+ \n Бросок :a+ \n Физ.':s+ \n Везучесть: ss+ \n Пас:s+ \n Данк:хз \n Ум(IQ):x+ \n Скрытая способность:  \n 🕸паутина🕸",
    19: "🦶 Пятка Небуя 🦶 \n Статы:  \n Дриблинг:s+ \n Бросок :s- \n Физ.':x \n Везучесть: a+ \n Пас:a+ \n Ум(IQ):c \n Данк:s+ \n Скрытая способность:  \n 💪Жоские мыштсы💪",
    20: "🐒Рео бибизянчик🐒 \n Статы:  \n Дриблинг:a- \n Бросок :x \n Физ.':s \n Везучесть: s \n Пас:s+ \n Данк:нет \n Ум(IQ):a- \n Скрытая способность: \n 🌤Небеса🌤 \n 🌏земля🌏 \n 🌌пустата🌌",
    21: "⚡️Флейзер Хаяма⚡️ \n Статы:  \n Дриблинг:x \n Бросок :a+ \n Физ.':s \n Везучесть: s+ \n Пас:s+ \n Данк:хз \n Ум(IQ):a \n Скрытая способность:  \n ⚡️Молниеносный дриблинг⚡️",
    22: "Шинджи Коганеи  \n Статы:  \n Дриблинг:b+ \n Бросок :b \n Физ.':A++ \n Везучесть: s+ \n Пас:b+ \n Данк:хз \n Ум(IQ):a \n Скрытая способность: Универсальный игрок",
    23: "Ринноске Митобе \n Статы:  \n Дриблинг:b+ \n Бросок :a \n Физ.':b \n Везучесть: s+ \n Пас:a- \n Данк:хз \n Ум(IQ):a \n Скрытая способность: \n Бросок-крюк \n Защита-давлением",
    24: "Шун Изуки \n Статы:  \n Дриблинг:b \n Бросок :b \n Физ.':b \n Везучесть: s+ \n Пас:a \n Данк:хз \n Ум(IQ):a \n Скрытая способность: \n Орлиный глаз ",
    25: "Джумпей Хьюга \n Статы:  \n Дриблинг:b+ \n Бросок :a \n Физ.':b \n Везучесть: s+ \n Пас:a- \n Данк:нету \n Ум(IQ):s+ \n Скрытая способность: \n Форма броска 'Земля'(спиздел у бебезянчека) \n Неприкосновенный бросок \n Дальние броски ",
    26: "Читор аумене \n Статы:  \n Дриблинг:xxx+ \n Бросок :sx \n Физ.':ss+ \n Данк:s+ \n Везучесть:s+ \n Пас:нетуXD😜 \n Ум(IQ):c+ \n Скрытая способность:😈жёсткий дриблинг😈",
    27: "Мурасакибара пенокио🇰🇬 \n Статы:  \n Дриблинг:s \n Бросок :s \n Физ.':sxx+ \n Везучесть: a+ \n Пас:d+ \n Ум(IQ):d+ \n Данк:sss+ \n Скрытая способность: ⚡️молниеносная реакция⚡️",
    28: "🔫Медарима папагета🔫 \n Статы:  \n Дриблинг:s- \n Бросок :sxx+ \n Физ.:ss- \n Данк: нету \n Везучесть:ss \n Пас:a- \n Ум(IQ):a \n Скрытая способность:🍃100% бросок🍃",
    29: "🥵Акаши лол🥵 \n Статы:  \n Дриблинг:sxx+ \n Бросок :s \n Физ.':ss \n Данк: a+ \n Везучесть:a- \n Пас:s+ \n Ум(IQ):ss+ \n Скрытая способность: 🌹глаз  императора🌹",
    30: "✨Кисэ лева✨ \n Статы:  \n Дриблинг:ss \n Бросок :ss \n Физ.':ss- \n Везучесть:s \n Пас:s+ \n Ум(IQ):a+ \n Скрытая способность: ✨копирование✨",
    31: "❄️Ессыр куроко❄️ \n Статы:  \n Дриблинг:c \n Бросок:a- \n Физ.':d+ \n Данк:нету \n Везучесть:ss \n Пас:xxx \n Ум(IQ):c+ \n Скрытая способность: 💨призрачный  игрок💨",
    32: "🌇Перепепепекагами🌇 \n Статы:  \n Дриблинг:sx \n Бросок :a+ \n Физ.':s++ \n Везучесть: s+ \n Пас:s \n Данк:sx \n Ум(IQ):b \n Скрытая способность: \n 🦵Супер прыжок🦵",
    33: "Нэш Голд-младший \n Статы:  \n Дриблинг:ss+ \n Бросок :ss+ \n Физ.':ss+ \n Везучесть: ss+ \n Пас:ss+ \n Данк:ss+ \n Ум(IQ):ss+ \n Скрытая способность: Маскировка движений \n Глаза Дьявола \n Максимально выверенные движения \n Превосходные баскетбольные навыки",
    34: "Джейсон Сильвер \n Статы:  \n Дриблинг:ss+ \n Бросок :ss+ \n Физ.':ss+ \n Везучесть: ss+ \n Пас:ss+ \n Данк:ss+ \n Ум(IQ):a \n Скрытая способность: Животные инстинкты",
    35: "Ник \n Статы:  \n Дриблинг:X+ \n Бросок :ss+ \n Физ.':ss+ \n Везучесть: ss+ \n Пас:ss+ \n Данк:ss+ \n Ум(IQ):ss+ \n Скрытая способность: Нету",
    36: "Аллен \n Статы:  \n Дриблинг:ss+ \n Бросок :ss+ \n Физ.':ss+ \n Везучесть: ss+ \n Пас:ss+ \n Данк:ss+ \n Ум(IQ):ss+ \n Скрытая способность: Неприкосновенный бросок",
    37: "Зак \n Статы:  \n Дриблинг:ss+ \n Бросок :ss+ \n Физ.':x+ \n Везучесть: ss+ \n Пас:ss+ \n Данк:ss+ \n Ум(IQ):ss+ \n Скрытая способность: Дьявольская выносливость ",
    38: "🥵Акаши лол🥵 \n Статы:  \n Дриблинг:sxx+ \n Бросок :ss+ \n Физ.':ssa+ \n Данк: aa+ \n Везучесть:s- \n Пас:ss+ \n Ум(IQ):ssx \n Скрытая способность: 🌹глаз  императора🌹 \n в потоке: 😈но калене😈",
    39: "🔫Медарима папагета🔫 \n Статы:  \n Дриблинг:ss+ \n Бросок :xxx+ \n Физ.':sss- \n Данк: нету \n Везучесть:ss \n Пас:s+ \n Ум(IQ):s \n Скрытая способность:🍃100% бросок🍃 \n В потоке: 🌪быстрый бросок🌪",
    40: "💤Читор аумене💤 \n Статы: \n Дриблинг:xxx+ \n Бросок :sx \n Физ.':sx+ \n Данк:x+ \n Везучесть:s+ \n Пас:нетуXD😜 \n Ум(IQ):a+ \n Скрытая способность:😈жёсткий дриблинг😈 \n  в потоке: дриблинг усиливается в два раза",
    41: "✨Кисэ лева✨ \n Статы:  \n Дриблинг:ssa+ \n Бросок :ssa+ \n Физ.':ss+ \n Везучесть:s \n Пас:ss+ \n Ум(IQ):s \n Скрытая способность: \n ✨копирование✨ \n в патоке:💫абсолютное копирование💫",
    42: "❄️Ессыр куроко❄️  \n Статы:  \n Дриблинг:a \n Бросок:s- \n Физ.':a- \n Данк:нету \n Везучесть:ss+ \n Пас:xxx+ \n Ум(IQ):s+ \n Скрытая способность:💨призрачный  игрок💨 \n в потоке: 🫥Абсолютная невидимость🫥",
    43: "Мурасакибара пенокио🇰🇬  \n Статы:  \n Дриблинг:s+ \n Бросок :ss \n Физ.':xxx+ \n Везучесть: a+ \n Пас:d+ \n Данк:ssx+ \n Ум(IQ):a \n Скрытая способность: ⚡️молниеносная реакция⚡️ \n в потоке: скрытая способность усиливается в два раза",
    44: "🌇Перепепепекагами🌇 \n Статы:  \n Дриблинг:x+ \n Бросок :a++ \n Физ.':x \n Везучесть: ss \n Пас:s+ \n Данк:x+ \n Ум(IQ):a \n Скрытая способность: Супер прыжок \n В потоке: ☄ метеоритный данк☄",

}

START_IMAGE_FILE_ID = "AgACAgIAAxkBAAIIWmaiyreMQgxWEhX3TAUG0cpIsk5cAAJA4TEbPzehSO1QkhnygGBwAQADAgADeQADNQQ"


user_data = {}
number_data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,44]


# Хранение данных пользователей
user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id in user_data:
        bot.send_message(message.chat.id, "Вы уже заполнили свой профиль, если хотите редактировать его, то напишите 'Изменить профиль'")
    else:
        markup = types.InlineKeyboardMarkup()
        reg_button = types.InlineKeyboardButton("Прайде регестрацию", callback_data="register")
        markup.add(reg_button)
        bot.send_photo(message.chat.id, START_IMAGE_FILE_ID, caption="Мы абсолюты", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == "register")
def handle_register(call):
    user_id = call.from_user.id
    if user_id in user_data:
        bot.send_message(call.message.chat.id, "Вы уже заполнили свой профиль, если хотите редактировать его, то напишите 'Изменить профиль'")
    else:
        bot.send_message(call.message.chat.id, "Напеши свай ник")
        bot.register_next_step_handler(call.message, get_nickname)

def get_nickname(message):
    user_id = message.from_user.id
    user_data[user_id] = {'nickname': message.text}
    bot.send_message(message.chat.id, "Тепер прешли фото, катарое хочеш уведеть у сипя на аве")
    bot.register_next_step_handler(message, get_photo)

def get_photo(message):
    user_id = message.from_user.id
    if message.content_type == 'photo':
        user_data[user_id]['photo'] = message.photo[-1].file_id
        markup = types.InlineKeyboardMarkup()
        card_button = types.InlineKeyboardButton("Получить карту", callback_data="get_card")
        markup.add(card_button)
        bot.send_message(message.chat.id, "Регестрация завершено", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "пришли фото ипасос")
        bot.register_next_step_handler(message, get_photo)

@bot.message_handler(func=lambda message: message.text.lower() == 'мой профиль')
def show_profile(message):
    user_id = message.from_user.id
    if user_id in user_data:
        nickname = user_data[user_id]['nickname']
        photo_id = user_data[user_id].get('photo')
        profile_text = f"ник: *{nickname}*"
        if photo_id:
            bot.send_photo(message.chat.id, photo_id, caption=profile_text, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, profile_text)
    else:
        bot.send_message(message.chat.id, "Сначала прайдэ регестрацию талпайоп")

@bot.message_handler(func=lambda message: message.text.lower() == 'изменить профиль')
def change_profile(message):
    user_id = message.from_user.id
    if user_id in user_data:
        bot.send_message(message.chat.id, "Напеше свай ник")
        bot.register_next_step_handler(message, update_nickname)
    else:
        bot.send_message(message.chat.id, "Сначала пройдите регистрацию.")

def update_nickname(message):
    user_id = message.from_user.id
    user_data[user_id]['nickname'] = message.text
    bot.send_message(message.chat.id, "Тепер прешли фото, катарое хочеш уведеть у сипя на аве")
    bot.register_next_step_handler(message, update_photo)

def update_photo(message):
    user_id = message.from_user.id
    if message.content_type == 'photo':
        user_data[user_id]['photo'] = message.photo[-1].file_id
        bot.send_message(message.chat.id, "Профель обновлен")
    else:
        bot.send_message(message.chat.id, "пришли фото ипасос")
        bot.register_next_step_handler(message, update_photo)

@bot.message_handler(func=lambda message: message.text.lower() == 'меню')
def show_menu(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Сначала пройдите регистрацию.")
        return

    profile_data = user_data[user_id]
    nickname = profile_data['nickname']
    photo_id = profile_data.get('photo')

    profile_text = f"Ник: *{nickname}*\nВселенная: поколение чурок"

    if photo_id:
        bot.send_photo(message.chat.id, photo_id, caption=profile_text, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, profile_text)

@bot.message_handler(func=lambda message: message.text.startswith('+ник '))
def change_nickname(message):
    user_id = message.from_user.id
    new_nickname = message.text.split('+ник ', 1)[1].strip()

    if user_id in user_data:
        user_data[user_id]['nickname'] = new_nickname
        bot.send_message(message.chat.id, f"твай ник  изменон на '*{new_nickname}*'")
    else:
        bot.send_message(message.chat.id, "Сначала пройдите регистрацию.")



def get_photo(message):
    user_id = message.from_user.id
    if message.content_type == 'photo':
        user_data[user_id]['photo'] = message.photo[-1].file_id
        markup = types.InlineKeyboardMarkup()
        card_button = types.InlineKeyboardButton("Получить карту", callback_data="get_card")
        markup.add(card_button)
        bot.send_message(message.chat.id, "Регестрация завершено", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "пришли фото ипасос")
        bot.register_next_step_handler(message, get_photo)








# Новый словарь для эдитов (замените VIDEO_FILE_ID_X на реальные file_id)
edit_videos = [
    "BAACAgIAAxkBAAIH3Gaii81achJZtSKkTZHL6VEAAXf4BgACx00AAkx6EEnITEFR_WpKnjUE",
    "BAACAgIAAxkBAAIH22aii8245z7Z0lgF5ggogcIL3rPIAALGTQACTHoQSRDPpdWzS6t2NQQ",
    "BAACAgIAAxkBAAIH3Waii838MAIzjVPRb0O7Ch4Z4-avAALJTQACTHoQSa7qCPJMQF3xNQQ",
    "BAACAgIAAxkBAAIH3maii80Jy7l79aUq_t7PZb2DFVB9AALKTQACTHoQSdVQzC9ikSb1NQQ",
    "BAACAgIAAxkBAAIH32aii82RURqFEfiNIsbK1EQpBXR2AALMTQACTHoQSQICe1B2dn_oNQQ",
    "BAACAgIAAxkBAAIH4Gaii82XoIhyC4_FBpTagPJbVsH-AALPTQACTHoQSfdTGgHe4AhANQQ",
    "BAACAgIAAxkBAAIH4Waii829Ps0KZ-7Al75saDpcMNjOAALQTQACTHoQSWWXFnv3f03fNQQ",
    "BAACAgIAAxkBAAIH4maii80qhhHDlMAeEGgAAbWuL8NKmQAC0U0AAkx6EElMfq64NkvPtjUE",
    "BAACAgIAAxkBAAIH42aii81FKwEKpdcla7z-1FJt0f30AALTTQACTHoQScxWaGtkMCWRNQQ",
    "BAACAgIAAxkBAAIH5Gaii80uPWIIj1sDsN727BcvocOvAALUTQACTHoQSaOx5dImdBj0NQQ",
    "BAACAgIAAxkBAAIH5Waii82iguw6uDiKyGupHBOnKMKoAALVTQACTHoQSa7H9IskLEybNQQ",
    "BAACAgIAAxkBAAIH5maii81UmlhxxQS7um7h722D2XlTAALYTQACTHoQSVv6V72NN8_ONQQ",
    "BAACAgIAAxkBAAIH52aii82rUO0LdNMnIS0kNejc_YkfAALZTQACTHoQSVDV3cL8AAFQxDUE",
    "BAACAgIAAxkBAAIH6Gaii82PhUMp6PlxdhpS8YOa8fbYAALbTQACTHoQSS8iFyBJWNj_NQQ",
    "BAACAgIAAxkBAAIH6Waii81lWQ8xXAh0R0FCQyVQ2-UEAALcTQACTHoQSfh3d0HgarVGNQQ",
    "BAACAgIAAxkBAAIH6maii81mAXzGLuILU-hRCZiYjoh1AALfTQACTHoQSeHBcZ_sZNKCNQQ",
    "BAACAgIAAxkBAAIH62aii82c7681nDmZZHZvdUnsiyNaAALgTQACTHoQST-ADmaZAAFFGzUE",
    "BAACAgIAAxkBAAIH7Gaii819pVHS18SC0301m45bQqeVAALiTQACTHoQSSd0qi8I_kIDNQQ",
    "BAACAgIAAxkBAAIH7Waii81gbvZ_lvN8zfKBrgunJ7Q-AALlTQACTHoQSbA_mzSooZRpNQQ",
    "BAACAgIAAxkBAAIH7maii82qauZoVz5gopmujd6SkGcwAAIOUQACTHoQSeWFJBTT_Uk8NQQ",
    "BAACAgIAAxkBAAIH72aii81y2sG6YJ1q-HRV_e_2SRdhAAIPUQACTHoQSW_WsKHDmAeHNQQ",
    "BAACAgIAAxkBAAIH8Gaii80hPB9dcXgaK5tPas5vbSYoAAIQUQACTHoQSSyuVXAPWiC6NQQ",
    "BAACAgIAAxkBAAIH8Waii83k6BtoRQEu2bCd0dyVKH_mAAIRUQACTHoQSYRV7dnVsH75NQQ",
    "BAACAgIAAxkBAAIH8maii80anljd58vmvE4VPqHB9Dt3AAISUQACTHoQSQOOs8htidihNQQ",
    "BAACAgIAAxkBAAIH82aii81cONOQG0WBVHsn91HijhayAAITUQACTHoQSVk-OwI_wSfPNQQ",
    "BAACAgIAAxkBAAIH9Gaii80t1LUu-mFe7387CboCKJTiAAIVUQACTHoQSbBZ9WaDuFfgNQQ",
    "BAACAgIAAxkBAAIH9Waii80B0f4yAvv7RqbCmJG6UjzgAAIWUQACTHoQSTf-xm5SGYaaNQQ",
    "BAACAgIAAxkBAAIH9maii82am_H5uiYBaDpxp7364khgAAIXUQACTHoQScOKDOYtqfUPNQQ",
    "BAACAgIAAxkBAAIH92aii82AzRWllz4AARefZZYhrtKvvgACGFEAAkx6EEl0gm-vrmvktTUE",
    "BAACAgIAAxkBAAIH-Gaii81tUVhbo2w5FJjH1SacNMTqAAIaUQACTHoQSWsqQ-R0NdyuNQQ",
    "BAACAgIAAxkBAAIH-Waii81givvszOpxqZmnHSAxTzauAAIbUQACTHoQSaeiFPODa1UhNQQ",
    "BAACAgIAAxkBAAIH-maii81InnEXke1SNkbDo4t2ZqJyAAIfUQACTHoQSX0yfYTqQY04NQQ",
    "BAACAgIAAxkBAAIH-2aii82TgLkpGYXtPAVJRDXh2eZkAAIjUQACTHoQSbIUvtQdNwIzNQQ",
    "BAACAgIAAxkBAAIH_Gaii80dM0MChJhLileq8ILuiSOSAAIkUQACTHoQSbnr5Ew568l_NQQ",
    "BAACAgIAAxkBAAIH_Waii80POn63eFLpxJFl5DhlTizUAAIlUQACTHoQSb1w7bz-G5A3NQQ",
    "BAACAgIAAxkBAAIH_maii82PPWN8-z_RKNkH0jBK-pgFAAJ5UQACTHoQSUqk4IETtsdTNQQ",
    "BAACAgIAAxkBAAIH_2aii808vCKgYTl9mWiqSi3BxQsBAAJ7UQACTHoQSRIM-6SjiDYBNQQ",
    "BAACAgIAAxkBAAIIAAFmoovNaTSU-f1ABa0klZFEh7eMiwACfFEAAkx6EEnCn7Id4XK6qjUE",
    "BAACAgIAAxkBAAIIAWaii82eBTKJxrAi1fxMS1YL5FukAAJ-UQACTHoQSaLJncGDTlEMNQQ",
    "BAACAgIAAxkBAAIIAmaii83PGyO9jCcIwAq8z1gpizeVAAJ_UQACTHoQSQTf0WTgXsPENQQ",
    "BAACAgIAAxkBAAIIA2aii83L9CDrfqDuuvsxwjr4zzUZAAKBUQACTHoQSSkvPeoEXUz-NQQ",
    "BAACAgIAAxkBAAIIBGaii81MwFbvhDVG6XnAQ_QVMrf2AAKCUQACTHoQSVTpEch6jyk3NQQ",
    "BAACAgIAAxkBAAIIBWaii80YwisyzhRiw0UprgsN5G3uAAKDUQACTHoQSTVyN8oWm4UtNQQ",
    "BAACAgIAAxkBAAIIBmaii81daatFKKgAAXzsczzqu4Pk5QAChlEAAkx6EElN2EDbkndT8zUE",
    "BAACAgIAAxkBAAIIB2aii82fmpIAAaDj83LwTgygS4pHCgACh1EAAkx6EEk195AM3dfyqjUE",
    "BAACAgIAAxkBAAIICGaii800Ao5vCF3WG8Mg23-z1R_cAAKJUQACTHoQST2RfkNhNi_7NQQ",
    "BAACAgIAAxkBAAIICWaii80SORB2d13oKoiHhGyWkFc4AAKMUQACTHoQSR2HIEXX3xiPNQQ",
    "BAACAgIAAxkBAAIICmaii82N2WmHMENkL25w2UUxm5HvAAKNUQACTHoQScM3tB12av-INQQ",
    "BAACAgIAAxkBAAIIC2aii80BjY2-45RyBCEZPYr73BLzAAKOUQACTHoQSdrt-LovlZT2NQQ",
    "BAACAgIAAxkBAAIIDGaii80i87xT5gbnP_2C_P-BSrsGAAKRUQACTHoQSQfrHX8g3wGONQQ",
    "BAACAgIAAxkBAAIIDWaii80d-XlneJhsMDluwl830iNAAAKVUQACTHoQSXh8fiBGA60PNQQ",
    "BAACAgIAAxkBAAIIDmaii80yRBYVT1zyEP3OqD9kTMS9AAKXUQACTHoQSeC9gYCyEucSNQQ",
    "BAACAgIAAxkBAAIID2aii80yBzOcMO2SdCsLLMfoDY_tAAKiUQACTHoQSUzHz4OIfWnhNQQ",
    "BAACAgIAAxkBAAIIEGaii82_qfL-BizP73U7s_yny6jwAAKkUQACTHoQSagbBhtxW_mxNQQ",
    "BAACAgIAAxkBAAIIR2aijAasV7Sr_G3wXSemFuspaGJcAAK-VwACWTjJSPVM3UXuxd0GNQQ",
    "BAACAgIAAxkBAAIISWaijD-5aiHoRmadvfdZtVQjy51iAAKcYAACPzeZSIPWuVaVCAxDNQQ",
    "BAACAgIAAxkBAAIIS2aijJrEcq1ykbtT3j6Cag7bB1bCAAJjUwACxfqQSMOL_enKTlp-NQQ",
    "BAACAgIAAxkBAAIITWaijQjdDlqxaLzc1l8kE2reGsUHAAIyWgACikAZSYradfhcNQTBNQQ"
    "BAACAgIAAxkBAAIIbWai1Xtf7eQi6WMFPv31wBp-a4oJAALjTQACM3YYScXyEePoYYy0NQQ"
    "BAACAgIAAxkBAAIIbmai1XtjBfp3o7bUfEZVhfTtzilqAAIDTgACM3YYSZaEUDyitktnNQQ"
  ]


@bot.message_handler(func=lambda message: message.text.lower() == "эдит")
def send_random_edit(message):
    random_video = random.choice(edit_videos)  # Выбор случайного видео
    bot.send_video(message.chat.id, random_video, caption="Рандамний эдит")




"""

# Определяем веса для каждой группы
weights = [
    (1, 6, 10),  # Числа от 1 до 6, 10 раз
    (7, 11, 5),  # Числа от 7 до 11, 5 раз
    (12, 16, 3),  # Числа от 12 до 16, 3 раза
    (17, 25, 2),  # Числа от 17 до 25, 2 раза
    (26, 37, 1),  # Числа от 26 до 37, 1 раз
    (38, 44, 0.5)  # Числа от 38 до 44, 0.5 раза
]

# Генерация карт с учетом весов
weighted_numbers = []
for start, end, count in weights:
    for num in range(start, end + 1):
        weighted_numbers.extend([num] * int(count * 10))

# Уникальные числовые значения с учетом весов
unique_weighted_numbers = list(set(weighted_numbers))

# Хранение полученных карт пользователей
user_received_cards = {}
user_last_draw_time = {}  # Время последнего получения карт
user_cards_indices = {}  # Индексы карт для пользователей
msg_id_storage = {}  # Хранение идентификаторов сообщений

# Определение уровней
level_ranges = {
    "level_1_6": (1, 6),
    "level_7_11": (7, 11),
    "level_12_16": (12, 16),
    "level_17_25": (17, 25),
    "level_26_37": (26, 37),
    "level_38_44": (38, 44),
}


@bot.message_handler(func=lambda message: message.text.lower() == "мои карты")
def choose_numbers(message):
    markup = types.InlineKeyboardMarkup()  # Создаем кнопки для каждого уровня сложности
    difficulty_buttons = [
        ("🟤хуйня🟤", "level_1_6"),
        ("⚪️обычный⚪️", "level_7_11"),
        ("🟢редки🟢", "level_12_16"),
        ("🟠мифически🟠", "level_17_25"),
        ("🟡легендарный🟡", "level_26_37"),
        ("🟣божественный🟣", "level_38_44"),
        ("Все карты", "all_cards")  # Добавляем кнопку "Все карты"
    ]

    user_id = message.from_user.id
    for label, level_key in difficulty_buttons:
        button = types.InlineKeyboardButton(label, callback_data=level_key)
        markup.add(button)

    bot.send_message(message.chat.id, "Выберите уровень сложности:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in level_ranges)
def handle_level_selection(call):
    user_id = call.from_user.id
    level = level_ranges[call.data]

    # Инициализация данных пользователя, если они еще не существуют
    if user_id not in user_received_cards:
        user_received_cards[user_id] = []  # Инициализируем, если еще не было полученных карт

    if user_id not in user_cards_indices:
        user_cards_indices[user_id] = {}

    # Если пользователь выбирает новый уровень, сбрасываем индекс
    if call.data not in user_cards_indices[user_id]:
        user_cards_indices[user_id][call.data] = 0

    current_index = user_cards_indices[user_id][call.data]

    # Получаем числа в зависимости от выбранного уровня
    numbers = [num for num in unique_weighted_numbers if level[0] <= num <= level[1]]

    # Доступные карты, которые пользователь собрал
    available_cards = [num for num in numbers if num in user_received_cards[user_id]]

    if current_index < len(available_cards):
        num = available_cards[current_index]
        user_cards_indices[user_id][call.data] += 1  # Увеличиваем индекс для следующего запроса

        image_id = card_images.get(num)
        video_id = card_videos.get(num)

        if image_id:
            card_text = card_texts.get(num, f"Карта: {num}")
            media = types.InputMediaPhoto(image_id, caption=card_text)
        elif video_id:
            card_text = card_texts.get(num, f"Карта: {num}")
            media = types.InputMediaVideo(video_id, caption=card_text)
        else:
            bot.send_message(call.message.chat.id, "Картинка или видео не найдены.")
            return

        # Отправляем сообщение с текущей картой и кнопкой "Дальше"
        markup = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("Дальше", callback_data=call.data)
        )

        if current_index == 0:  # Если это первая карта, создаем новое сообщение
            msg = bot.send_media_group(call.message.chat.id, [media])[0]
            msg_id = msg_id_storage.get(user_id)
            if msg_id:
                bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=msg_id)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg_id, reply_markup=markup)
            else:
                bot.send_message(call.message.chat.id, "ха лашара у тебя закончелес карты или ищо нету таких карт")

            @bot.callback_query_handler(func=lambda call: call.data == "all_cards")
            def handle_all_cards(call):
                user_id = call.from_user.id
                total_cards = 44  # Общее количество карт
                collected_cards = len(user_received_cards.get(user_id, []))  # Количество собранных карт
                bot.send_message(call.message.chat.id,
                                 f"Общие каличиства сабранных карт: {collected_cards}/{total_cards}")

            @bot.message_handler(func=lambda message: message.text.lower() == "получить карту")
            def get_card_manual(message):
                user_id = message.from_user.id
                # Инициализация данных пользователя, если еще не было
                if user_id not in user_received_cards:
                    user_received_cards[user_id] = []  # Инициализируем, если еще не было полученных карт
                user_last_draw_time[user_id] = int(time.time())  # Инициализируем время

                # Проверяем, сколько карт уже получено
                if len(user_received_cards[user_id]) < 2:
                    # Выбор одной случайной карты
                    card_number = random.choice(weighted_numbers)  # Выбираем одну карту
                    user_received_cards[user_id].append(card_number)  # Добавляем карту в список полученных
                    user_last_draw_time[user_id] = int(time.time())  # Обновляем время получения карты

                    # Отправляем карту пользователю
                    if card_number in card_images:
                        card_text = card_texts.get(card_number, f"Ваша карта: {card_number}")
                        bot.send_photo(message.chat.id, card_images[card_number], caption=card_text)
                    elif card_number in card_videos:
                        card_text = card_texts.get(card_number, f"Ваша карта: {card_number}")
                        bot.send_video(message.chat.id, card_videos[card_number], caption=card_text)
                    else:
                        bot.send_message(message.chat.id, f"Ваша карта: {card_number}")
                else:
                    # Проверяем, прошло ли 1 час с последнего получения
                    current_time = int(time.time())
                    elapsed_time = current_time - user_last_draw_time[user_id]
                    if elapsed_time >= 3600:  # 3600 секунд = 1 час (время ожидания)
                        bot.send_message(message.chat.id,
                                         "Вы можете получить новые карты. Используйте команду 'получить карту' снова.")
                    else:
                        remaining_time = 3600 - elapsed_time
                        minutes = remaining_time // 60
                        seconds = remaining_time % 60
                        bot.send_message(message.chat.id,
                                         f"Вернес через {minutes} менут и {seconds} сикунт, чтабы палучит навые карты")
"""
"""
# Определяем веса для каждой группы
weights = [
    (1, 6, 10),
    (7, 11, 5),
    (12, 16, 3),
    (17, 25, 2),
    (26, 37, 1),
    (38, 44, 0.5)
]

# Генерация уникальных номеров карт с учетом весов
weighted_numbers = []
for start, end, count in weights:
    for num in range(start, end + 1):
        weighted_numbers.extend([num] * int(count * 10))

# Уникальные числовые значения с учетом весов
unique_weighted_numbers = list(set(weighted_numbers))
random.shuffle(unique_weighted_numbers)  # Перемешивание для случайного порядка

# Хранение полученных карт и состояния пользователей
user_received_cards = {}
user_last_draw_time = {}
user_cards_indices = {}

# Время ожидания между получениями карт (в секундах)
TIME_LIMIT = 3600  # 1 час
CARDS_PER_HOUR = 2

@bot.message_handler(func=lambda message: message.text.lower() == "получить карту")
def get_card(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id not in user_last_draw_time:
        user_last_draw_time[user_id] = 0
        user_received_cards[user_id] = []

    # Проверяем, сколько карт пользователь уже получил за последний час
    time_since_last_draw = current_time - user_last_draw_time[user_id]
    if len(user_received_cards[user_id]) >= CARDS_PER_HOUR and time_since_last_draw < TIME_LIMIT:
        remaining_time = TIME_LIMIT - time_since_last_draw
        minutes, seconds = divmod(remaining_time, 60)
        bot.send_message(message.chat.id, f"Вернись через {int(minutes)} минут и {int(seconds)} секунд, чтобы получить новые карточки.")
        return

    # Генерация номера карточки
    chosen_card_idx = random.choice(unique_weighted_numbers)

    # Проверяем, что карточка есть в словарях
    if chosen_card_idx in card_images:
        # Сохраняем полученную карту
        user_received_cards[user_id].append(chosen_card_idx)
        user_last_draw_time[user_id] = current_time

        # Отправляем картинку
        bot.send_photo(message.chat.id, card_images[chosen_card_idx], caption=card_texts[chosen_card_idx])
    elif chosen_card_idx in card_videos:
        # Сохраняем полученную карту
        user_received_cards[user_id].append(chosen_card_idx)
        user_last_draw_time[user_id] = current_time

        # Отправляем видео
        bot.send_video(message.chat.id, card_videos[chosen_card_idx], caption=card_texts.get(chosen_card_idx, ""))
    else:
        bot.send_message(message.chat.id, "Не удалось получить карточку. Попробуйте еще раз.")

@bot.message_handler(func=lambda message: message.text.lower() == "мои карты")
def choose_numbers(message):
    markup = types.InlineKeyboardMarkup()
    difficulty_buttons = [
        ("🟤хуйня🟤", "level_1_6"),
        ("⚪️обычный⚪️", "level_7_11"),
        ("🟢редки🟢", "level_12_16"),
        ("🟠мифически🟠", "level_17_25"),
        ("🟡легендарный🟡", "level_26_37"),
        ("🟣божественный🟣", "level_38_44"),
        ("Все карты", "all_cards")
    ]

    for label, level_key in difficulty_buttons:
        button = types.InlineKeyboardButton(label, callback_data=level_key)
        markup.add(button)

    bot.send_message(message.chat.id, "Выберите уровень сложности:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_card_level(call):
    user_id = call.from_user.id
    level_key = call.data
    level_ranges = {
        "level_1_6": (1, 6),
        "level_7_11": (7, 11),
        "level_12_16": (12, 16),
        "level_17_25": (17, 25),
        "level_26_37": (26, 37),
        "level_38_44": (38, 44),
    }

    if user_id not in user_cards_indices:
        user_cards_indices[user_id] = {k: 0 for k in level_ranges.keys()}

    if level_key in level_ranges:
        start, end = level_ranges[level_key]
        available_cards = [num for num in range(start, end + 1) if num in unique_weighted_numbers]

        # Получение текущего индекса карты для пользователя
        current_index = user_cards_indices[user_id][level_key]

        if current_index < len(available_cards):
            chosen_card_idx = available_cards[current_index]

            # Убедимся, что выбранная карточка существует в словарях
            if chosen_card_idx in card_images:
                # Редактируем сообщение с медиа и текстом
                bot.edit_message_media(
                    media=types.InputMediaPhoto(card_images[chosen_card_idx], caption=card_texts[chosen_card_idx]),
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id
                )
            elif chosen_card_idx in card_videos:
                # Редактируем сообщение с видео
                bot.edit_message_media(
                    media=types.InputMediaVideo(card_videos[chosen_card_idx], caption=card_texts.get(chosen_card_idx, "")),
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id
                )

            # Редактируем индекс для следующей карты
            user_cards_indices[user_id][level_key] += 1
        else:
            bot.send_message(call.message.chat.id, "Карты этого уровня закончены.")
            return  # Отмена, чтобы избежать ошибки дальнейшего редактирования

    # Кнопка "Дальше" для навигации
    next_button = types.InlineKeyboardButton("Дальше", callback_data=level_key)
    markup = types.InlineKeyboardMarkup()
    markup.add(next_button)
    bot.send_message(call.message.chat.id, "Нажмите 'Дальше', чтобы увидеть следующую карту", reply_markup=markup)
"""

# Определяем веса для каждой группы
weights = [
    (1, 6, 10),  # Числа от 1 до 6, 10 раз
    (7, 11, 5),  # Числа от 7 до 11, 5 раз
    (12, 16, 3),  # Числа от 12 до 16, 3 раза
    (17, 25, 2),  # Числа от 17 до 25, 2 раза
    (26, 37, 1),  # Числа от 26 до 37, 1 раз
    (38, 44, 0.5)  # Числа от 38 до 44, 0.5 раза
]

# Генерация карт с учетом весов
weighted_numbers = []
for start, end, count in weights:
    for num in range(start, end + 1):
        weighted_numbers.extend([num] * int(count * 10))

# Уникальные числовые значения с учетом весов
unique_weighted_numbers = list(set(weighted_numbers))

# Хранение полученных карт пользователей
user_received_cards = {}
user_last_draw_time = {}  # Время последнего получения карт
user_cards_indices = {}  # Индексы карт для пользователей
msg_id_storage = {}  # Хранение идентификаторов сообщений

# Определение уровней
level_ranges = {
    "level_1_6": (1, 6),
    "level_7_11": (7, 11),
    "level_12_16": (12, 16),
    "level_17_25": (17, 25),
    "level_26_37": (26, 37),
    "level_38_44": (38, 44),
}



@bot.message_handler(func=lambda message: message.text.lower() == "мои карты")
def choose_numbers(message):
    markup = types.InlineKeyboardMarkup()  # Создаем кнопки для каждого уровня сложности
    difficulty_buttons = [
        ("🟤хуйня🟤", "level_1_6"),
        ("⚪️обычный⚪️", "level_7_11"),
        ("🟢редки🟢", "level_12_16"),
        ("🟠мифически🟠", "level_17_25"),
        ("🟡легендарный🟡", "level_26_37"),
        ("🟣божественный🟣", "level_38_44"),
        ("Все карты", "all_cards")  # Добавляем кнопку "Все карты"
    ]
    user_id = message.from_user.id
    for label, level_key in difficulty_buttons:
        button = types.InlineKeyboardButton(label, callback_data=level_key)
        markup.add(button)
    bot.send_message(message.chat.id, "Выберите уровень сложности:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in level_ranges)
def handle_level_selection(call):
    user_id = call.from_user.id
    level = level_ranges[call.data]

    # Инициализация данных пользователя, если они еще не существуют
    if user_id not in user_received_cards:
        user_received_cards[user_id] = []
    if user_id not in user_cards_indices:
        user_cards_indices[user_id] = {}

    # Если пользователь выбирает новый уровень, сбрасываем индекс
    if call.data not in user_cards_indices[user_id]:
        user_cards_indices[user_id][call.data] = 0

    current_index = user_cards_indices[user_id][call.data]

    # Получаем числа в зависимости от выбранного уровня
    numbers = [num for num in unique_weighted_numbers if level[0] <= num <= level[1]]

    # Доступные карты, которые пользователь собрал
    available_cards = [num for num in numbers if num in user_received_cards[user_id]]

    if current_index < len(available_cards):  # Проверяем, есть ли доступные карты
        num = available_cards[current_index]
        user_cards_indices[user_id][call.data] += 1  # Увеличиваем индекс для следующего запроса

        image_id = card_images.get(num)
        video_id = card_videos.get(num)

        media = None  # Инициализируем переменную media
        if image_id:
            card_text = card_texts.get(num, f"Карта: {num}")
            media = types.InputMediaPhoto(image_id, caption=card_text)
        elif video_id:
            card_text = card_texts.get(num, f"Карта: {num}")
            media = types.InputMediaVideo(video_id, caption=card_text)

        if media:  # Проверяем, что media инициализирована
            # Отправляем сообщение с текущей картой и кнопкой "Дальше"
            markup = types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton("Дальше", callback_data=call.data)
            )

            if current_index == 0:  # Если это первая карта, создаем новое сообщение
                msg = bot.send_media_group(call.message.chat.id, [media])[0]
                msg_id_storage[user_id] = msg.message_id  # Сохраняем идентификатор сообщения
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg.message_id, reply_markup=markup)
            else:  # Если же карта не первая, обновляем существующее сообщение
                msg_id = msg_id_storage.get(user_id)
                bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=msg_id)
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg_id, reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, "Не удалось найти изображение или видео для данной карты.")
    else:
        bot.send_message(call.message.chat.id, "ха лашара у тебя закончелись карты или ещё нету таких карт.")

@bot.callback_query_handler(func=lambda call: call.data == "all_cards")
def handle_all_cards(call):
    user_id = call.from_user.id
    total_cards = 44  # Общее количество карт
    collected_cards = len(user_received_cards.get(user_id, []))  # Количество собранных карт
    bot.send_message(call.message.chat.id, f"Общие количества собранных карт: {collected_cards}/{total_cards}")

@bot.message_handler(func=lambda message: message.text.lower() == "получить карту")
def get_card_manual(message):
    user_id = message.from_user.id
    # Инициализация данных пользователя, если еще не было
    if user_id not in user_received_cards:
        user_received_cards[user_id] = []
        user_last_draw_time[user_id] = int(time.time())  # Инициализируем время

    # Проверяем, сколько карт уже получено
    if len(user_received_cards[user_id]) < 2:
        # Выбор одной случайной карты
        card_number = random.choice(weighted_numbers)  # Выбираем одну карту
        user_received_cards[user_id].append(card_number)  # Добавляем карту в список полученных
        user_last_draw_time[user_id] = int(time.time())  # Обновляем время получения карты

        # Отправляем карту пользователю
        if card_number in card_images:
            card_text = card_texts.get(card_number, f"Ваша карта: {card_number}")
            bot.send_photo(message.chat.id, card_images[card_number], caption=card_text)
        elif card_number in card_videos:
            card_text = card_texts.get(card_number, f"Ваша карта: {card_number}")
            bot.send_video(message.chat.id, card_videos[card_number], caption=card_text)
        else:
            bot.send_message(message.chat.id, f"Ваша карта: {card_number}")
    else:
        # Проверяем, прошло ли 1 час с последнего получения
        current_time = int(time.time())
        elapsed_time = current_time - user_last_draw_time[user_id]
        if elapsed_time >= 3600:  # 3600 секунд = 1 час (время ожидания)
            bot.send_message(message.chat.id, "Вы можете получить новые карты. Используйте команду 'получить карту' снова.")
        else:
            remaining_time = 3600 - elapsed_time
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            bot.send_message(message.chat.id, f"Вернусь через {minutes} минут и {seconds} секунд, чтобы получить новые карты.")





bot.polling()

